# SigmaOS-sdl2

SDL2 hardware-accelerated windowing and input layer for SigmaOS

## Overview
- **Category**: `platform`
- **Repository**: [AaryanSinghChauhan09/SigmaOS-sdl2](https://github.com/AaryanSinghChauhan09/SigmaOS-sdl2)
- **License**: GPL-3.0-or-later
- **Release Model**: Rolling release (`0.1.0`, no release tags)

## Architecture & Principles
- `#![forbid(unsafe_code)]` enforced
- Structured error handling via `thiserror`
- Deterministic Arrange-Act-Assert unit tests
- Environment-variable configuration only (no hardcoded credentials)
