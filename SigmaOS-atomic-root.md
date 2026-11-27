# SigmaOS-atomic-root

**Category:** Boot  
**License:** GPL-3.0-or-later  
**Rolling release:** Yes

Immutable root filesystem management with A/B boot slots. The inactive slot is updated atomically; the active pointer is flipped in a single rename. On failure, the system boots from the previous slot automatically.

## Slots

| Slot | Description |
|------|-------------|
| A | First root filesystem slot |
| B | Second root filesystem slot |

Active slot is tracked in `SlotManager`. `atomic_switch_root()` flips it safely.

## Tests: 6 AAA

## See Also
- [SigmaOS-rollback](SigmaOS-rollback)
- [SigmaOS-efi-boot](SigmaOS-efi-boot)
- [SigmaOS-initramfs](SigmaOS-initramfs)
