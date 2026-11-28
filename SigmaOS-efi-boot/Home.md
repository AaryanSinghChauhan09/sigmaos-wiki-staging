# SigmaOS-efi-boot

> efi-boot

## Status

- **Component**: efi-boot
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-efi-boot

## Overview

**Unified EFI boot entry manager with generation-aware ordering.**

Maintains a list of `BootEntry` records (label + EFI path + cmdline).
Exactly one entry is active at boot. Integrates with SigmaOS rollback
generation management so older generations can be selected at boot time.

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
