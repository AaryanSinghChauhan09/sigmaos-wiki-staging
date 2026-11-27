# SigmaOS-display-manager

> **Category:** Desktop | **Language:** Rust | **License:** GPL-3.0-or-later

Display and monitor configuration manager for SigmaOS (`#![forbid(unsafe_code)]`). Manages multi-monitor outputs, resolution, refresh rates, DPI scaling, rotation, and primary display assignment for Wayland/Deskland sessions.

## Key Types

| Type | Description |
|------|-------------|
| `Rotation` | `Normal`, `Left`, `Right`, `Inverted` |
| `MonitorConfig` | Output ID, width/height, refresh rate, scale, rotation, enabled flag |
| `DisplayManager` | Multi-output registry, primary monitor selection, resolution lookup |

## Tests (6 AAA)
- `test_add_and_count_monitors_aaa`
- `test_set_primary_known_monitor_aaa`
- `test_set_primary_unknown_monitor_returns_false_aaa`
- `test_resolution_of_known_monitor_aaa`
- `test_resolution_of_unknown_returns_none_aaa`
- `test_rotation_default_is_normal_aaa`

## See Also
- [SigmaOS-wayland-portal](SigmaOS-wayland-portal)
- [SigmaOS-input-manager](SigmaOS-input-manager)
- [SigmaOS-theme-engine](SigmaOS-theme-engine)
