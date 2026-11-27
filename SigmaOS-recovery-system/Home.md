# SigmaOS-recovery-system

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS system recovery and rollback system with snapshot management.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Modules (`src/lib.rs`):** `error`, `recovery`, `restore`, `snapshot`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-recovery-system`
- **Subcommands / Actions:** `snapshot`, `list`, `restore`, `delete`, `status`

```sh
sigmaos-recovery-system --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-recovery-system`
- `component.license` = `GPL-3.0-or-later`
- **Feature flags:** `default`, `compression`, `encryption`, `incremental`

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
- `walkdir` (`2.0`)
- `sha2` (`0.10`)
- `hex` (`0.4`)
- `directories` (`5.0`)
- `rand` (`0.10.4`)
- `chrono` (`0.4.45`)

**Dev Dependencies:** `tempfile`

**SigmaOS Component Dependencies:** `sigmaos-config-system`, `sigmaos-update-system`

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
