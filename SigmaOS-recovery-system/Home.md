# SigmaOS Recovery System

File-based system snapshots with selective restore — backs up system
config, user data, and package lists into per-snapshot directories
under the XDG data dir.

## Capabilities

- `RecoveryManager::create_snapshot` — writes `metadata.json`
  (id/name/description/timestamps/flags) plus payload backups:
  `backup_system_config` always, `backup_user_data` and
  `backup_package_list` when requested
- `list_snapshots` / `get_snapshot_info` — metadata-driven listing,
  newest first
- `restore_snapshot` — restores config/user-data/packages selectively
  per snapshot flags; takes an automatic `pre-restore` snapshot unless
  `force`
- `delete_snapshot` — `--force` removes, otherwise moves to trash
- `RestoreManager::verify_snapshot` — validates a snapshot dir
  (parseable `metadata.json`, id matches dir name, has payload files)
- `RestoreManager::restore` intentionally errors — destructive restore
  must go through `restore_snapshot` for the safety backup
- `get_status` — snapshot count, total size, last snapshot time

## Commands

```bash
sigmaos-recovery snapshot <name> [-d DESC] [-u] [-p]
sigmaos-recovery list [-v]
sigmaos-recovery restore <name|id> [--dry-run] [--force]
sigmaos-recovery delete <name|id> [--force]
sigmaos-recovery status [-v]
```

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

3 `RestoreManager` tests (valid snapshot, rejection cases, loud
restore failure).

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-recovery-system)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
