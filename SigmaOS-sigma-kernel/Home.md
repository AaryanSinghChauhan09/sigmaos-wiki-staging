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
