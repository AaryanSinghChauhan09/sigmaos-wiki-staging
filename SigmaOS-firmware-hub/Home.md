# SigmaOS-firmware-hub

> firmware-hub

## Status

- **Component**: firmware-hub
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-firmware-hub

## Overview

SigmaOS component: **firmware-hub** — firmware blob catalog. Every binary firmware artifact (NIC, GPU, Wi-Fi, DSP firmware; initramfs hooks/modules) is registered with provenance (vendor, version, license, source URL) and a SHA-256 digest verified before staging into an initramfs or /lib/firmware. Registry + verification layer only; loading stays in kernel/drivers.

- `src/lib.rs` — library implementation
- `src/main.rs` — CLI entry point
- `docs/` — architecture, principles, testing, security docs

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
