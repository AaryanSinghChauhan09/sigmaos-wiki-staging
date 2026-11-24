# SigmaOS Kernel (sigma-kernel)

`no_std` operating system core — the heart of SigmaOS.

## Subsystems

| Module | Responsibility |
|--------|---------------|
| `boot` | Multiboot2 info struct + tag parser (mem map, framebuffer, cmdline) |
| `mm` | Bitmap physical frame allocator (4 KiB frames, contiguous alloc) |
| `vfs` | Virtual FS trait + cpio "newc" initramfs parser/writer |
| `uart` | 16550 serial: register map, polled TX/RX, DLAB-aware |
| `virtio` | VirtIO-MMIO registers + split virtqueue descriptor tracker |
| `syscall` | x86_64 syscall ABI: numbers, arg registers, arity table |
| `fb` | Linear framebuffer: pixel formats, rect fill, 8x8 font text |

## Constants

- `HIGHER_HALF_BASE` = `0xFFFF_8000_0000_0000`
- `KERNEL_LOAD_ADDR` = `0x100_000` (1 MiB)
- `KERNEL_VERSION` = `0.1.0`

## Interconnectivity

- `sigmaos-sigma-bootloader` — produces the MB2 header this parses
- `sigmaos-initramfs` — hook plans feed the cpio archive loaded here
- `sigmaos-system-profile` — kernel cmdline/profile options

## Status

Real implementation (was stub). 26 tests passing, `#![no_std]`,
`#![forbid(unsafe_code)]`, GPL-3.0.
