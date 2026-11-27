# SigmaOS-video

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
Omareel is a native screen recorder and editor for SigmaOS and Hyprland. It captures the screen without the system cursor, records pointer and keyboard activity separately, and then renders a smooth synthetic cursor, click effects, rounded framing, backgrounds, and automatic cursor-following zooms. Finished projects export to MP4 or GIF.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `CMakeLists.txt`, `Cargo.toml`, `LICENSES/`, `assets/`, `bin/`, `cmake/`, `crates/`, `docs/`, `pkg/`, `plugin/`, `src/`, `target/`, `tests/`, `tools/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-video`
- `component.id` = `sigmaos-video`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
C++17 / CMake / Qt6 toolchain (see `CMakeLists.txt`).

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
