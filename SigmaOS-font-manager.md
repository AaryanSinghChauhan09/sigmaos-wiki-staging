# SigmaOS-font-manager

> **Category:** Desktop | **Language:** Rust | **License:** GPL-3.0-or-later

Font discovery, loading, and fallback configuration for SigmaOS (`#![forbid(unsafe_code)]`). Supports weight selection, monospace classification, and ordered fallback chains.

## Key Types

| Type | Description |
|------|-------------|
| `FontWeight` | `Thin`, `Light`, `Regular`, `Medium`, `Bold`, `ExtraBold` |
| `Font` | Family name, weight, filesystem path, monospace flag |
| `FontManager` | Family registry, primary lookup, fallback chain resolution |

## Tests (6 AAA)
- `test_register_and_resolve_font_aaa`
- `test_resolve_missing_family_returns_none_aaa`
- `test_fallback_chain_resolves_aaa`
- `test_family_count_aaa`
- `test_monospace_flag_aaa`
- `test_multiple_weights_in_family_aaa`

## See Also
- [SigmaOS-theme-engine](SigmaOS-theme-engine)
- [SigmaOS-display-manager](SigmaOS-display-manager)
- [SigmaOS-locale-manager](SigmaOS-locale-manager)
