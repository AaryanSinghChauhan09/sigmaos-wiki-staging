# SigmaOS-app-sandbox

> **Category:** Security | **Language:** Rust | **License:** GPL-3.0-or-later

Unified application sandbox profile compiler for SigmaOS (`#![forbid(unsafe_code)]`). Combines fine-grained capabilities (`ReadHome`, `WriteDownloads`, `WaylandGui`, `AudioOut`, `NetworkClient`, `Camera`), read-only/read-write path lists, and default-deny network isolation.

## Key Types

| Type | Description |
|------|-------------|
| `SandboxCap` | `ReadHome`, `WriteDownloads`, `WaylandGui`, `AudioOut`, `NetworkClient`, `Camera` |
| `SandboxProfile` | App ID, capability set, RO/RW filesystem paths, `net_deny_by_default` |

## Tests (6 AAA)
- `test_strict_profile_is_network_isolated_aaa`
- `test_network_cap_disables_network_isolation_aaa`
- `test_filesystem_ro_and_rw_paths_aaa`
- `test_wayland_and_audio_caps_aaa`
- `test_duplicate_cap_deduplicated_aaa`
- `test_app_id_stored_aaa`

## See Also
- [SigmaOS-pledge-caps](SigmaOS-pledge-caps)
- [SigmaOS-container-engine](SigmaOS-container-engine)
- [SigmaOS-wayland-portal](SigmaOS-wayland-portal)
