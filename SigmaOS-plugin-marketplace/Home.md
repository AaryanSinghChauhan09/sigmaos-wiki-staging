# SigmaOS Plugin Marketplace

Component definition and contract specification for the SigmaOS plugin marketplace (applet/desklet/extension marketplace).

## Overview

This repository defines the marketplace contracts between SigmaOS components. It provides the component manifest and metadata for plugin marketplace integration.

## Component Details

- **Category:** Desktop/UI
- **Engine:** theme_marketplace
- **Language:** Rust
- **License:** GPL-3.0-or-later

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

## Architecture

The SigmaOS plugin marketplace ecosystem consists of:

- **SigmaOS-plugin-marketplace** (this repository): Component definition and contract specification
- **SigmaOS-plugin-registry**: Rails control plane for plugin registry (plugins.sigmaos.org)
- **SigmaOS-plugin-marketplace-tools**: Consolidated repository containing:
  - `site/`: Static marketplace frontend
  - `worker/`: Cloudflare Worker engagement backend
  - `registry.json`: Curated registry data
  - `scripts/`: Build scripts, security baseline scanning, verification

## Related Repositories

- [SigmaOS-plugin-registry](https://github.com/AaryanSinghChauhan09/SigmaOS-plugin-registry)
- [SigmaOS-plugin-marketplace-tools](https://github.com/AaryanSinghChauhan09/SigmaOS-plugin-marketplace-tools)

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-plugin-marketplace)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
