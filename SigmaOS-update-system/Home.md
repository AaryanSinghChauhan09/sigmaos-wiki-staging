# SigmaOS Update System

Rolling-release update manager — checks an update server, downloads
signed packages, installs via pacman, and supports rollback.

## Capabilities

- `check` — query `updates.sigmaos.org` for the channel
  (`stable`/`beta`/`nightly`/custom), rate-limited by
  `check_interval` unless `--force`
- `update` — fetch, verify signature (TODO), install via
  `sudo pacman -U`, record version; `--dry-run` lists pending updates
- `rollback [--version V | --list]` — version history with
  backup-before-rollback
- `status [--detailed]` — current version, channel, last check,
  auto-update flag, and pending updates persisted from the last check
- `config --channel/--auto-update/--interval` — update settings in
  `~/.config/sigmaos/update.toml`
- Pending updates are stored in `update-state.json` so `status`
  reports what `check` last found without re-querying the server

## Commands

```bash
sigmaos-update check [--channel stable] [--force]
sigmaos-update update [--channel stable] [--dry-run] [--force]
sigmaos-update rollback [--version X.Y.Z | --list]
sigmaos-update status [--detailed]
sigmaos-update config [--channel C] [--auto-update BOOL] [--interval SECS]
```

## Structure

- `src/updater.rs` - UpdateManager: check/apply/rollback/state
- `src/channel.rs` - UpdateChannel enum (stable/beta/nightly/custom)
- `src/notifier.rs` - desktop notification hook
- `src/main.rs` - CLI entry point

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

2 unit tests (update-state JSON round-trip incl. legacy files without
`pending`).

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-update-system)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
