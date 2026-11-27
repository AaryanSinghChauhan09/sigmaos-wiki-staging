# SigmaOS-service-supervisor

> **Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later

Lightweight dependency-aware service supervisor with restart backoff for SigmaOS (`#![forbid(unsafe_code)]`). Enforces dependency ordering (`after`), tracks restart counts against `max_retries`, and transitions crashed services between `Backoff` and `Failed` states.

## Key Types

| Type | Description |
|------|-------------|
| `ServiceState` | `Stopped`, `Starting`, `Running`, `Backoff`, `Failed` |
| `ServiceSpec` | Service name, `depends_on` list, `max_retries`, current state, restart count |
| `ServiceSupervisor` | Dependency-checked `start()`, crash accounting, active service queries |

## Tests (6 AAA)
- `test_start_service_without_deps_aaa`
- `test_start_blocked_until_dependency_running_aaa`
- `test_crash_enters_backoff_then_failed_aaa`
- `test_start_unknown_service_returns_false_aaa`
- `test_crash_unknown_service_returns_none_aaa`
- `test_running_services_tracks_multiple_aaa`

## See Also
- [SigmaOS-process-manager](SigmaOS-process-manager)
- [SigmaOS-boot-verify](SigmaOS-boot-verify)
- [SigmaOS-telemetry-local](SigmaOS-telemetry-local)
