# SigmaOS Kernel (sigma-kernel)

`no_std` operating system core — the heart of SigmaOS.

## Subsystems

| Module | Responsibility |
|--------|---------------|
| `boot` | Multiboot2 + PVH (hvm_start_info) parsers -> BootInfo |
| `mm` | Bitmap physical frame allocator (4 KiB frames, contiguous alloc) |
| `vfs` | Virtual FS trait + cpio "newc" initramfs parser/writer |
| `uart` | 16550 serial: register map, polled TX/RX, DLAB-aware |
| `virtio` | VirtIO-MMIO registers + split virtqueue descriptor tracker |
| `syscall` | x86_64 syscall ABI: numbers, arg registers, arity table |
| `fb` | Linear framebuffer: pixel formats, rect fill, 8x8 font text |
| `compositor` | Window list, z-order, damage tracking, software render |
| `virtio_blk` | VirtIO block device: request protocol, sector I/O |
| `virtio_net` | VirtIO net: eth header + packet codec |
| `virtio_gpu` | VirtIO gpu: control message codec |

## Constants

- `HIGHER_HALF_BASE` = `0xFFFF_8000_0000_0000`
- `KERNEL_LOAD_ADDR` = `0x100_000` (1 MiB)
- `KERNEL_VERSION` = `0.1.0`

## Interconnectivity

- `sigmaos-sigma-bootloader` — produces the MB2 header this parses
- `sigmaos-initramfs` — hook plans feed the cpio archive loaded here
- `sigmaos-system-profile` — kernel cmdline/profile options

## Boot

PVH protocol: `src/bin/sigma-kernel/pvh.asm` enters in 32-bit protected
mode (%ebx = hvm_start_info), builds PAE identity page tables, sets
EFER.LME, far-jumps to 64-bit, loads a 32-entry IDT (serial fault
reporter), then calls `pvh_kernel_entry` -> `parse_pvh` -> `boot_ok`.

## Status

Bootable kernel ELF (linked at 0x100000 via `linker.ld` + rust-lld).
Verified booting in QEMU. 46 tests passing, `#![no_std]`,
`#![forbid(unsafe_code)]`, GPL-3.0.

## Userspace & Interrupts (latest)

The kernel now boots all the way into **ring-3 userspace**:

- **ELF loader** (`elf.rs`, `process.rs`): parses ELF64, loads `PT_LOAD`
  segments into allocated frames, relocates `ET_DYN` to `USER_LOAD_BIAS`
  (4 MiB), emits `(vaddr, phys, flags)` page-table mappings.
- **Ring-3 page tables** (`usermem.rs`): builds a user CR3 over a
  `PhysMem` trait — supervisor 2 MiB identity pages keep the kernel
  mapped, 4K U/S pages cover user regions (U/S flag required at *every*
  level). `IdentityPhysMem` in `arch.rs` writes real entries.
- **Syscall ABI** (`syscall.rs`): `dispatch()` routes WRITE/EXIT/
  GETPID/KERNEL_INFO/TIME/RAND/OPEN/READ/CLOSE/LISTDIR/BRK/MMAP;
  unimplemented -> ENOSYS. `TrapSvc` (arch.rs) serves them via a
  global VFS, fd table, serial+VGA console, PS/2 keyboard input.
- **Anonymous memory** (`usermem.rs::map_user_page`): BRK/MMAP map
  demand-zero 4K frames into the live user CR3, splitting 2 MiB
  supervisor slots into PTs on demand (Linux `pmd_install` model).
  `flush_tlb()` reloads CR3 after installs so paging-structure caches
  can't hold stale non-present translations.
- **Asm transition** (`pvh.asm`): ring-3 GDT (user CS 0x33 / SS 0x2b),
  STAR/LSTAR/SFMASK MSRs, `syscall_entry`/`sysret` stubs,
  `enter_user` (`mov cr3` + `iretq`).
- **`/init` = sigma-init** (`SigmaOS-sigma-sh`): `no_std` static
  `ET_EXEC` at 0x200000 using `sigma-sys`; interactive shell
  (`help`/`ls`/`cat`/`ver`/`time`/`mem`/`exit`) over PS/2 keyboard.

### Interrupts

- **TSS** (GDT idx7): RSP0 = kernel stack for ring3->kernel switches.
- **8259 PIC remap**: IRQ0-7 -> vecs 0x20-0x27 (BIOS default sent IRQ0
  to vec 8 = #DF handler).
- **Timers**: PIT ch0 (~1 kHz) + x2APIC LAPIC timer (vec 0x30, periodic,
  MSR 0x80b EOI). IDT extended to 64 entries.
- IRQ path (`irq_common`): IRQ stubs (vec >= 32) save user `rax`
  *before* loading the vector into `eax` — previously `mov $vec,%eax`
  destroyed user `rax`, so every IRQ returned `0x20` to userspace
  (the root cause of intermittent syscall-result corruption and the
  sigma-init `rep movsb` flake). `irq_common` saves the other 14
  GPRs, ticks, sends proper EOI (x2APIC vs PIC), restores all regs
  + user `rax`, `iretq` resumes the interrupted context.
- `syscall_entry` does `cli` + `SFMASK=0x200` (clear IF on entry,
  Linux-style) so IRQs can't land inside kernel syscall handling,
  and restores rdi/rsi/rdx/r10/r8/r9 before `sysret` (syscall_trap
  clobbers them; sysret does not).

**Root-cause bug found via QEMU debugging**: STAR was built in RAX but
`wrmsr` consumes EDX:EAX — EDX was never set, so `sysret` intermittently
loaded `CS=0x13/SS=0x0b`, which then poisoned IRQ frames -> `iretq` #GP.
STAR/LSTAR/SFMASK are now written with explicit `edx:eax`.

Verified in QEMU: PVH -> long mode -> IDT -> initramfs -> ELF load ->
ring-3 CR3 -> `iretq` -> sigma-init runs a boot self-test that grows
brk by a page, writes/reads it back (`last=90`), and mmaps — then
reaches the `sigma$` prompt; timer IRQs fire in ring 3 with all
registers preserved. 78 lib tests green.
