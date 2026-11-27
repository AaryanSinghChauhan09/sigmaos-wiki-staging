# SigmaOS-aether

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
A visual theming application for SigmaOS. Extract colors from wallpapers and apply cohesive themes across your entire desktop.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `Makefile`, `assets/`, `build/`, `cli/`, `contrib/`, `docs/`, `examples/`, `frontend/`, `go.mod`, `install.sh`, `internal/`, `ipc/`, `package.json`, `templates/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference

```sh
aether --generate ~/wallpaper.jpg
aether --apply-blueprint "My Theme"
aether --list-blueprints
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `aether`
- `component.id` = `sigmaos-aether`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
Go toolchain (see `go.mod` for module dependencies).

## Testing
Run the test suite and linter:

```sh
make
make test
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
