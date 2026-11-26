# SigmaOS ZFS Integration

ZFS dataset state tracker for SigmaOS — records datasets, snapshot
policy, and scrub schedule. Actual `zfs(8)` operations are delegated
by callers; this component owns the JSON-backed state.

## Overview

`SigmaOS-zfs-integration` maintains a `ZfsState`: a map of `Dataset`
records (name, kind, mountpoint, compression, snapshot enablement and
retention), an optional `ScrubSchedule` (cron expression + optional
dataset subset), and `last_scrub`. Dataset names must contain `/`
(pool-qualified). State saves atomically (temp + rename) under the
XDG data dir.

## Features

- **Dataset registry**: add/remove with name validation
- **Queries**: `snapshot_targets` (snapshots enabled), `by_pool`
  (pool-prefix filter)
- **Scrub validation**: `validate` rejects scrub schedules that name
  unknown datasets; an empty dataset list means "all" and always
  validates
- **Persistence**: `save`/`load` JSON roundtrip preserving
  `last_scrub`
- **Tests**: 4 unit tests cover validation, queries, scrub reference
  checking, and persistence

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-zfs-integration)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
