# SigmaOS-ui

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
A cross-framework UI kit for apps that look and feel like SigmaOS, in any toolkit. It has three parts:

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `Cargo.toml`, `bin/`, `build/`, `crates/`, `docs/`, `examples/`, `fixtures/`, `gpui/`, `gtk/`, `kde/`, `packaging/`, `qt/`, `rune/`, `spec/`, `target/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `ui`
- `component.id` = `sigmaos-ui`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

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
