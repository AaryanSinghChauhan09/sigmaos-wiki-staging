# SigmaOS Rolling-Release Model

> Continuous delivery, atomic updates, and snapshot-backed recovery without static version tags.

## Philosophy
SigmaOS follows a **pure rolling-release model**:
- **No Release Tags:** Component repositories do not cut static `vX.Y.Z` release tags. Improvements land continuously on `main`.
- **Semantic Unreleased Versioning:** Rolling Rust crates declare `version = "0.1.0"` in `Cargo.toml` until stabilized interfaces require explicit contract bumps.
- **Continuous Verification:** Every commit is validated through automated formatting, Clippy lints, and Arrange-Act-Assert unit tests before integration.

## Update & Recovery Pipeline

| Component | Role in Rolling Release |
| :--- | :--- |
| **`SigmaOS-mirror`** / **`SigmaOS-pkg-mirror`** | Hosts and syncs `edge`, `rc`, and `stable` package repository snapshots. |
| **`SigmaOS-update-system`** | Orchestrates rolling system updates with pre-flight checks and transaction logging. |
| **`SigmaOS-atomic-root`** | Manages A/B root slots so updates write to the inactive slot without mutating the running OS. |
| **`SigmaOS-generations`** | Tracks immutable system generations with atomic activation and bounded retention. |
| **`SigmaOS-efi-boot`** | Generates and selects EFI boot entries for generation switching. |
| **`SigmaOS-boot-verify`** | Verifies kernel, initramfs, and rootfs SHA-256 measurements before boot handoff. |
| **`SigmaOS-service-supervisor`** | Supervises core daemons with dependency-ordered startup and health checks. |
| **`SigmaOS-live-patch`** | Applies hot kernel/userspace security patches without requiring a full reboot. |
| **`SigmaOS-rebuild`** | Rebuilds system images, initramfs plans, and declarative profiles deterministically. |
| **`SigmaOS-zfs-integration`** | Creates pre-update ZFS filesystem snapshots automatically. |
| **`SigmaOS-rollback`** | Restores the system to a known-good snapshot if an update fails. |
| **`SigmaOS-recovery-system`** | Provides boot-time and CLI recovery workflows for broken states. |

## Update Workflow
1. Pre-update snapshot is captured via `SigmaOS-zfs-integration`.
2. Package metadata and signatures are verified via `SigmaOS-signed` and `SigmaOS-openpgpkey`.
3. `SigmaOS-update-system` applies updates from the configured `SigmaOS-mirror` channel (`stable`, `rc`, or `edge`).
4. If verification or boot health checks fail, `SigmaOS-rollback` / `SigmaOS-recovery-system` reverts to the previous working state.
