# SigmaOS-initramfs

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS-initramfs — SigmaOS initramfs component following standard Linux initramfs conventions. Ordered execution plan: validated steps executed fail-fast, first error aborts. Principles: single responsibility, fail-fast, defensive programming, component isolation, stable API, deterministic tests. Initramfs builder with two layers:

## Architecture
- **Language / Runtime:** `rust` (Tier: `2`, Stability: `beta`)
- **Modules (`src/lib.rs`):** `cpio`, `pack`
- **Key Structs:** `Plan`
- **Key Enums:** `PlanError`
- **Public Functions:** `new`, `add_step`, `len`, `is_empty`, `validate`, `run`
- **Provides:** `component`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos_initramfs`

```sh
cargo run -- --config /etc/sigmaos/initramfs.toml --dry-run
cargo run -- --config initramfs.toml --json
cargo run -- --rootfs /path/to/rootfs --out /boot/initramfs.img
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-initramfs`
- `component.tier` = `2`
- `component.stability` = `beta`
- `component.language` = `rust`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `serde` (`1`)
- `serde_json` (`1`)
- `toml` (`0.8`)
- `thiserror` (`2`)
- `clap` (`4`)
- `env_logger` (`0.11`)
- `log` (`0.4`)
- `directories` (`6`)
- `flate2` (`1`)
- `zstd` (`0.14`)

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
