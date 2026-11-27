# SigmaOS Architecture

> Layered, modular architecture from boot and kernel through userspace, desktop, and application suites.

## Architectural Layers

```
+-------------------------------------------------------------------+
|  User Applications & Suites                                       |
|  (Browser, BetterOffice, GenOffice, Craft, BI, BigData, ML/DL)    |
+-------------------------------------------------------------------+
|  Desktop & Shell Layer                                            |
|  (Deskland, Quickshell, Hyprland Titlebars, SDDM, Themes, UI)     |
+-------------------------------------------------------------------+
|  Core System Services & Package Management                        |
|  (pkg-core, build-system, update-system, recovery, rollback, zfs) |
+-------------------------------------------------------------------+
|  Security & Verification Layer                                    |
|  (security-hardening, sec-audit, signed, openpgpkey)              |
+-------------------------------------------------------------------+
|  Kernel, Boot & Hardware Abstraction                              |
|  (sigma-kernel, sigma-bootloader, initramfs, dkms, m1n1, mesa)    |
+-------------------------------------------------------------------+
```

## 1. Boot & Kernel Layer
- **`SigmaOS-sigma-kernel`**: Core OS kernel configuration, integration, and verification tooling.
- **`SigmaOS-sigma-bootloader`, `SigmaOS-efi-boot` & `SigmaOS-initramfs`**: Bootloader orchestration, unified EFI boot entry manager, and deterministic `newc` cpio initramfs builder with topological hook ordering.
- **`SigmaOS-atomic-root`**: Immutable A/B root filesystem slot management with atomic switch-root.
- **`SigmaOS-dkms` & `SigmaOS-mesa`**: Dynamic kernel module support and 3D/Vulkan graphics stack.
- **`SigmaOS-ISO`, `SigmaOS-installer`, `SigmaOS-live-media`**: Bootable live media builder and guided system installer.

## 2. Core System & Package Management
- **`SigmaOS-config-system`, `SigmaOS-sys-declare`, `SigmaOS-sysctl-manager` & `SigmaOS-system-profile`**: Declarative, schema-validated TOML/JSON/YAML system configuration and atomic sysctl tuning with diff-and-apply planning.
- **`SigmaOS-pkg-core`, `SigmaOS-build-system`, `SigmaOS-ports`, `SigmaOS-mirror`, `SigmaOS-pkg-mirror`**: Package lifecycle with conflict/cycle detection, reproducible builds (`sigma-build`), and rolling package mirrors.
- **`SigmaOS-update-system`, `SigmaOS-live-patch`, `SigmaOS-recovery-system`, `SigmaOS-rollback`, `SigmaOS-generations`, `SigmaOS-rebuild`, `SigmaOS-zfs-integration`**: Atomic updates, live patching, immutable generations, ZFS snapshots, and instant system rollback.
- **`SigmaOS-process-manager`, `SigmaOS-service-supervisor`, `SigmaOS-dbus-broker`, `SigmaOS-cgroup-manager`, `SigmaOS-sleep-inhibitor`**: Supervised process lifecycle, service supervision, D-Bus broker tracking, cgroup v2 resource limits, and power sleep inhibit leases.
- **`SigmaOS-network-manager`, `SigmaOS-dns-resolver`, `SigmaOS-user-manager`, `SigmaOS-sigma-sh` & `SigmaOS-sigma-sys`**: Declarative networking, DNS resolution, capability-aware user/group DB, and core system shell.

## 3. Security & Isolation Layer
- **`SigmaOS-jails`, `SigmaOS-pledge-caps`, `SigmaOS-app-sandbox`, `SigmaOS-mount-namespace`, `SigmaOS-process-isolator`**: Process/rootfs isolation, mount namespaces, application sandboxing, and irreversible capability-based privilege reduction.
- **`SigmaOS-pf-firewall`, `SigmaOS-network-filter`, `SigmaOS-oom-guardian` & `SigmaOS-wayland-portal`**: Default-deny stateful/stateless packet filters, protected-process OOM policy guard, and sandboxed desktop portal broker.
- **`SigmaOS-boot-verify`, `SigmaOS-crypto-keys`, `SigmaOS-audit-log`, `SigmaOS-signed`, `SigmaOS-security-hardening`**: Measured boot verification, PKI trust store, tamper-evident SHA-256 chained audit log, and package signature verification.

## 4. Desktop Environment & Theming
- **`SigmaOS-deskland`, `SigmaOS-shell`, `SigmaOS-shell-config`, `SigmaOS-quickshell`**: Wayland/Hyprland-based desktop shell and compositor integration.
- **`SigmaOS-aether`, `SigmaOS-theme-registry`, `SigmaOS-theme-marketplace`, `SigmaOS-theme-sync`**: Dynamic color extraction, theme distribution, and live desktop accent syncing.
- **`SigmaOS-folio`, `SigmaOS-notification-center`, `SigmaOS-notifications`, `SigmaOS-screenshot`, `SigmaOS-screensaver`**: Native desktop utilities.

## 5. Application, Data & Developer Suites
- **Office & Productivity:** `SigmaOS-betteroffice`, `SigmaOS-genoffice`, `SigmaOS-libreoffice`, `SigmaOS-onlyoffice`, `SigmaOS-iloveapi`, `SigmaOS-craft`, `SigmaOS-write`, `SigmaOS-calc`, `SigmaOS-hype`.
- **Data Science & Engineering:** `SigmaOS-bigdata`, `SigmaOS-bi-analytics`, `SigmaOS-data-wrangling`, `SigmaOS-duckdb`, `SigmaOS-trino`, `SigmaOS-eda`, `SigmaOS-ml-dl`, `SigmaOS-notebooks`, `SigmaOS-rdbms`.
- **Browsers & Virtualization:** `SigmaOS-browser`, `SigmaOS-chromium`, `SigmaOS-zen-browser`, `SigmaOS-app-env`, `SigmaOS-dos`, `SigmaOS-mac-vm`, `SigmaOS-windows-vm`.
- **AI & Developer Ecosystem:** `SigmaOS-local-ai`, `SigmaOS-skills`, `SigmaOS-plugin-marketplace`, `SigmaOS-lazyvim`, `SigmaOS-dots`.

See [Component-Map](./Component-Map) for the full dependency graph.
