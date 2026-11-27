# SigmaOS-crossover

CrossOver application compatibility bottle manager for SigmaOS

## Overview
- **Category**: `app-environment`
- **Repository**: [AaryanSinghChauhan09/SigmaOS-crossover](https://github.com/AaryanSinghChauhan09/SigmaOS-crossover)
- **License**: GPL-3.0-or-later
- **Release Model**: Rolling release (`0.1.0`, no release tags)

## Architecture & Principles
- `#![forbid(unsafe_code)]` enforced
- Structured error handling via `thiserror`
- Deterministic Arrange-Act-Assert unit tests
- Environment-variable configuration only (no hardcoded credentials)
