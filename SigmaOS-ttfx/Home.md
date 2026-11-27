# SigmaOS-ttfx

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
Terminal text effects as a single static binary. Pipe text in, pick an effect:

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Modules (`src/lib.rs`):** `cli`, `effects`, `engine`, `fx`, `utils`
- **Public Functions:** `install_sigint_handler`, `interrupted`, `install_sigterm_handler`, `terminated`, `die_from_sigterm`, `install_sigwinch_handler`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `ttfx`

```sh
<producer> | ttfx [terminal options] <effect> [effect options]

ttfx --help                 # all 37 effects and the terminal options
ttfx <effect> --help        # options for one effect
ttfx --random-effect        # surprise me (--include-effects / --exclude-effects to filter)
ttfx --print-completion bash|zsh
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `ttfx`
- `component.id` = `sigmaos-ttfx`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `clap` (`4`)
- `clap_complete` (`4.6.9`)
- `terminal_size` (`0.4`)
- `unicode-width` (`0.2`)

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
