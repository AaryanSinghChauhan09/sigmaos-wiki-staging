# SigmaOS-ab-boot

**Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

A/B bootloader slot manager for SigmaOS — ChromeOS/Android-style dual-slot booting with try-boot verification and automatic rollback, part of the immutable-root update track.

## Features

- **Two slots** (`a`/`b`) each holding a staged boot-image hash
- **Try-boot state machine** — `unbooted -> try_boot -> good | bad`
- **Try budget** — `max_tries` decremented per `mark_bad`; exhaustion marks the slot bad
- **Automatic rollback** — a bad active slot falls back to the peer when it is `good`
- **Atomic persistence** — single JSON doc, tmp+rename writes
- **`sigma-ab` CLI** — status/stage/mark-good/mark-bad/boot-slot/set-tries

## API

| Item | Description |
|---|---|
| `AbBoot::stage/mark_good/mark_bad/boot_slot` | slot lifecycle |
| `SlotState` | Unbooted / TryBoot / Good / Bad |
| `BootDecision` | RetrySame / RolledBack(slot) / NoFallback |

## Tests

8 AAA unit tests: staging, good-confirm + peer reset, rollback, try-budget retries, slot validation, boot-slot selection, save/load round-trip.

## See Also

- [SigmaOS-atomic-root](SigmaOS-atomic-root) — atomic root updates
- [SigmaOS-efi-boot](SigmaOS-efi-boot) — EFI boot integration
- [SigmaOS-generations](SigmaOS-generations) — system generations
- [SigmaOS-rollback](SigmaOS-rollback) — transactional rollback
