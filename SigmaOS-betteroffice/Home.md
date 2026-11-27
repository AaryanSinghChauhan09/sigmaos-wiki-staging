# SigmaOS-betteroffice

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS betteroffice — office document model. Unified document model for text docs, spreadsheets, and slides. Documents serialize to a SigmaOS office JSON format (.sdoc). SigmaOS component: **betteroffice**.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Key Structs:** `TextDoc`, `SheetDoc`, `Slide`, `SlidesDoc`, `Document`
- **Key Enums:** `OfficeError`, `DocKind`
- **Public Functions:** `column_sum`, `row_count`, `col_count`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-betteroffice`
- **Subcommands / Actions:** `new`, `show`, `validate`, `list`

```sh
sigmaos-betteroffice --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `betteroffice`
- `component.id` = `sigmaos-betteroffice`
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
