# SigmaOS-session-manager

> **Category:** Desktop | **Language:** Rust | **License:** GPL-3.0-or-later

Login session and multi-seat management for SigmaOS (`#![forbid(unsafe_code)]`). Tracks per-seat user sessions and lifecycle states (`Active`, `Idle`, `Locked`, `Closed`).

## Key Types

| Type | Description |
|------|-------------|
| `SessionState` | `Active`, `Idle`, `Locked`, `Closed` |
| `Session` | Session ID, user, seat, state, optional TTY |
| `SessionManager` | Multi-seat registry, lock/unlock/close transitions |

## Tests (6 AAA)
- `test_open_and_count_sessions_aaa`
- `test_lock_session_reduces_active_count_aaa`
- `test_close_session_aaa`
- `test_lock_unknown_session_returns_false_aaa`
- `test_session_state_transitions_aaa`
- `test_multi_seat_isolation_aaa`

## See Also
- [SigmaOS-user-manager](SigmaOS-user-manager)
- [SigmaOS-screensaver](SigmaOS-screensaver)
- [SigmaOS-power-manager](SigmaOS-power-manager)
