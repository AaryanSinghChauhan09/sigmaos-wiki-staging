# SigmaOS-build-system

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
- **Category:** DevOps - **Engine:** build_ci - **Language:** Rust

## Architecture
- **Language / Runtime:** `rust` (Tier: `2`, Stability: `scaffold`)
- **Modules (`src/lib.rs`):** `builder`, `error`, `package`, `verifier`
- **Provides:** `component`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-build-system`

```sh
sigmaos-build-system --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-build-system`
- `component.tier` = `2`
- `component.stability` = `scaffold`
- `component.language` = `rust`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `serde` (`1.0`)
- `serde_json` (`1.0`)
- `thiserror` (`1.0`)
- `log` (`0.4`)
- `env_logger` (`0.10`)
- `chrono` (`0.4`)
- `walkdir` (`2`)
- `toml` (`0.8`)
- `directories` (`5`)

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
