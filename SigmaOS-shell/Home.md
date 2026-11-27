# SigmaOS-shell

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS-shell — Desktop shell process: Wayland panel, app launcher widget, and notification center. Inspired by Quickshell / Waybar / Hyprpanel. Design principles: single responsibility, fail-fast, no unsafe code, deterministic unit-testable logic, policy in configuration. The SigmaOS desktop shell — a Quickshell/QML layer providing the bar, dock, launcher, and notification center for the Hyprland session.

## Architecture
- **Language / Runtime:** `rust+qml` (Tier: `3`, Stability: `beta`)
- **Modules (`src/lib.rs`):** `sigmaquickshell`
- **Key Structs:** `AppEntry`, `AppLauncher`
- **Key Enums:** `ShellError`, `ShellComponent`
- **Public Functions:** `new`, `with_category`, `with_icon`, `new`, `register`, `search`
- **Provides:** `desktop-shell-process`, `wayland-panel`, `app-launcher-widget`, `notification-center`, `qml-shell`
- **Component Dependencies:** `sigmaos-shell-config`, `sigmaos-quickshell`, `sigmaos-notification-center`, `sigmaos-live-media`

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
- `component.name` = `SigmaOS-shell`
- `component.tier` = `3`
- `component.stability` = `beta`
- `component.language` = `rust+qml`
- `component.license` = `GPL-3.0-or-later`
- **Config directory:** `config/` contains runtime configuration templates.

## Dependencies
Standard SigmaOS runtime environment (no external Rust crate dependencies).

## Testing
Run the test suite and linter:

```sh
# QML syntax check (requires qmllint)
qmllint qml/

# Runtime: quickshell -p qml/
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
