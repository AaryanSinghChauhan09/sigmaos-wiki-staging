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
- **`SigmaOS-sigma-bootloader` & `SigmaOS-initramfs`**: Bootloader orchestration and deterministic `newc` cpio initramfs builder with topological hook ordering.
- **`SigmaOS-dkms` & `SigmaOS-mesa`**: Dynamic kernel module support and 3D/Vulkan graphics stack.
- **`SigmaOS-ISO`, `SigmaOS-installer`, `SigmaOS-live-media`**: Bootable live media builder and guided system installer.

## 2. Core System & Package Management
- **`SigmaOS-config-system` & `SigmaOS-system-profile`**: Declarative, schema-validated TOML/JSON/YAML system configuration.
- **`SigmaOS-pkg-core`, `SigmaOS-build-system`, `SigmaOS-ports`, `SigmaOS-mirror`**: Package lifecycle, reproducible builds, and rolling package mirrors.
- **`SigmaOS-update-system`, `SigmaOS-recovery-system`, `SigmaOS-rollback`, `SigmaOS-rebuild`, `SigmaOS-zfs-integration`**: Atomic updates, ZFS snapshots, and instant system rollback.
- **`SigmaOS-sigma-sh` & `SigmaOS-sigma-sys`**: Core system shell and system-level runtime utilities.

## 3. Desktop Environment & Theming
- **`SigmaOS-deskland`, `SigmaOS-shell`, `SigmaOS-shell-config`, `SigmaOS-quickshell`**: Wayland/Hyprland-based desktop shell and compositor integration.
- **`SigmaOS-aether`, `SigmaOS-theme-registry`, `SigmaOS-theme-marketplace`, `SigmaOS-theme-sync`**: Dynamic color extraction, theme distribution, and live desktop accent syncing.
- **`SigmaOS-folio`, `SigmaOS-notification-center`, `SigmaOS-notifications`, `SigmaOS-screenshot`, `SigmaOS-screensaver`**: Native desktop utilities.

## 4. Application, Data & Developer Suites
- **Office & Productivity:** `SigmaOS-betteroffice`, `SigmaOS-genoffice`, `SigmaOS-libreoffice`, `SigmaOS-onlyoffice`, `SigmaOS-iloveapi`, `SigmaOS-craft`, `SigmaOS-write`, `SigmaOS-calc`, `SigmaOS-hype`.
- **Data Science & Engineering:** `SigmaOS-bigdata`, `SigmaOS-bi-analytics`, `SigmaOS-data-wrangling`, `SigmaOS-duckdb`, `SigmaOS-trino`, `SigmaOS-eda`, `SigmaOS-ml-dl`, `SigmaOS-notebooks`, `SigmaOS-rdbms`.
- **Browsers & Virtualization:** `SigmaOS-browser`, `SigmaOS-chromium`, `SigmaOS-zen-browser`, `SigmaOS-app-env`, `SigmaOS-dos`, `SigmaOS-mac-vm`, `SigmaOS-windows-vm`.
- **AI & Developer Ecosystem:** `SigmaOS-local-ai`, `SigmaOS-skills`, `SigmaOS-plugin-marketplace`, `SigmaOS-lazyvim`, `SigmaOS-dots`.

See [Component-Map](./Component-Map) for the full dependency graph.
