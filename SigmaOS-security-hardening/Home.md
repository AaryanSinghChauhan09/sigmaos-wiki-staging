# SigmaOS-security-hardening

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS security hardening system with compliance checking and audit capabilities.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Modules (`src/lib.rs`):** `audit`, `compliance`, `error`, `hardening`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-security-hardening`
- **Subcommands / Actions:** `compliancechecker`

```sh
sigmaos-security audit --audit-type all
sigmaos-security audit --audit-type network --format json
sigmaos-security audit --audit-type filesystem
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-security-hardening`
- `component.license` = `GPL-3.0-or-later`
- **Feature flags:** `default`, `selinux`, `apparmor`, `firewall`, `audit`, `encryption`, `compliance`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `serde` (`1.0`)
- `serde_json` (`1.0`)
- `thiserror` (`1.0`)
- `log` (`0.4`)
- `env_logger` (`0.10`)
- `chrono` (`0.4`)

**SigmaOS Component Dependencies:** `sigmaos-config-system`, `sigmaos-update-system`

## Testing
Run the test suite and linter:

```sh
cargo build
cargo test
cargo clippy
cargo fmt
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
