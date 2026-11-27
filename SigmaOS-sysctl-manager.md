# SigmaOS-sysctl-manager

**Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Declarative sysctl tuning engine for SigmaOS. Replaces ad-hoc `/etc/sysctl.d/` scripts with a typed, atomic, verifiable parameter management layer.

## Features

- **Typed parameters** — `Int`, `Bool`, `Text` variants with canonical string serialization
- **Atomic batch apply** — all-or-nothing application via `apply_all()`
- **Live verification** — `verify(key, live_value)` checks kernel reality against declared intent
- **Rollback-safe** — integrates with `SigmaOS-rollback` for generation-aware sysctl snapshots

## API

| Function | Description |
|---|---|
| `declare(key, value)` | Register a sysctl parameter |
| `apply_all()` | Atomically apply all declared params |
| `verify(key, live)` | Verify live value matches declared value |
| `get_applied(key)` | Retrieve last applied value |

## Errors

| Error | Condition |
|---|---|
| `KeyNotFound(key)` | `verify()` called for undeclared key |
| `ValueMismatch { key, expected, actual }` | Live value differs from declared |
| `ApplyFailed(msg)` | Write to `/proc/sys/` failed |

## Tests

6 AAA unit tests covering: declaration count, bool serialization, int match, mismatch error, unknown key, text param round-trip.

## See Also

- [SigmaOS-sys-declare](SigmaOS-sys-declare) — declarative system configuration
- [SigmaOS-atomic-root](SigmaOS-atomic-root) — atomic A/B root switching
- [SigmaOS-rollback](SigmaOS-rollback) — generation rollback management
