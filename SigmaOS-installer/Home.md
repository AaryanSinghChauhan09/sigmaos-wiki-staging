# SigmaOS-installer

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS-installer — installer component for SigmaOS Installer component for SigmaOS — installation state machine for the partition/copy/bootloader flow. Disk operations are future work.

## Architecture
- **Language / Runtime:** `rust` (Tier: `2`, Stability: `beta`)
- **Modules (`src/lib.rs`):** `sigmainstaller`
- **Key Structs:** `Component`
- **Key Enums:** `ComponentError`
- **Public Functions:** `new`, `init`, `is_ready`, `run`, `name`, `reset`
- **Provides:** `system-installer`, `disk-partitioner`, `luks-encryption-wizard`
- **Component Dependencies:** `SigmaOS-ISO`, `SigmaOS-system`

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
- `component.name` = `SigmaOS-installer`
- `component.tier` = `2`
- `component.stability` = `beta`
- `component.language` = `rust`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `thiserror` (`1`)

## Testing
Run the test suite and linter:

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
