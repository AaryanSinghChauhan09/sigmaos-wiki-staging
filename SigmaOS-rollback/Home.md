# SigmaOS Rollback

System rollback utility for SigmaOS: BTRFS snapshot management, pre-update snapshots, restore on failure.

## Overview

SigmaOS Rollback provides automatic BTRFS snapshot management for safe system updates and recovery. It creates snapshots before and after pacman transactions, allowing easy rollback if something goes wrong.

## Features

- **Automatic snapshots**: Pre- and post-transaction snapshots via pacman hooks
- **Easy rollback**: Simple command to restore previous system state
- **BTRFS integration**: Native BTRFS subvolume and snapshot support
- **Space-efficient**: Uses BTRFS snapshot deduplication
- **Safety first**: Dry-run mode and confirmation prompts

## Usage

List available snapshots:
```bash
sigmaos-snapshot list
```

Rollback to a previous snapshot:
```bash
sigmaos-snapshot rollback <snapshot-name>
```

Create a manual snapshot:
```bash
sigmaos-snapshot create <name>
```

Delete a snapshot:
```bash
sigmaos-snapshot delete <snapshot-name>
```

## Integration

SigmaOS Rollback integrates with pacman through hooks:
- `pre_transaction`: Creates snapshot before package changes
- `post_transaction`: Creates snapshot after successful changes

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-rollback)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
