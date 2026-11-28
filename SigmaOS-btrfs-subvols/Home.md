# SigmaOS-btrfs-subvols

> btrfs-subvols

## Status

- **Component**: btrfs-subvols
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-btrfs-subvols

## Overview

SigmaOS component: **btrfs-subvols** — btrfs subvolume and snapshot manager. Metadata layer for the subvolume lifecycle: independently-mountable trees, writable/read-only snapshots, quotas, and send/receive pairing. Actual CoW extent operations are delegated to the filesystem driver.

- `src/lib.rs` — library implementation
- `src/main.rs` — CLI entry point
- `docs/` — architecture, principles, testing, security docs

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
