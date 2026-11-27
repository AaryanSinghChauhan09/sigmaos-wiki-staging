# SigmaOS-sigma-kernel

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS kernel — no_std operating system core. Modules: boot info parsing (Multiboot2/Limine), physical memory management, VFS with cpio initramfs, 16550 UART, VirtIO-MMIO queues, syscall ABI, and linear framebuffer output. SigmaOS sigma-kernel - modular Rust crate for the SigmaOS system

## Architecture
- **Language / Runtime:** `rust` (Tier: `2`, Stability: `scaffold`)
- **Modules (`src/lib.rs`):** `agent`, `boot`, `compositor`, `console`, `elf`, `error`, `fat32`, `fb`, `fb_console`, `installer`, `mm`, `process`, `ps2`, `syscall`, `theme`
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
