# SigmaOS-pkg-core

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS pkg-core — package management core. Provides a local package database, dependency resolution, and transaction planning for the SigmaOS package manager. Backed by JSON on disk. SigmaOS component: **pkg-core** — see docs/FUTURE_PLAN_DISTROS.md in the main SigmaOS repository for rationale.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Key Structs:** `Package`, `Version`
- **Key Enums:** `PkgError`, `Constraint`
- **Public Functions:** `valid_name`, `parse`, `matches`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-pkg-core`
- **Subcommands / Actions:** `list`, `search`, `deps`, `add`, `install`, `remove`, `orphans`, `path`

```sh
sigmaos-pkg-core --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `pkg-core`
- `component.id` = `sigmaos-pkg-core`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `serde` (`1.0`)
- `serde_json` (`1.0`)
- `thiserror` (`1.0`)
- `log` (`0.4`)
- `env_logger` (`0.10`)
- `clap` (`4.0`)
- `directories` (`5.0`)

**Dev Dependencies:** `tempfile`

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
