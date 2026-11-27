# SigmaOS-shell-config

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS shell-config — declarative shell configuration manager. Manages bar, dock, launcher, and theming configuration for the SigmaOS desktop shell (Quickshell-based). All configuration is declarative TOML; this crate validates, merges, and applies it idempotently. SigmaOS component inspired by the corresponding SigmaOS repository.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Key Structs:** `BarConfig`, `BarModule`, `DockConfig`, `LauncherConfig`, `ThemeConfig`, `ShellConfig`
- **Key Enums:** `ShellConfigError`, `BarPosition`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-shell-config`
- **Subcommands / Actions:** `validate`, `default`, `apply`, `path`, `module`

```sh
sigmaos-shell-config --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `shell-config`
- `component.id` = `sigmaos-shell-config`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `serde` (`1.0`)
- `toml` (`0.8`)
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
