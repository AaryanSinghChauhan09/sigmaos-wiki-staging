# SigmaOS-generations

**Category:** System  
**License:** GPL-3.0-or-later  
**Rolling release:** Yes

Immutable system generation tracking with atomic activation and rollback. Each generation is a snapshot of the full system state. Switching to a new generation is atomic; previous generations are preserved up to `max_keep`.

## Commands

- `sigma-gen list` — list all generations
- `sigma-gen create <label> <hash>` — create a new generation
- `sigma-gen activate <number>` — switch to a generation
- `sigma-gen remove <number>` — remove a non-active generation

## Tests: 6 AAA

## See Also
- [SigmaOS-rollback](SigmaOS-rollback)
- [SigmaOS-atomic-root](SigmaOS-atomic-root)
- [SigmaOS-efi-boot](SigmaOS-efi-boot)
