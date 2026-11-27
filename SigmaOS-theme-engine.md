# SigmaOS-theme-engine

> **Category:** Desktop | **Language:** Rust | **License:** GPL-3.0-or-later

Theme and color scheme management for SigmaOS desktop (`#![forbid(unsafe_code)]`). Supports `Light`, `Dark`, and `Auto` modes, semantic color palettes, and custom design tokens.

## Key Types

| Type | Description |
|------|-------------|
| `ThemeMode` | `Light`, `Dark`, `Auto` |
| `ColorScheme` | Name, mode, accent/bg/fg colors, custom token map |
| `ThemeEngine` | Scheme registry and active theme switching |

## Tests (6 AAA)
- `test_register_and_apply_theme_aaa`
- `test_apply_unknown_theme_returns_false_aaa`
- `test_theme_token_set_and_get_aaa`
- `test_theme_count_aaa`
- `test_auto_mode_aaa`
- `test_no_active_theme_returns_none_aaa`

## See Also
- [SigmaOS-font-manager](SigmaOS-font-manager)
- [SigmaOS-display-manager](SigmaOS-display-manager)
- [SigmaOS-themes-intros](SigmaOS-themes-intros)
