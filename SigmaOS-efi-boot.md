# SigmaOS-efi-boot

**Category:** Boot  
**License:** GPL-3.0-or-later  
**Rolling release:** Yes

Unified EFI boot entry manager with generation-aware ordering. Maintains `BootEntry` records (label + EFI path + cmdline). Exactly one entry is active. Integrates with SigmaOS rollback generation management.

## API

- `add_entry(BootEntry)` — add entry (labels must be unique; first is auto-activated)
- `remove_entry(label)` — remove non-active entry
- `set_active(label)` — switch active boot entry
- `active_entry()` — get the currently active entry

## Tests: 6 AAA

## See Also
- [SigmaOS-atomic-root](SigmaOS-atomic-root)
- [SigmaOS-rollback](SigmaOS-rollback)
- [SigmaOS-initramfs](SigmaOS-initramfs)
