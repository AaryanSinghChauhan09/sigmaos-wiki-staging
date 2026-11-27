# SigmaOS-config-system

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS declarative configuration system providing declarative configuration management.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Modules (`src/lib.rs`):** `config`, `error`, `loader`, `schema`, `validator`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-config-system`
- **Subcommands / Actions:** `load`, `validate`, `generate`, `show`, `set`, `get`

```sh
sigmaos-config-system --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-config-system`
- `component.license` = `GPL-3.0-or-later`
- **Feature flags:** `default`, `toml`, `json`, `yaml`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `serde` (`1.0`)
- `serde_json` (`1.0`)
- `serde_yaml` (`0.9`)
- `toml` (`0.8`)
- `anyhow` (`1.0`)
- `thiserror` (`1.0`)
- `log` (`0.4`)
- `env_logger` (`0.10`)
- `clap` (`4.0`)
- `directories` (`5.0`)

**Dev Dependencies:** `tempfile`

**SigmaOS Component Dependencies:** `sigmaos-build-system`, `sigmaos-update-system`

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
