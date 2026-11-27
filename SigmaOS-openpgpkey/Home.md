# SigmaOS-openpgpkey

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
The [Web Key Directory](https://datatracker.ietf.org/doc/draft-koch-openpgp-webkey-service/) (WKD) for sigmaos.org. Any OpenPGP client can fetch SigmaOS's key from the address `pkgs@sigmaos.org`, over HTTPS, with no keyserver.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `package.json`, `public/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `openpgpkey`
- `component.id` = `sigmaos-openpgpkey`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
Node.js / npm runtime (see `package.json`).

## Testing
Verify component integrity and scripts in the repository root:

```sh
# Check repository scripts and configuration
ls -la
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
