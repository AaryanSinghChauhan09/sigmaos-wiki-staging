# SigmaOS-mac-pkgs

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
**Want SigmaOS on your Mac?** Use the [SigmaOS Installer](https://github.com/AaryanSinghChauhan09/SigmaOS-mac-installer), or `brew install SigmaOS/mac/sigmaos`. This repository holds the packages it installs. It is not an installer, and it is not a copy of SigmaOS.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `mac-manual/`, `omarchy-mac/`, `omarchy-mac-boot/`, `test/`, `tools/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference

```sh
sigmaos-mac/test/all
sigmaos-mac-boot/test/all
OMARCHY_TEST_RUNTIME=~/code/sigmaos test/integration/all
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-mac-pkgs`
- `component.license` = `GPL-3.0-or-later`

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
