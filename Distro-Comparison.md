# SigmaOS vs Arch, Omarchy, Debian, and Linux Mint

SigmaOS combines the rolling freshness of Arch, the curated Wayland desktop polish of Omarchy, the stability guarantees of Debian, and the out-of-the-box usability of Linux Mint — while eliminating their single-distro failure modes through **modular Rust-first architecture** (`#![forbid(unsafe_code)]`), **atomic A/B + generation rollback**, and **BSD-inspired security isolation**.

## Feature Matrix

| Capability | SigmaOS | Arch Linux | Omarchy | Debian | Linux Mint |
|---|---|---|---|---|---|
| **Architecture** | **336+ modular component repos** | Monolithic PKGBUILD tree | Dotfiles/script overlay on Arch | Monolithic `.deb` archive | Ubuntu/Debian derivative |
| **Memory Safety** | **`#![forbid(unsafe_code)]` Rust core** | C / Bash scripts | Bash / C / QML | C / Shell | C / Python |
| **Atomic Rollback** | **Built-in (`SigmaOS-rollback`, `SigmaOS-generations`, `SigmaOS-atomic-root`, `SigmaOS-zfs-integration`)** | Manual snapshots only | Manual snapshots | None by default | Timeshift (external) |
| **Declarative Config** | **Built-in (`SigmaOS-sys-declare`, `SigmaOS-config-system`)** | Imperative | Imperative | Imperative | Imperative |
| **Privilege Reduction** | **Built-in (`SigmaOS-pledge-caps`, `SigmaOS-jails`, `SigmaOS-wayland-portal`)** | Optional / manual | Optional | AppArmor (partial) | AppArmor (partial) |
| **Default-Deny Firewall** | **Built-in (`SigmaOS-pf-firewall`)** | Disabled by default | Disabled by default | Disabled by default | UFW (opt-in) |
| **Tamper-Evident Audit** | **SHA-256 chained `SigmaOS-audit-log`** | journald | journald | auditd (opt-in) | journald |
| **Container Isolation** | **Built-in rootless OCI (`SigmaOS-container-engine`)** | Podman/Docker (manual) | None | LXC (optional) | None |
| **Hardware Detection** | **Auto driver scoring (`SigmaOS-hw-detect`)** | Manual/mkinitcpio | None | udev rules | Hardware Manager |
| **Display Management** | **Declarative Wayland config (`SigmaOS-display-manager`)** | wlr-randr (manual) | Hyprland config file | Xrandr/Wayland | Display Settings GUI |
| **Power Management** | **Profile-based (`SigmaOS-power-manager`)** | TLP (manual) | None | No default | Power Manager |
| **DNS Resolver** | **Declarative DoT split-horizon (`SigmaOS-dns-resolver`)** | systemd-resolved | systemd-resolved | resolvconf | NetworkManager |
| **Time Sync** | **NTP/PTP with ring-buffer tracking (`SigmaOS-time-sync`)** | systemd-timesyncd | systemd-timesyncd | ntpd/timesyncd | systemd-timesyncd |
| **Mirror Sync** | **Sigma-native tiered sync daemon (`SigmaOS-pkg-mirror`)** | reflector (manual) | Arch mirrors | apt-mirror | apt-mirror |
| **Release Model** | **Rolling with atomic recovery** | Rolling (manual fix on breakage) | Rolling on Arch | Point release (2-yr freeze) | Point release (LTS base) |
| **Desktop & Suites** | **Hyprland/Deskland + BetterOffice, GenOffice, Craft, BI, BigData, ML/DL** | DIY | Hyprland + curated apps | DE choices, older packages | Cinnamon/MATE/XFCE |

## Key Architectural Advantages

1. **Zero-Unsafe Core**: Core system, package, boot, firewall, and isolation crates enforce `#![forbid(unsafe_code)]` with deterministic AAA unit tests.
2. **True Atomic Recovery**: Updates target the inactive A/B root (`SigmaOS-atomic-root`) and record a new generation (`SigmaOS-generations`) with ZFS snapshot integration (`SigmaOS-zfs-integration`) and EFI boot selection (`SigmaOS-efi-boot`).
3. **Secure by Default**: Processes drop privileges via `SigmaOS-pledge-caps`, run isolated in `SigmaOS-jails`, mediate desktop access via `SigmaOS-wayland-portal`, and traverse a default-deny `SigmaOS-pf-firewall`. Every audit event is SHA-256 chained via `SigmaOS-audit-log`.
4. **Full Native Identity**: Independent SigmaOS tooling (`sigma-pkg`, `sigma-build`, `sigma-initramfs`, `sigma-gen`, `sigma-pf`, `sigma-mirror-*`) — no wrapped foreign distro package managers.
5. **Complete Subsystem Coverage**: 336+ dedicated component repos covering power, display, input, filesystem, locale, containers, DNS, time, hardware, mirrors — each independently tested with 6+ AAA tests.

## Component Coverage by Domain

| Domain | SigmaOS Components | Arch | Debian |
|--------|-------------------|------|--------|
| **Security** | pledge-caps, jails, pf-firewall, audit-log, crypto-keys, wayland-portal, sec-audit, security-hardening | Optional | Partial |
| **Boot** | efi-boot, atomic-root, sigma-bootloader, initramfs | GRUB/systemd-boot | GRUB |
| **Packaging** | pkg-core, build-system, pkg-mirror, update-system, rollback, generations | pacman | apt/dpkg |
| **System** | process-manager, user-manager, network-manager, time-sync, locale-manager, power-manager | systemd | systemd |
| **Desktop** | display-manager, input-manager, wayland-portal, screensaver, notifications | DIY | GNOME/KDE |
| **Storage** | zfs-integration, filesystem-manager, atomic-root, recovery-system | Manual | LVM/mdadm |

## See Also

- [Home](./Home)
- [Architecture](./Architecture)
- [Security](./Security)
- [Rolling-Release](./Rolling-Release)
- [SigmaOS-rollback](./SigmaOS-rollback)
- [SigmaOS-jails](./SigmaOS-jails)
- [SigmaOS-pf-firewall](./SigmaOS-pf-firewall)
- [SigmaOS-container-engine](./SigmaOS-container-engine)


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
