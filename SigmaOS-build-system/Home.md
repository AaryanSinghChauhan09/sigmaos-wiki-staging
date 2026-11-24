# SigmaOS Build System

Reproducible build system for SigmaOS - containerized, deterministic builds.

## Overview

SigmaOS Build System provides a reproducible build pipeline for creating SigmaOS ISO images and packages. Uses containerization and deterministic build practices to ensure consistent, verifiable artifacts.

## Features

- **Reproducible builds**: Bit-for-bit identical outputs
- **Containerized**: Builds run in containers for isolation
- **Multi-architecture**: Support for x86_64, aarch64, and more
- **Parallel builds**: Parallel compilation for speed
- **Caching**: Build cache for faster rebuilds
- **Verification**: Automatic verification of build artifacts
- **Signing**: Package signing for security
- **Rolling release**: Continuous integration for packages

## Build Process

```bash
# Build ISO image
sudo sigmaos-build iso

# Build specific package
sudo sigmaos-build package firefox

# Build all packages
sudo sigmaos-build all

# Verify build artifacts
sudo sigmaos-build verify
```

## Architecture

The build system uses:
- **Docker**: Containerized builds
- **mkarchiso**: Arch Linux ISO creation
- **pacman**: Package management
- **make**: Build orchestration
- **CI/CD**: Automated builds on GitHub

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-build-system)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
