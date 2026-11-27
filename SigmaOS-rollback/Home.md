# SigmaOS-rollback

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS rollback component. Pacman-style transaction journal: callers record the changes a transaction made, and `rollback_last` yields the inverse steps so the most recent transaction can be undone. SigmaOS System rollback: BTRFS snapshot management, pre-update snapshots, restore on failure.

## Architecture
- **Language / Runtime:** `rust` (Tier: `2`, Stability: `scaffold`)
- **Key Structs:** `Step`, `InverseStep`, `Transaction`, `RollbackManager`
- **Key Enums:** `ComponentError`, `Action`
- **Public Functions:** `new`, `record`
- **Provides:** `component`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-rollback`
- `component.tier` = `2`
- `component.stability` = `scaffold`
- `component.language` = `rust`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `thiserror` (`1`)

## Testing
Run the test suite and linter:

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
