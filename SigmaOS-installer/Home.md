# SigmaOS Installer

Installer component for SigmaOS — installation state machine for the partition/copy/bootloader flow.

## Overview

`SigmaOS-installer` is a Rust library that models the installation flow as an explicit state machine: `Welcome → Language → Location → Partitioning → UserSetup → Installation → Complete`, with `Failed` and `Cancelled` terminal states. It tracks per-installation configuration (language, timezone, keyboard, hostname, username, partitioning mode, target disk, filesystem) and progress.

This is the installer backend/state layer. Actual disk partitioning, file copy, and bootloader installation are future work; see `COMPONENT.toml` (`next_milestone = "Hardware and runtime integration"`).

## Features

- **State machine**: explicit install states with `advance_step`, `start_installation`, `update_progress`, `complete_installation`, `cancel_installation`, `fail_installation`.
- **Config tracking**: per-installation `InstallConfig` with partitioning mode, target disk, filesystem, and progress.
- **Global instance**: `init_sigmainstaller` / `get_sigmainstaller` singleton for embedding in the desktop or live environment.
- **Safe Rust**: `#![forbid(unsafe_code)]`, `missing_docs` warnings enabled.

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

## Category

Utilities

## Engine

installer

## Language

Rust

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-installer)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
