# SigmaOS-pkg-mirror

> **Category:** Packaging | **Language:** Rust | **License:** GPL-3.0-or-later

Sigma-native package mirror sync daemon. Provides tiered mirror management (Primary → Secondary → Edge) with staged promotion workflow — syncs upstream package repositories into local staging, validates, then promotes to live. Replaces all legacy `omarchy-mirror-*` and `arch-mirror-*` tooling with a fully SigmaOS-native Rust implementation.

## Architecture

```
Upstream Repo ──► MirrorSyncer.sync_all() ──► Local Stage ──► promote() ──► Live Mirror
                        │
                   MirrorRepo {
                     url, path, tier, enabled
                   }
```

## Key Types

| Type | Description |
|------|-------------|
| `MirrorTier` | `Primary` / `Secondary` / `Edge` — sync priority |
| `MirrorRepo` | A single mirror endpoint with URL, local path, tier and enabled flag |
| `MirrorSyncer` | Orchestrates multi-repo sync; tracks synced URLs with history |

## Shell Scripts (bin/)

The `bin/sigma-mirror-*` scripts wrap the daemon for cron/CI use:

| Script | Purpose |
|--------|---------|
| `sigma-mirror-sync` | Full upstream → stage sync |
| `sigma-mirror-stage` | Stage only (no upstream fetch) |
| `sigma-mirror-promote-arm` | Promote ARM staging to live |
| `sigma-mirror-upload` | Upload staged packages to R2 |

## Tests (6 AAA)
- `test_register_and_sync_enabled_repo_aaa`
- `test_disabled_repo_not_synced_aaa`
- `test_synced_count_accumulates_aaa`
- `test_promote_enabled_repo_aaa`
- `test_promote_unknown_url_returns_false_aaa`
- `test_mirror_tier_primary_eq_aaa`

## See Also
- [SigmaOS-pkg-core](SigmaOS-pkg-core)
- [SigmaOS-build-system](SigmaOS-build-system)
- [SigmaOS-mirror](SigmaOS-mirror)
