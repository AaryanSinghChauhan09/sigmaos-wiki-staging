# SigmaOS-sigma-sys

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS sigma-sys — userspace syscall shim. Safe wrappers over the kernel syscall ABI (see `sigma_kernel::syscall`). The raw `syscall` instruction is isolated in `arch` behind the `x86_64` feature; on host builds a pluggable `Syscall` impl is used so the API is fully testable. Userspace syscall shim standardizing memory, IPC, and I/O across SigmaOS components

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Modules (`src/lib.rs`):** `api`, `errno`, `arch`
- **Traits:** `Syscall`
- **Public Functions:** `register`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-sigma-sys`
- `component.license` = `GPL-3.0-or-later`
- **Feature flags:** `default`, `x86_64`

## Dependencies

**SigmaOS Component Dependencies:** `sigmaos-sigma-kernel`

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
