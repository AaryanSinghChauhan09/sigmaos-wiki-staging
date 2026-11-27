# SigmaOS-plugin-marketplace

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS-plugin-marketplace — plugin catalog & installer. A marketplace is a catalog of available plugins (metadata + download info) with search, install, update, and uninstall workflows. It delegates actual installation to a `MarketBackend` (which typically wraps the plugin-registry + a fetch source). Keeps an install history and supports pinned versions.

## Architecture
- **Language / Runtime:** `rust` (Tier: `3`, Stability: `active`)
- **Key Structs:** `CatalogEntry`, `InstalledEntry`, `HostBackend`
- **Key Enums:** `MarketError`
- **Traits:** `MarketBackend`

## Design Principles
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `SigmaOS-plugin-marketplace`

```sh
SigmaOS-plugin-marketplace --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-plugin-marketplace`
- `component.tier` = `3`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `serde` (`1`)
- `serde_json` (`1`)

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
