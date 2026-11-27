# SigmaOS-pager

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
A notification daemon for [SigmaOS](https://sigmaos.org) with grouped notifications, inline actions and screen-sharing detection. Replaces the built-in notification service and follows your SigmaOS theme.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `assets/`, `bin/`, `docs/`, `security/`, `tests/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-pager`
- `component.id` = `sigmaos-pager`
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
