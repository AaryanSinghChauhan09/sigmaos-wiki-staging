# SigmaOS-m1n1

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
You need an `aarch64-linux-gnu-gcc` cross-compiler toolchain (or a native one, if running on ARM64). You will also need to install the `aarch64-unknown-none-softfloat` toolchain for rust.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `3rdparty_licenses/`, `Makefile`, `artwork/`, `data/`, `docs/`, `font/`, `proxyclient/`, `rust/`, `src/`, `sysinc/`, `tests/`, `tools/`, `udev/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `m1n1`
- `component.id` = `sigmaos-m1n1`
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
