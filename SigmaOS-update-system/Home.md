# SigmaOS-update-system

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS rolling release update system with automatic updates and rollback capabilities.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Modules (`src/lib.rs`):** `channel`, `error`, `notifier`, `updater`
- **Key Capabilities:**
  - `UpdateManager::with_paths()` for isolated config/state management
  - `UpdateManager::validate_package_artifact()` for non-empty archive and signature checks
  - `UpdateManager::rollback()` / `rollback_to_previous()` / `apply_rollback()` for persisted state restoration
  - `SIGMA_PKG_BIN` environment override (defaults to `sigma-pkg`)

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-update-system`
- **Subcommands / Actions:** `check`, `update`, `rollback`, `status`, `config`

```sh
sigmaos-update-system --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-update-system`
- `component.license` = `GPL-3.0-or-later`
- **Feature flags:** `default`, `stable`, `beta`, `nightly`, `auto-update`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `serde` (`1.0`)
- `serde_json` (`1.0`)
- `toml` (`0.8`)
- `anyhow` (`1.0`)
- `thiserror` (`1.0`)
- `log` (`0.4`)
- `env_logger` (`0.10`)
- `clap` (`4.0`)
- `reqwest` (`0.11`)
- `tokio` (`1.0`)
- `semver` (`1.0`)
- `directories` (`5.0`)
- `notify` (`6.0`)
- `chrono` (`0.4.45`)

**Dev Dependencies:** `tempfile`, `mockito`

**SigmaOS Component Dependencies:** `sigmaos-config-system`, `sigmaos-build-system`

## Testing
Run the test suite and linter:

```sh
cargo build
cargo test
cargo clippy
cargo fmt
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
