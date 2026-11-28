# Architecture — Sigma

Extracted from the repository README.

## Architecture

SigmaOS is built on:

- **Base**: Linux packages
- **Kernel**: Linux
- **Init System**: systemd
- **Package Manager**: sigma-pkg
- **Bootloader**: GRUB (UEFI)
- **Library**: Rust (sigma-system crate)
- **Configuration**: /etc/sigmaos/
