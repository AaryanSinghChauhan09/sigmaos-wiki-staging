# SigmaOS-xtask

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
Build runner and QEMU orchestrator for SigmaOS kernel and userspace

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `Cargo.toml`, `src/`, `target/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `xtask`
- **Subcommands / Actions:** `buildkernel`, `builduserspace`, `initramfs`, `kernelelf`, `qemu`, `qemudebug`, `testqemu`, `status`

```sh
xtask --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-xtask`
- `component.license` = `GPL-3.0-or-later`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `clap` (`4`)
- `thiserror` (`2`)
- `serde` (`1`)
- `serde_json` (`1`)
- `toml` (`0.8`)
- `env_logger` (`0.11`)
- `log` (`0.4`)
- `directories` (`6`)

**SigmaOS Component Dependencies:** `sigmaos-sigma-kernel`, `sigmaos-sigma-bootloader`, `sigmaos-initramfs`, `sigmaos-ISO`

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
