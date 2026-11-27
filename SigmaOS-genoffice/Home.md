# SigmaOS-genoffice

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
- **Category:** Office - **Engine:** office - **Language:** Rust

## Architecture
- **Language / Runtime:** `rust` (Tier: `3`, Stability: `beta`)
- **Key Structs:** `GenOfficeDocument`, `GenOfficeSuite`
- **Key Enums:** `DocumentFormat`
- **Public Functions:** `from_extension`, `from_path`, `new`, `mark_offline_ready`, `mime_type`, `new`, `register_app`, `has_app`, `apps`
- **Provides:** `genoffice-suite`, `format-registry`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-genoffice`
- `component.tier` = `3`
- `component.stability` = `beta`
- `component.language` = `rust`

## Dependencies
Standard SigmaOS runtime environment (no external Rust crate dependencies).

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
