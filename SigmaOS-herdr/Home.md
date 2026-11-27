# SigmaOS-herdr

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
English · <a href="README.zh-CN.md">简体中文</a> </p>

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `Cargo.toml`, `assets/`, `docs/`, `nix/`, `packaging/`, `scripts/`, `skills/`, `src/`, `target/`, `tests/`, `vendor/`, `website/`, `workers/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `herdr`
- **Subcommands / Actions:** `disablebracketedpaste`, `enablefocuschange`, `pushkeyboardenhancementflags`

```sh
herdr --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `herdr`
- `component.id` = `sigmaos-herdr`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `base64` (`0.22.1`)
- `bincode` (`2`)
- `bytes` (`1`)
- `clap` (`4.5`)
- `clap_complete` (`4.5`)
- `crossterm` (`0.29`)
- `ctrlc` (`3`)
- `interprocess` (`2.4.2`)
- `jsonc-parser` (`0.33.1`)
- `libc` (`0.2`)
- `portable-pty` (`=0.9.0`)
- `png` (`0.17`)
- `ratatui` (`0.30`)
- `regex` (`1`)
- `serde` (`1`)
- `serde_ignored` (`0.1.14`)
- `serde_json` (`1`)
- `sha2` (`0.10`)
- `time` (`0.3.47`)
- `tokio` (`1`)

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
