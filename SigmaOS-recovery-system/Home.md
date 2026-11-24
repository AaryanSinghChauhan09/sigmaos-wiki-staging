# SigmaOS Recovery System

System recovery and rollback system for SigmaOS - BTRFS snapshots and recovery tools.

## Overview

SigmaOS Recovery System provides automatic BTRFS snapshots, system rollback, and recovery tools. Ensures system reliability and quick recovery from failures.

## Features

- **BTRFS snapshots**: Automatic snapshots before updates
- **Rollback**: Rollback to previous snapshots
- **Boot recovery**: Recovery from boot failures
- **File recovery**: Recover deleted files
- **System repair**: Automated system repair
- **Backup integration**: Integration with backup tools
- **Snapshot management**: Manage and clean up snapshots
- **Emergency mode**: Emergency recovery mode

## Commands

```bash
# Create snapshot
sudo sigmaos-recovery snapshot create

# List snapshots
sudo sigmaos-recovery snapshot list

# Rollback to snapshot
sudo sigmaos-recovery rollback <snapshot-id>

# Restore files
sudo sigmaos-recovery restore <path>

# System repair
sudo sigmaos-recovery repair
```

## Configuration

Edit `/etc/sigmaos/recovery.conf` for configuration:

```ini
[recovery]
automatic_snapshots = true
snapshot_frequency = daily
keep_snapshots = 7
rollback_enabled = true
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-recovery-system)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
