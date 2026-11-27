# SigmaOS-data-wrangling

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS data-wrangling — ETL pipeline engine. Declarative pipelines over JSON records: filter, map, aggregate, sort, limit, dedup. Sources read JSON files/arrays; sinks write JSON. SigmaOS component: **data-wrangling**.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Key Structs:** `Pipeline`
- **Key Enums:** `WrangleError`, `Transform`
- **Public Functions:** `apply_step`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-data-wrangling`
- **Subcommands / Actions:** `run`, `transform`, `show`, `savetemplate`

```sh
sigmaos-data-wrangling --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `data-wrangling`
- `component.id` = `sigmaos-data-wrangling`
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
