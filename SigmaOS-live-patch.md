# SigmaOS-live-patch

> **Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later

Live kernel and userspace hotpatch metadata and signature verification tracker for SigmaOS (`#![forbid(unsafe_code)]`). Rejects unsigned patches, tracks CVE references, and supports clean revert of applied hotpatches without requiring a reboot.

## Key Types

| Type | Description |
|------|-------------|
| `PatchStatus` | `Staged`, `Applied`, `Reverted`, `Rejected` |
| `LivePatch` | Patch ID, target component, optional CVE, SHA-256 digest, signed flag, status |
| `LivePatchManager` | Stages, verifies, applies, and reverts live patches |

## Tests (6 AAA)
- `test_apply_signed_patch_succeeds_aaa`
- `test_unsigned_patch_rejected_aaa`
- `test_revert_applied_patch_aaa`
- `test_revert_staged_patch_returns_false_aaa`
- `test_apply_unknown_patch_err_aaa`
- `test_cve_attached_aaa`

## See Also
- [SigmaOS-sigma-kernel](SigmaOS-sigma-kernel)
- [SigmaOS-update-system](SigmaOS-update-system)
- [SigmaOS-crypto-keys](SigmaOS-crypto-keys)
