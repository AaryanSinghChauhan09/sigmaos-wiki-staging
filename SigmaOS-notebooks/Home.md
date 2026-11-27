# SigmaOS-notebooks

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS notebooks component — Jupyter notebook (.ipynb) handling. Parses notebook JSON into structured cells, extracts code/markdown, and computes notebook statistics. Safe Rust, no unsafe code. Uses only `serde_json`-free minimal parsing via manual JSON walk — kept dependency-free for portability.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Key Structs:** `Cell`, `Notebook`
- **Key Enums:** `NotebookError`, `CellType`
- **Public Functions:** `counts`, `code_source`, `source_of`, `line_count`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-notebooks`

```sh
sigmaos-notebooks --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `notebooks`
- `component.id` = `sigmaos-notebooks`
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
