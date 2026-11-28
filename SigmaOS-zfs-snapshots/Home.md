# SigmaOS-zfs-snapshots

> zfs-snapshots

## Status

- **Component**: zfs-snapshots
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-zfs-snapshots

## Overview

SigmaOS component: **zfs-snapshots** — ZFS-style dataset snapshots. Datasets hold named snapshots; policies schedule creation (hourly/daily/weekly) and retention (keep N newest). Snapshots are immutable point-in-time records; rollback clones dataset state from a snapshot. Policy/bookkeeping layer — CoW block ops are delegated to sigmaos-zfs-integration.

- `src/lib.rs` — library implementation
- `src/main.rs` — CLI entry point
- `docs/` — architecture, principles, testing, security docs

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
