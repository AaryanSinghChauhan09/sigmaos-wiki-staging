# SigmaOS-system-profile

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS system profile — declarative whole-system configuration. A `system.toml` profile composes per-component configs into one declarative system definition using the SigmaOS config system design. The profile names which components are enabled and where each component's config lives; `resolve` merges them into a single effective view for validation and generation. Declarative whole-system configuration — a SigmaOS declarative config-style `system.toml` that composes every component's config into one system definition.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Key Structs:** `ComponentEntry`, `SystemProfile`, `ResolvedComponent`, `ResolvedSystem`
- **Key Enums:** `ProfileError`
- **Public Functions:** `load`, `save`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-system-profile`

```sh
sigmaos-system-profile --profile system.toml           # show resolved view
sigmaos-system-profile --profile system.toml --json    # JSON output
sigmaos-system-profile --profile system.toml --validate
sigmaos-system-profile --profile system.toml --list    # enabled components
sigmaos-system-profile --init                        # write default profile
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-system-profile`
- `component.license` = `GPL-3.0-or-later`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `serde` (`1`)
- `serde_json` (`1`)
- `toml` (`0.8`)
- `thiserror` (`2`)
- `clap` (`4`)
- `env_logger` (`0.11`)
- `log` (`0.4`)
- `directories` (`6`)

**SigmaOS Component Dependencies:** `sigmaos-config-system`, `sigmaos-shell-config`, `sigmaos-update-system`

## Testing
Run the test suite and linter:

```sh
cargo test
cargo clippy --all-targets -- -D warnings
cargo fmt --check
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
