# SigmaOS-sigma-sh

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS sigma-sh — minimal rescue shell. Builtins: help, ls, pwd, cd, echo, cat, which, history, export, unset, mem, ps, time, launch, reboot, true/false/:/clear, mkdir/rmdir/rm/touch, `>`/`>>` redirection, `|` pipelines between builtins, plus `*` glob expansion in arguments. `launch` resolves bare names through PATH. exit.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Traits:** `Io`, `Fs`, `ProcTable`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigma-sh`, `sigma-init`, `ls`, `cat`, `ps`, `pkg`, `kill`, `mount`, `sigma-child`, `sh`

```sh
sigma-sh --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-sigma-sh`
- `component.license` = `GPL-3.0-or-later`
- **Feature flags:** `default`, `sigmaos-target`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `sigmaos-sigma-sys` (`*`)

**SigmaOS Component Dependencies:** `sigmaos-sigma-sys`, `sigmaos-sigma-kernel`

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
