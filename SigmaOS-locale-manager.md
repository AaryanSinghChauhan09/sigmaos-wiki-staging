# SigmaOS-locale-manager

> **Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later

Locale, timezone, and i18n configuration for SigmaOS (`#![forbid(unsafe_code)]`). Manages system locale, extra generated locales, and validated IANA/UTC timezone settings.

## Key Types

| Type | Description |
|------|-------------|
| `Locale` | Language code, encoding (e.g., `UTF-8`), optional territory |
| `LocaleManager` | System locale, timezone validation, extra locales registry |

## Tests (6 AAA)
- `test_set_and_get_system_locale_aaa`
- `test_set_and_get_timezone_aaa`
- `test_add_extra_locales_count_aaa`
- `test_locale_as_string_with_territory_aaa`
- `test_valid_timezone_check_aaa`
- `test_no_locale_set_returns_none_aaa`

## See Also
- [SigmaOS-time-sync](SigmaOS-time-sync)
- [SigmaOS-input-manager](SigmaOS-input-manager)
- [SigmaOS-sys-declare](SigmaOS-sys-declare)
