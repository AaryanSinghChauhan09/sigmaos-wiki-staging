# SigmaOS Installer

Graphical live installer for SigmaOS (partition, copy, bootloader installation).

## Overview

The SigmaOS installer provides a graphical interface for installing SigmaOS to disk. It handles disk partitioning, file system setup, system copy, and bootloader configuration in a user-friendly way.

## Features

- **Graphical interface**: Easy-to-use GUI for installation
- **Disk partitioning**: Automatic and manual partitioning options
- **File system support**: BTRFS with subvolumes for system and home
- **Bootloader**: Configures systemd-boot for UEFI or syslinux for BIOS
- **Safety checks**: Dry-run mode to preview changes before applying
- **Rollback support**: BTRFS snapshot integration for safe recovery

## Usage

The installer is available on the SigmaOS live ISO. Run it from the live session:

```bash
sigmaos-install
```

Dry-run mode (default):
```bash
sigmaos-install --dry-run
```

Destructive installation:
```bash
sigmaos-install --destructive
```

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
