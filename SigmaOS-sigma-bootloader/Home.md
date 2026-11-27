# SigmaOS-sigma-bootloader

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS bootloader — Multiboot2 boot header and tag generation. Produces the MB2 header embedded in the kernel image: magic, arch, header length, checksum, and header tags requesting framebuffer, memory map, and module loading. SigmaOS sigma-bootloader - modular Rust crate for the SigmaOS system

## Architecture
- **Language / Runtime:** `rust` (Tier: `2`, Stability: `scaffold`)
- **Key Structs:** `Module`, `Mb2Header`
- **Key Enums:** `BootError`
- **Public Functions:** `sigmaos_default`
- **Provides:** `component`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-sigma-bootloader`
- `component.tier` = `2`
- `component.stability` = `scaffold`
- `component.language` = `rust`
- **Feature flags:** `default`

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
