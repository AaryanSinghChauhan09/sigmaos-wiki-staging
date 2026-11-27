# SigmaOS-hw-detect

> **Category:** Hardware | **Language:** Rust | **License:** GPL-3.0-or-later

Hardware detection and driver recommendation for SigmaOS. Scans PCI/USB devices, matches against a vendor → driver database, and produces scored `DriverMatch` results. Falls back to `sigma-generic` for unknown devices. Integrates with the SigmaOS installer for automatic driver selection during first boot.

## Key Types

| Type | Description |
|------|-------------|
| `DeviceClass` | `Cpu`, `Gpu`, `Network`, `Storage`, `Audio`, `Usb`, `Unknown` |
| `HwDevice` | PCI ID, class, vendor, model |
| `DriverMatch` | device_id, driver name, confidence score (0–100) |
| `HwDetector` | Registry of devices + driver DB; `detect_all()` returns matches |

## Scoring

| Match type | Score |
|-----------|-------|
| Known vendor → matched driver | 90 |
| Unknown vendor → sigma-generic | 50 |

## Tests (6 AAA)
- `test_known_vendor_gets_matched_driver_aaa`
- `test_unknown_vendor_uses_generic_driver_aaa`
- `test_device_count_aaa`
- `test_no_devices_returns_empty_matches_aaa`
- `test_device_class_storage_aaa`
- `test_multiple_drivers_registered_aaa`

## See Also
- [SigmaOS-installer](SigmaOS-installer)
- [SigmaOS-efi-boot](SigmaOS-efi-boot)
- [SigmaOS-sigma-kernel](SigmaOS-sigma-kernel)
