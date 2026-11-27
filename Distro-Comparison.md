# SigmaOS vs Arch, Omarchy, Debian, and Linux Mint

SigmaOS combines the rolling freshness of Arch, the curated Wayland desktop polish of Omarchy, the stability guarantees of Debian, and the out-of-the-box usability of Linux Mint — while eliminating their single-distro failure modes through **modular Rust-first architecture** (`#![forbid(unsafe_code)]`), **atomic A/B + generation rollback**, and **BSD-inspired security isolation**.

## Feature Matrix

| Capability | SigmaOS | Arch Linux | Omarchy | Debian | Linux Mint |
|---|---|---|---|---|---|
| **Architecture** | **326+ modular component repos** | Monolithic PKGBUILD tree | Dotfiles/script overlay on Arch | Monolithic `.deb` archive | Ubuntu/Debian derivative |
| **Memory Safety** | **`#![forbid(unsafe_code)]` Rust core** | C / Bash scripts | Bash / C / QML | C / Shell | C / Python |
| **Atomic Rollback** | **Built-in (`SigmaOS-rollback`, `SigmaOS-generations`, `SigmaOS-atomic-root`, `SigmaOS-zfs-integration`)** | Manual snapshots only | Manual snapshots | None by default | Timeshift (external) |
| **Declarative Config** | **Built-in (`SigmaOS-sys-declare`, `SigmaOS-config-system`)** | Imperative | Imperative | Imperative | Imperative |
| **Privilege Reduction** | **Built-in (`SigmaOS-pledge-caps`, `SigmaOS-jails`, `SigmaOS-wayland-portal`)** | Optional / manual | Optional | AppArmor (partial) | AppArmor (partial) |
| **Default-Deny Firewall** | **Built-in (`SigmaOS-pf-firewall`)** | Disabled by default | Disabled by default | Disabled by default | UFW (opt-in) |
| **Tamper-Evident Audit** | **SHA-256 chained `SigmaOS-audit-log`** | journald | journald | auditd (opt-in) | journald |
| **Release Model** | **Rolling with atomic recovery** | Rolling (manual fix on breakage) | Rolling on Arch | Point release (2-yr freeze) | Point release (LTS base) |
| **Desktop & Suites** | **Hyprland/Deskland + BetterOffice, GenOffice, Craft, BI, BigData, ML/DL** | DIY | Hyprland + curated apps | DE choices, older packages | Cinnamon/MATE/XFCE |

## Key Architectural Advantages

1. **Zero-Unsafe Core**: Core system, package, boot, firewall, and isolation crates enforce `#![forbid(unsafe_code)]` with deterministic AAA unit tests.
2. **True Atomic Recovery**: Updates target the inactive A/B root (`SigmaOS-atomic-root`) and record a new generation (`SigmaOS-generations`) with ZFS snapshot integration (`SigmaOS-zfs-integration`) and EFI boot selection (`SigmaOS-efi-boot`).
3. **Secure by Default**: Processes drop privileges via `SigmaOS-pledge-caps`, run isolated in `SigmaOS-jails`, mediate desktop access via `SigmaOS-wayland-portal`, and traverse a default-deny `SigmaOS-pf-firewall`.
4. **Full Native Identity**: Independent SigmaOS tooling (`sigma-pkg`, `sigma-build`, `sigma-initramfs`, `sigma-gen`, `sigma-pf`) rather than wrapping foreign distro package managers.

## See Also

- [Home](./Home)
- [Architecture](./Architecture)
- [SigmaOS-rollback](./SigmaOS-rollback)
- [SigmaOS-jails](./SigmaOS-jails)
- [SigmaOS-pf-firewall](./SigmaOS-pf-firewall)
