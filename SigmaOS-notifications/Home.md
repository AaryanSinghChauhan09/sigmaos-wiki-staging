# SigmaOS-notifications

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS Notifications - unified notification daemon core. In-process notification manager inspired by mako/dunst: apps post notifications, the daemon tracks active ones, keeps a bounded history, expires stale entries on `tick`, and notifies registered observers so a shell widget can render them. Unified notification daemon for SigmaOS with libnotify compatibility.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Key Structs:** `Notification`, `NotificationDaemon`
- **Key Enums:** `Priority`
- **Traits:** `Observer`
- **Public Functions:** `new`, `notify`, `dismiss`
- **Provides:** `notifications`, `notification-daemon`, `urgency-levels`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-notifications`
- `component.language` = `rust`

## Dependencies
Standard SigmaOS runtime environment (no external Rust crate dependencies).

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
