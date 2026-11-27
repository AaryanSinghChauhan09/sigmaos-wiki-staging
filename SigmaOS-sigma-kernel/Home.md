# SigmaOS-sigma-kernel

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS kernel — no_std bare-metal OS core, bootable in QEMU via PVH. Boots Multiboot2/PVH start info, mounts a cpio initramfs into a writable VFS (with /proc), loads ELF64 userspace into ring 3 with per-process page tables, and runs a multitasking process model: fork/exec/spawn/wait, round-robin scheduler, signals, blocking pipes, fd redirection, and ~35 syscalls (nr 0-38). Includes VirtIO block/net/gpu/MMIO drivers, PS/2 + serial console, and a linear-framebuffer drawing library.

## Architecture
- **Language / Runtime:** `rust` (Tier: `2`, Stability: `scaffold`)
- **Modules (`src/lib.rs`):** `agent`, `boot`, `compositor`, `console`, `elf`, `error`, `fat32`, `fb`, `fb_console`, `installer`, `mm`, `process`, `ps2`, `syscall`, `theme`, `uart`, `usermem`, `vfs`, `virtio`, `virtio_blk`, `virtio_gpu`, `virtio_mmio`, `virtio_net`, `window_manager`
- **Provides:** `component`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigma-kernel`

```sh
sigma-kernel --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-sigma-kernel`
- `component.tier` = `2`
- `component.stability` = `scaffold`
- `component.language` = `rust`
- **Feature flags:** `default`, `test-std`

## Dependencies
Standard SigmaOS runtime environment (no external Rust crate dependencies).

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
