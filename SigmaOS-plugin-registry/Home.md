# SigmaOS-plugin-registry

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
The hosted plugin registry for [SigmaOS](https://sigmaos.org) — `plugins.sigmaos.org`. A Rails control plane serving a crates.io-style static data plane: append-only JSON index + immutable, checksummed tarballs, with registry-native accounts, automated review, and a kill-bit for revoking already-installed plugins.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `app/`, `bin/`, `config/`, `db/`, `docs/`, `lib/`, `log/`, `public/`, `script/`, `storage/`, `test/`, `tmp/`, `vendor/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `plugin-registry`
- `component.id` = `sigmaos-plugin-registry`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`
- **Config directory:** `config/` contains runtime configuration templates.

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
