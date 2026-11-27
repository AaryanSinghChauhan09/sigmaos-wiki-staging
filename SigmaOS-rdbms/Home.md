# SigmaOS-rdbms

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS RDBMS component — database interoperability primitives. SQL identifier quoting per dialect, connection-string parsing, and schema-qualified name handling. Safe Rust, no unsafe code. SigmaOS component: **rdbms**.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Key Structs:** `ConnParams`
- **Key Enums:** `Dialect`, `RdbmsError`
- **Public Functions:** `quote_ident`, `quote_qualified`, `parse_conn_string`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-rdbms`

```sh
sigmaos-rdbms --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `rdbms`
- `component.id` = `sigmaos-rdbms`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

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
