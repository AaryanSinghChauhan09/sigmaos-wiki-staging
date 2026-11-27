# SigmaOS-snapshot-scheduler

**Category:** Storage | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Automated snapshot scheduling and retention policy engine for SigmaOS. Replaces ad-hoc cron/systemd-timer scripts with deterministic tier-based retention pruning (`Boot`, `Hourly`, `Daily`, `Weekly`) and snapshot pinning.

## Features

- **Tiered retention policy** — configurable `keep_boot`, `keep_hourly`, `keep_daily`, `keep_weekly` bounds
- **Pinned snapshots** — pinned snapshots are exempt from automated pruning and manual deletion
- **Oldest-first eviction** — `prune()` retains the newest snapshots per tier and returns pruned IDs

## API

| Function | Description |
|---|---|
| `record(snap)` | Register a new snapshot record |
| `pin(id, pinned)` | Pin or unpin a snapshot |
| `remove(id)` | Delete an unpinned snapshot |
| `prune()` | Prune unpinned snapshots exceeding per-tier limits |
| `count()` | Total tracked snapshots |

## Tests

6 AAA unit tests covering: oldest-first tier pruning, pinned preservation during prune, pinned removal rejection, duplicate ID rejection, unpin-then-remove, unknown ID error.

## See Also

- [SigmaOS-rollback](SigmaOS-rollback) — generation rollback management
- [SigmaOS-zfs-integration](SigmaOS-zfs-integration) — ZFS snapshot integration
- [SigmaOS-filesystem-manager](SigmaOS-filesystem-manager) — filesystem management
