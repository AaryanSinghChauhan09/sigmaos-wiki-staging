# SigmaOS-boot-verify

> **Category:** Security | **Language:** Rust | **License:** GPL-3.0-or-later

Measured boot TPM2 PCR policy and signed kernel/initramfs verification for SigmaOS (`#![forbid(unsafe_code)]`). Evaluates observed PCR digests against expected policy measurements and rejects missing or tampered boot stages.

## Key Types

| Type | Description |
|------|-------------|
| `BootVerdict` | `Trusted` or `Untrusted(String)` |
| `BootMeasurement` | PCR index, SHA-256 digest, component name |
| `BootPolicy` | Expected PCR map and deterministic `verify()` evaluator |

## Tests (6 AAA)
- `test_matching_pcrs_trusted_aaa`
- `test_tampered_pcr_untrusted_aaa`
- `test_missing_pcr_untrusted_aaa`
- `test_empty_policy_always_trusted_aaa`
- `test_pcr_count_aaa`
- `test_extra_untracked_pcrs_ignored_aaa`

## See Also
- [SigmaOS-efi-boot](SigmaOS-efi-boot)
- [SigmaOS-sigma-bootloader](SigmaOS-sigma-bootloader)
- [SigmaOS-atomic-root](SigmaOS-atomic-root)
