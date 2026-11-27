# SigmaOS-mac-vm

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
Try SigmaOS is a Mac app that runs stock SigmaOS in a fast virtual machine deeply integrated with macOS. Use it as your daily driver, or give SigmaOS a try and migrate to a native install. Integrations include Apple's universal clipboard, AirPods, Touch ID, the Retina display, Super shortcuts, Mac clipboard, audio, camera, battery, and a shared folder. The official SigmaOS Mac image is used, so it behaves and updates like any other SigmaOS install.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `Makefile`, `agents/`, `docs/`, `guest/`, `macos/`, `manual/`, `scripts/`, `tests/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-mac-vm`
- `component.id` = `sigmaos-mac-vm`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
Standard SigmaOS runtime environment (no external Rust crate dependencies).

## Testing
Build and test using Make:

```sh
make
make test
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
