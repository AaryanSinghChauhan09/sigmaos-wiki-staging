# SigmaOS-pixel.nvim

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
A dynamic Neovim colorscheme that adapts to your terminal's color palette, inspired by the bat command-line tool's approach to color theming.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `colors/`, `lua/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `pixel.nvim`
- `component.id` = `sigmaos-pixel.nvim`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
Standard SigmaOS runtime environment (no external Rust crate dependencies).

## Testing
Verify component integrity and scripts in the repository root:

```sh
# Check repository scripts and configuration
ls -la
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
