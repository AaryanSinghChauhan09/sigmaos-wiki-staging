# SigmaOS-ms-excel

MS Excel workbook and formula engine bridge for SigmaOS

## Overview
- **Category**: `data-science`
- **Repository**: [AaryanSinghChauhan09/SigmaOS-ms-excel](https://github.com/AaryanSinghChauhan09/SigmaOS-ms-excel)
- **License**: GPL-3.0-or-later
- **Release Model**: Rolling release (`0.1.0`, no release tags)

## Architecture & Principles
- `#![forbid(unsafe_code)]` enforced
- Structured error handling via `thiserror`
- Deterministic Arrange-Act-Assert unit tests
- Environment-variable configuration only (no hardcoded credentials)
