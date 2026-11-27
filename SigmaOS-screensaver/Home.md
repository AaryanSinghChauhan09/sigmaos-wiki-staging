# SigmaOS-screensaver

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
The [SigmaOS](https://sigmaos.org) screensaver: a native Wayland overlay on every display that animates your branding text with [ttfx](https://github.com/AaryanSinghChauhan09/SigmaOS-ttfx) effects. A key press, click, scroll or mouse movement dismisses it.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Modules (`src/lib.rs`):** `engine`, `launch`, `options`, `raster`, `vt`, `wayland`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `omarchy-launch-screensaver`

```sh
omarchy-launch-screensaver --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `screensaver`
- `component.id` = `sigmaos-screensaver`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `anyhow` (`1`)
- `clap` (`4`)
- `fontdue` (`0.9`)
- `fs2` (`0.4`)
- `signal-hook` (`0.3`)
- `smithay-client-toolkit` (`0.21.1`)
- `ttfx` (`*`)
- `wayland-client` (`0.31`)

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
