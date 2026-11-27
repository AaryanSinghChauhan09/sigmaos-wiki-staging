# SigmaOS-ISO

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS ISO Builder Multi-architecture ISO image builder with bootloader integration and live session creation Principles: - ZERO-COPY: Efficient file operations - FAIL-FAST: Early validation - LAYERED DESIGN: Separation of mechanism and policy - KISS: Simple, focused implementation The bootable SigmaOS system: an Linux-based live ISO with a pre-configured SigmaOS-inspired Hyprland desktop, plus the installer and release pipeline. This is the repository that produces the downloadable `.iso`.

## Architecture
- **Language / Runtime:** `rust` (Tier: `0`, Stability: `active`)
- **Modules (`src/lib.rs`):** `installer`, `iso`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.
- **Declared Capabilities:** DRY, KISS, SOLID, Arrange-Act-Assert, Pristine-Sources.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-ISO`
- `component.tier` = `0`
- **Feature flags:** `default`, `std`, `no_std`, `standalone_test`

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
