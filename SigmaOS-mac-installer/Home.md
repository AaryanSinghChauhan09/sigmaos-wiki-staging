# SigmaOS-mac-installer

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
A macOS app that installs [SigmaOS](https://github.com/AaryanSinghChauhan09/SigmaOS) on an Apple Silicon Mac, next to macOS. The app is named **SigmaOS Installer** and uses the `org.sigmaos.installer` identifiers (`Packaging/identity.conf`). It was extracted from [maralcbr/sigmaos-mx-mac](https://github.com/maralcbr/sigmaos-mx-mac) into [AaryanSinghChauhan09/SigmaOS-mac-installer](https://github.com/AaryanSinghChauhan09/SigmaOS-mac-installer); the Git history and attribution are preserved (see [extraction provenance](docs/extraction.md)).

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `Design/`, `Development/`, `Engine/`, `Packaging/`, `Plugins/`, `Recovery/`, `Release/`, `Sources/`, `Tests/`, `docs/`, `evidence/`, `image-builder/`, `scripts/`, `test/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `mac-installer`
- `component.id` = `sigmaos-mac-installer`
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
