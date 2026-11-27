# SigmaOS-plain

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
Plain is SigmaOS's text editor for config files: the editor you don't have to learn. Ctrl+S saves, Ctrl+Z undoes, Ctrl+F finds, and the window closes like any other. It follows SigmaOS's theme, font and language, colors Lua, hyprlang/INI, TOML, JSON, YAML, shell and CSS in the theme's palette, and keeps to one window and one file, with the folder's files beside it when you want them.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `CMakeLists.txt`, `bin/`, `docs/`, `pkgbuild/`, `scripts/`, `src/`, `tests/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `plain`
- `component.id` = `sigmaos-plain`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
C++17 / CMake / Qt6 toolchain (see `CMakeLists.txt`).

## Testing
Verify component integrity and scripts in the repository root:

```sh
# Check repository scripts and configuration
ls -la
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
