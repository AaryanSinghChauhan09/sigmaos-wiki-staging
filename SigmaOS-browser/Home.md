# SigmaOS-browser

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS-browser: browser component model. Browser component for SigmaOS

## Architecture
- **Language / Runtime:** `rust` (Tier: `2`, Stability: `beta`)
- **Key Structs:** `BrowserItem`, `BrowserConfig`, `BrowserManager`
- **Key Enums:** `BrowserError`
- **Public Functions:** `new`, `add_item`, `get_item`, `count`, `add_config`, `config_count`, `set_enabled`
- **Provides:** `component`
- **Component Dependencies:** `SigmaOS-system`

## Design Principles
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-browser`

```sh
sigmaos-browser --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-browser`
- `component.tier` = `2`
- `component.stability` = `beta`
- `component.language` = `rust`

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
