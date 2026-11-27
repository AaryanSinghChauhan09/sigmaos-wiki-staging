# SigmaOS-filesystem-manager

> **Category:** Storage | **Language:** Rust | **License:** GPL-3.0-or-later

Filesystem mount and overlay management for SigmaOS (`#![forbid(unsafe_code)]`). Manages Btrfs, Ext4, Tmpfs, Overlay, EROFS, and Squashfs mount entries with mount options and state tracking.

## Key Types

| Type | Description |
|------|-------------|
| `FsType` | `Btrfs`, `Ext4`, `Tmpfs`, `Overlay`, `Erofs`, `Squashfs` |
| `MountEntry` | Device, target mountpoint, filesystem type, options, mounted state |
| `FilesystemManager` | Mount registry, mount/umount state transitions, mounted count |

## Tests (6 AAA)
- `test_add_and_mount_btrfs_aaa`
- `test_umount_decreases_count_aaa`
- `test_mount_unknown_target_returns_false_aaa`
- `test_count_mounted_multiple_aaa`
- `test_overlay_fstype_aaa`
- `test_options_attached_aaa`

## See Also
- [SigmaOS-atomic-root](SigmaOS-atomic-root)
- [SigmaOS-zfs-integration](SigmaOS-zfs-integration)
- [SigmaOS-recovery-system](SigmaOS-recovery-system)
