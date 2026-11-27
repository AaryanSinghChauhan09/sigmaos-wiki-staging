# SigmaOS Future Architecture Plan — Linux & BSD Systems Roadmap

When GitHub repository creation quota resets, the following queued and next-phase SigmaOS component repositories will be published and integrated.

## Phase 1: Immediate Queue (Locally Built, Tested & Committed)

78 locally verified `SigmaOS-*` repositories (`cargo test --offline` passing, `#![forbid(unsafe_code)]`, 4+ AAA tests, `tools-sigmaos.sh` v2.1, `COMPONENT.toml`, `AGENTS.md`, `README.md` with `## See Also`) are queued in `push_all_no_remote.sh`:

- **Batch 14 (27 repos):** Core GUI Platform frameworks (`SigmaOS-basic`, `SigmaOS-tauri`, `SigmaOS-gtk-rs`, `SigmaOS-qt`, `SigmaOS-pyqt`, `SigmaOS-pyside`, `SigmaOS-gpui`, `SigmaOS-imgui`, `SigmaOS-sdl2`, `SigmaOS-tkinter`, `SigmaOS-nwjs`, `SigmaOS-wails`, `SigmaOS-flet`, `SigmaOS-nicegui`, `SigmaOS-pywebview`, `SigmaOS-webview`, `SigmaOS-wxwidgets`, `SigmaOS-wxpython`, `SigmaOS-kivy`, `SigmaOS-javafx`, `SigmaOS-compose-multiplatform`, `SigmaOS-elm-ui`, `SigmaOS-fyne`, `SigmaOS-sciter`, `SigmaOS-ultralight`, `SigmaOS-waydroid`, `SigmaOS-shiny`)
- **Batch 15 (31 repos):** GenOffice sub-repos (6), BetterOffice sub-repos (4), iLove series (3), OnlyOffice sub-repos (5), RDBMS sub-repos (5), extra GUI platforms (7), `SigmaOS-linux-mint`
- **Batch 16 (11 repos):** Extended GUI Platform frameworks (`SigmaOS-tauri-v2`, `SigmaOS-revery`, `SigmaOS-reactnative-desktop`, `SigmaOS-nativephp`, `SigmaOS-saucer`, `SigmaOS-una-platform`, `SigmaOS-vaadin`, `SigmaOS-monomer`, `SigmaOS-renweb`, `SigmaOS-electrobun`, `SigmaOS-nodegui`)
- **Batch 17 (9 repos):** Big Data, ETL, EDA & Tools (`SigmaOS-flink`, `SigmaOS-spark`, `SigmaOS-nifi`, `SigmaOS-dbt`, `SigmaOS-pandas`, `SigmaOS-talend`, `SigmaOS-ggplot2`, `SigmaOS-command-code`, `SigmaOS-python`)

## Phase 2: Linux & BSD Systems Capabilities (Next-Generation OS Sub-Repos)

Drawing on proven systems engineering patterns from modern Linux and BSD operating systems—while maintaining 100% SigmaOS-native identity—future component repositories will cover:

1. **Declarative System Configuration (`SigmaOS-sys-declare`, `SigmaOS-generations`)**
   - Declarative, reproducible system state graphs with atomic generation switching and instant boot-time rollback.
2. **BSD-Inspired Security & Isolation (`SigmaOS-jails`, `SigmaOS-pledge-caps`, `SigmaOS-pf-firewall`)**
   - Lightweight kernel-enforced process/filesystem jails, capability-based privilege reduction, and stateful packet filtering.
3. **Immutable Root & Atomic Updates (`SigmaOS-atomic-root`, `SigmaOS-ab-boot`)**
   - Read-only verified root images with A/B bootloader slot switching and cryptographic update verification.
4. **Source-Based & Binary Hybrid Packaging (`SigmaOS-ports-tree`, `SigmaOS-bin-cache`)**
   - Deterministic source build recipes paired with signed reproducible binary caches and isolated dependency sandboxes.
5. **Storage & Snapshots (`SigmaOS-zfs-snapshots`, `SigmaOS-btrfs-subvols`)**
   - Copy-on-write snapshot lifecycles integrated directly into package transactions and pre-upgrade hooks.
6. **Hardware & Bootloader Integration (`SigmaOS-efi-boot`, `SigmaOS-udev-rules`, `SigmaOS-firmware-hub`)**
   - Unified EFI boot manager, hot-plug device rule orchestration, and reproducible initramfs generation.
7. **Desktop & Compositor Ecosystem (`SigmaOS-deskland`, `SigmaOS-wayland-portal`, `SigmaOS-pipewire-studio`)**
   - Zero-copy Wayland compositor integration, sandboxed desktop portals, and low-latency audio routing.
8. **Extended GUI Platform Bindings**
   - Remaining cross-language GUI toolkit bridges (`SigmaOS-are-we-gui-yet`, `SigmaOS-astrodon`, `SigmaOS-blockly`, `SigmaOS-chromely`, `SigmaOS-eel`, `SigmaOS-lazarus`, `SigmaOS-swing`, etc.).

## Phase 3: Repository Hygiene & Unblocking

- Unarchive the 5 read-only GitHub repositories (`SigmaOS-mac-support`, `SigmaOS-notifications`, `SigmaOS-plugin-marketplace-site`, `SigmaOS-plugin-marketplace-worker`, `SigmaOS-themes-intros`) in the GitHub UI and push pending `tools-sigmaos.sh` + `README.md` updates.
- Initialize GitHub Wiki `.wiki.git` endpoints and run `push-wikis.sh` to publish all staged `Home.md` pages.
