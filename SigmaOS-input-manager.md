# SigmaOS-input-manager

> **Category:** Desktop | **Language:** Rust | **License:** GPL-3.0-or-later

Keyboard, mouse, touchpad, and stylus input configuration for SigmaOS (`#![forbid(unsafe_code)]`). Provides declarative per-device property management (keyboard layouts/variants, natural scrolling, tap-to-click, mouse DPI).

## Key Types

| Type | Description |
|------|-------------|
| `InputDevice` | `Keyboard`, `Mouse`, `Touchpad`, `Stylus` |
| `InputConfig` | Per-device key-value property map |
| `InputManager` | Device config registry, lookup, and batch apply summary |

## Tests (6 AAA)
- `test_register_keyboard_config_aaa`
- `test_find_touchpad_config_aaa`
- `test_find_missing_device_returns_none_aaa`
- `test_apply_all_returns_per_device_summary_aaa`
- `test_mouse_dpi_setting_aaa`
- `test_multiple_keyboards_registered_aaa`

## See Also
- [SigmaOS-display-manager](SigmaOS-display-manager)
- [SigmaOS-wayland-portal](SigmaOS-wayland-portal)
- [SigmaOS-locale-manager](SigmaOS-locale-manager)
