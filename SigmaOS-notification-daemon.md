# SigmaOS-notification-daemon

> **Category:** Desktop | **Language:** Rust | **License:** GPL-3.0-or-later

Desktop notification daemon for SigmaOS (`#![forbid(unsafe_code)]`), implementing bounded ring-buffer queuing, urgency levels (`Low`, `Normal`, `Critical`), timeout handling, and notification dismissal.

## Key Types

| Type | Description |
|------|-------------|
| `Urgency` | `Low`, `Normal`, `Critical` |
| `Notification` | App name, summary, body, urgency, timeout (ms) |
| `NotificationDaemon` | Bounded queue with auto-incrementing IDs and critical count |

## Tests (6 AAA)
- `test_push_notification_increments_id_aaa`
- `test_close_removes_notification_aaa`
- `test_close_unknown_returns_false_aaa`
- `test_capacity_evicts_oldest_aaa`
- `test_critical_urgency_count_aaa`
- `test_timeout_zero_means_never_expire_aaa`

## See Also
- [SigmaOS-notifications](SigmaOS-notifications)
- [SigmaOS-wayland-portal](SigmaOS-wayland-portal)
- [SigmaOS-session-manager](SigmaOS-session-manager)
