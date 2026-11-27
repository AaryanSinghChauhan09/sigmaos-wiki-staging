# SigmaOS-maclab

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS Mac Lab tests SigmaOS on real Apple Silicon Macs and publishes what it finds. This repository, `sigmaos-maclab`, holds all of it.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `Makefile`, `builder/`, `catalogue/`, `cli/`, `cmd/`, `deploy/`, `docs/`, `go.mod`, `installer/`, `internal/`, `release/`, `schema/`, `scripts/`, `site/`, `specs/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `maclab`
- `component.id` = `sigmaos-maclab`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
Go toolchain (see `go.mod` for module dependencies).

## Testing
Build and test using Make:

```sh
make
make test
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
