# SigmaOS-ab-boot

> ab-boot

## Status

- **Component**: ab-boot
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-ab-boot

## Overview

SigmaOS component: **ab-boot** — A/B boot slot management for safe
system updates. Two boot slots (`a`, `b`) hold staged boot images;
updates write to the inactive slot and the `active` pointer only
flips after the new slot survives its try-boot budget, giving
automatic rollback to the last-known-good slot on boot failure.

Model (Android `boot_control`-inspired state machine):

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
