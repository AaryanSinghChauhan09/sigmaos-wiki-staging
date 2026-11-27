# SigmaOS-iloveapi

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS iloveapi — file conversion API abstraction. Provider-agnostic conversion job manager: jobs track source file, target format, provider, and status. Actual conversion is delegated to a `ConversionProvider` implementation (HTTP, local tool, mock). SigmaOS component: **iloveapi**.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Key Structs:** `ConvertJob`, `JobManager`
- **Key Enums:** `ConvertError`, `JobStatus`
- **Traits:** `ConversionProvider`
- **Public Functions:** `create`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-iloveapi`
- **Subcommands / Actions:** `queued`, `processing`, `done`, `failed`, `create`, `run`, `list`, `show`, `remove`, `path`

```sh
sigmaos-iloveapi --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `iloveapi`
- `component.id` = `sigmaos-iloveapi`
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
- `uuid` (`1.0`)

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
