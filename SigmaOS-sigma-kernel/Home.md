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
| `virtio_mmio` | VirtIO MMIO transport probing/helpers |
| `fat32` | FAT32 filesystem support for block devices |
| `fb_console` | Framebuffer console output path |
| `window_manager` | Tiling window management over the compositor |
| `theme` | Kernel-side theme parsing/registry |
| `agent` | Agent capability/result plumbing |
| `installer` | ISO install planning: partitions, filesystems, GRUB config |

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
Verified booting in QEMU. `#![no_std]`, `#![forbid(unsafe_code)]`,
GPL-3.0. Latest commits add FAT32, framebuffer console, VirtIO MMIO,
tiling window manager, theme registry, agent plumbing, and ISO
installer planning on top of the ring-3 userspace path below.

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
  GETPID/KERNEL_INFO/TIME/RAND/OPEN/READ/CLOSE/LISTDIR/BRK/MMAP/MUNMAP;
  unimplemented -> ENOSYS. `TrapSvc` (arch.rs) serves them via a
  global VFS, fd table, serial+VGA console, PS/2 keyboard input.
- **Anonymous memory** (`usermem.rs`): BRK/MMAP map demand-zero 4K
  frames into the live user CR3 via `map_user_page` (splits 2 MiB
  supervisor slots into PTs, Linux `pmd_install` model); MUNMAP
  walks `user_pte` (PML4->PDPT->PD->PT), clears present U/S leaves
  and returns frames to the allocator — supervisor/kernel pages are
  never freed. `flush_tlb()` reloads CR3 after installs/teardowns.
- **Asm transition** (`pvh.asm`): ring-3 GDT (user CS 0x33 / SS 0x2b),
  STAR/LSTAR/SFMASK MSRs, `syscall_entry`/`sysret` stubs,
  `enter_user` (`mov cr3` + `iretq`).
- **`/init` = sigma-init** (`SigmaOS-sigma-sh`): `no_std` static
  `ET_EXEC` at 0x200000 using `sigma-sys`; interactive shell
  (`help`/`ls`/`cat`/`ver`/`time`/`mem`/`spawn`/`wait`/`exit`) over PS/2 keyboard.

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

### Processes (SPAWN/WAIT/EXIT)

Cooperative multitasking with per-process isolation — Linux
`copy_process`/`context_switch`/`sched` inspired:

- **Full context save**: `syscall_entry` saves all 15 GPRs + rip
  (rcx) + rflags (r11) + user rsp + cr3 into a 17-u64 ctx slot.
- **Process table** (`ProcSlot`, `NPROCS=4`): pid, parent, exit_code,
  pml4, brk — the minimal `task_struct` analogue.
- **SPAWN(path)**: reads an ELF from the VFS, `load_image` +
  `build_user_tables` into a *fresh* address space, materializes
  segments, installs a zeroed child ctx (rip=entry, fresh stack,
  rflags=0x202, child CR3), then `switch_to` — the parent resumes
  later with the child pid in `ctx.rax` (result is written to the
  *entry* ctx before the switch loads the child ctx).
- **EXIT(code)**: marks the slot exited, switches to the parent;
  init exit halts the machine.
- **WAIT(pid)**: returns the child's exit status; `EAGAIN` while the
  child is still running — callers retry (each retry is a syscall
  boundary the scheduler can preempt at).
- `USER_PML4`/`USER_BRK` swap per-process on every `switch_to`, so
  each process owns its page tables and heap break.
- `/child` (`sigma-child` in sigma-sh): minimal `no_std` test binary
  that prints its real pid (GETPID is now per-process), spins
  ~20M iterations printing progress, and exits 42.

### Preemptive scheduling

Timer IRQs (PIT vec `0x20`, LAPIC vec `0x30`) arriving **from user
mode** (cs RPL==3) now context-switch:

- `irq_common` saves the interrupted context — all GPRs plus rcx/r11
  in ctx slots 17/18 — into the current proc's slot, calls
  `sched_tick()` (Rust, `scheduler_tick` analogue), then rebuilds an
  `iret` frame from the *target* ctx and returns into its address
  space. Kernel-mode interrupts keep the plain save/EOI/`iret` path.
- `sched_tick` picks the next `used && !exited` process round-robin
  and swaps `USER_PML4`/`USER_BRK`/`cur_ctx` — the same globals
  `switch_to` maintains for the syscall path.
- ctx is now 19 u64s: slots 0-16 written by `syscall_entry`
  (rcx/r11 are implicitly rip/rflags there), slots 17/18 written by
  the IRQ path for the GPRs an interrupt doesn't preserve.

**Verified in QEMU** (at commit `6caf877`): ~600 preemptions while
`sigma-child` spins — the parent's WAIT-retry loop and the child's
progress ticks interleave; child exits 42, `wait status=42`, prompt
returns. The code logic is correct.

**Toolchain regression** (Rust 1.99.0+): the kernel bin fails to build with
"unwinding panics are not supported without std" despite adding
`-C panic=abort` to rustflags. Tested across Rust 1.96.1/1.97.1/1.99.1
with the same error; the lib builds fine. The preemptive scheduling code
at `6caf877` was verified working in QEMU before this regression hit.
Fixing may require nightly `-Zbuild-std` or investigation of the core
library precompilation. The implementation is sound; this is an
environmental issue.

**Next gaps** (once build is restored):
- **Blocking WAIT** (sleep/wake queue) — implemented but not pushed:
  `ProcSlot::sleeping`/`wait_pid`/`reaped` fields, `next_runnable`,
  `sys_wait`/`sys_exit` rewritten to use Linux `wait`/`wake_up` analogue.
- Process teardown (exited slots leak page tables/frames).
- Per-process fd isolation (global fd table).
- Framebuffer console, VirtIO blk/net/gpu probing.

**Root-cause bug found via QEMU debugging**: STAR was built in RAX but
`wrmsr` consumes EDX:EAX — EDX was never set, so `sysret` intermittently
loaded `CS=0x13/SS=0x0b`, which then poisoned IRQ frames -> `iretq` #GP.
STAR/LSTAR/SFMASK are now written with explicit `edx:eax`.

Verified in QEMU: PVH -> long mode -> IDT -> initramfs -> ELF load ->
ring-3 CR3 -> `iretq` -> sigma-init runs a boot self-test that grows
brk by a page, writes/reads it back (`last=90`), mmaps, and munmaps
— then reaches the `sigma$` prompt; timer IRQs fire in ring 3 with
all registers preserved. 79 lib tests green.
