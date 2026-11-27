# SigmaOS-power-manager

> **Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later

Power profile and sleep/hibernate management for SigmaOS (`#![forbid(unsafe_code)]`). Manages active power profiles (`Performance`, `Balanced`, `PowerSaver`, `Custom`), system sleep states (`Active`, `Idle`, `Suspended`, `Hibernated`), and governor/ACPI settings.

## Key Types

| Type | Description |
|------|-------------|
| `PowerProfile` | `Performance`, `Balanced`, `PowerSaver`, `Custom(String)` |
| `SleepState` | `Active`, `Idle`, `Suspended`, `Hibernated` |
| `PowerManager` | Profile switching, suspend/hibernate/wake transitions, key-value settings |

## Tests (6 AAA)
- `test_default_profile_is_balanced_aaa`
- `test_set_performance_profile_aaa`
- `test_suspend_and_wake_aaa`
- `test_hibernate_state_aaa`
- `test_custom_profile_roundtrip_aaa`
- `test_setting_store_and_retrieve_aaa`

## See Also
- [SigmaOS-hw-detect](SigmaOS-hw-detect)
- [SigmaOS-session-manager](SigmaOS-session-manager)
- [SigmaOS-process-manager](SigmaOS-process-manager)
