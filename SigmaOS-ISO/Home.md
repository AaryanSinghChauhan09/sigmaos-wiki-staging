# SigmaOS-ISO

The bootable SigmaOS system: an Arch-based live ISO with a pre-configured
Hyprland desktop, plus the installer and release pipeline.
This is the repository that produces the downloadable `.iso`.

SigmaOS is **not** a custom-kernel project - it ships the stock Arch Linux
kernel and official Arch packages (`pacman`).

## What you get

- Live Hyprland (Wayland) desktop, autologin as `liveuser`
- Waybar status bar, Rofi launcher, foot terminal, hyprlock
- 3 tested themes: catppuccin, tokyo-night, gruvbox (`sigmaos-theme`)
- `sigmaos-doctor` - one-command health check (session, network, audio, disk, updates)
- `sigmaos-welcome` - first-login cheatsheet
- `sigmaos-install` - installer (dry-run by default; destructive steps are guarded)
- Boots via BIOS (syslinux) **and** UEFI (systemd-boot)

## Live session credentials

- **user:** `liveuser` - **password:** `sigmaos`
- `liveuser` is in `wheel`; `sudo` uses the same password.
- `root` is locked in the live image. `sigmaos-install` prompts for new
  credentials on install.

## Download

Releases: <https://github.com/AaryanSinghChauhan09/SigmaOS-ISO/releases>

The ISO is published as split parts (`*.part00`, `*.part01`, ...) to stay under
GitHub's 2 GiB asset limit. Reassemble and verify:

```bash
cat sigmaos-desktop-*.iso.part* > sigmaos-desktop.iso
sha256sum -c sigmaos-desktop-*.iso.sha256   # or .parts.sha256 for the parts
```

Site download page: <https://aaryansinghchauhan09.github.io/Sigma/download.html>

## Requirements

- x86_64 CPU, 4 GiB RAM (8 GiB recommended), ~10 GiB free disk for install
- UEFI or legacy BIOS boot
- For VMs: QEMU/KVM or any mainstream hypervisor works

## Build

Requires Docker **or** an Arch Linux host with `archiso`.

```bash
# Validate the profile only (any host):
scripts/build_archiso.sh --validate-only

# Build via Docker (works on Ubuntu/Debian hosts):
scripts/build_archiso.sh --docker

# Build natively on Arch Linux:
sudo scripts/build_archiso.sh --native
```

Output: `out/sigmaos-desktop-<date>-x86_64.iso`. The build fails if the ISO is
missing, suspiciously small, or not a readable ISO9660 image.

The ISO is produced by `mkarchiso` (archiso), which writes a hybrid
MBR/GPT El Torito image with the EFI system partition appended as a GPT
partition - the same mechanism official Arch ISOs use.

## Verification

```bash
# Direct kernel/initramfs boot test (fast, bypasses firmware):
bash scripts/ci/qemu_iso_boot.sh out/*.iso

# Real firmware boot test - SeaBIOS + OVMF, requires kernel markers on
# the serial console (boot entries include console=ttyS0):
bash scripts/ci/qemu_firmware_boot.sh out/*.iso both
```

Both run in CI on every ISO build. A release is only published after these
pass.

Manual QEMU test:

```bash
qemu-system-x86_64 -m 4G -enable-kvm -cdrom out/*.iso
# UEFI: add OVMF pflash drives and -boot d (see qemu_firmware_boot.sh)
```

## Repository layout

- `iso/archiso/` - archiso profile (packages, bootloader entries, airootfs)
- `iso_root/` - installer root filesystem bits
- `scripts/` - build, signing, reassembly, CI helpers
- `installer/` - `sigmaos-install` implementation

## Compatibility matrix

| Platform | Status |
|---|---|
| BIOS boot (SeaBIOS, syslinux) | Verified in QEMU |
| UEFI boot (OVMF/EDK2, systemd-boot) | Verified in QEMU (2026.11.24+) |
| `dd`-written USB | Supported (hybrid ISO) |
| Secure Boot | Not supported - image is unsigned |
| NVIDIA GPUs | Experimental - untested |
| aarch64 / ARM | Not supported (x86_64 only) |

## Known issues

- Releases before `sigmaos-desktop-2026.11.24-uefi` have a broken UEFI
  boot path - use BIOS mode or upgrade to the 2026.11.24 release.
- Full OS installation (`sigmaos-install --destructive`) is experimental;
  the dry-run and disk-safety paths are CI-tested, end-to-end install is
  not yet verified.
- Snapshot/rollback features are not yet implemented end-to-end; do not
  rely on them.

## Recovery

- **Bad theme/config:** `sigmaos-theme reset` restores defaults (backs up
  current config first); `sigmaos-doctor` (SUPER+/) diagnoses session,
  network, audio, disk, and update problems.
- **Boot problems:** boot the ISO in a VM first; the live session needs no
  installation. Serial console (`console=ttyS0`) shows kernel logs.
- **Failed updates:** boot the previous known-good environment; package
  state can be inspected with `pacman -Q` / `journalctl -b -p err`.

## Security features

SigmaOS includes security hardening beyond the baseline Arch Linux:

- **AppArmor**: Enabled in enforcement mode by default
- **Kernel hardening**: ASLR, ptrace restrictions, network hardening, unprivileged BPF disabled
- **Audit logging**: `auditd` pre-installed for security event logging
- **Automatic security updates**: Daily systemd timer with randomized delay
- **Package signing**: Required repository signatures with `archlinux-keyring`
- **Mirror ranking**: Automatic mirror ranking via `reflector` with weekly updates

## System recovery

SigmaOS provides advanced recovery features:

- **BTRFS snapshots**: Automatic snapshots before and after pacman transactions
- **Rollback utility**: `sigmaos-snapshot rollback` for easy system rollback
- **BTRFS optimizations**: zstd:3 compression, SSD detection with TRIM, async discard
- **Additional subvolume**: `@var_tmp` for better tmp directory isolation

## Package management

SigmaOS uses standard Arch package management with enhancements:

- **Baseline**: Standard `pacman` and official Arch repositories
- **Signed packages**: Repository signatures required (`SigLevel = Required DatabaseOptional`)
- **Keyring**: `archlinux-keyring` included for package verification
- **Mirrors**: Geo-DNS mirror with fallback list, automatic ranking via `reflector`
- **Parallel downloads**: 5 parallel downloads by default
- **Space checking**: `CheckSpace` enabled to prevent full-disk failures

## Desktop features

The live session includes a pre-configured Hyprland desktop:

- **Compositor**: Hyprland with Wayland
- **Status bar**: Waybar with app menu launcher and media player integration
- **Launcher**: Rofi for application launching
- **Terminal**: foot terminal with enhanced zsh configuration
- **Shell**: Enhanced zsh with history, completion, aliases, zoxide, fzf
- **Theme**: Starship prompt with SigmaOS color palette
- **Themes**: 3 tested themes (catppuccin, tokyo-night, gruvbox) via `sigmaos-theme`
- **Audio**: PipeWire, WirePlumber, Bluetooth support
- **Media**: Screenshot/recording tools, display tools

## Documentation

- **[Parity Matrix](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO/blob/main/PARITY_MATRIX.md)**: Detailed comparison with Arch Linux and Omarchy
- **[Supported Features](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO/blob/main/SUPPORTED_FEATURES.md)**: Verified, partial, and experimental features
- **[Plugin Marketplace Consolidation](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO/blob/main/PLUGIN_MARKETPLACE_CONSOLIDATION.md)**: Marketplace architecture
- **[Theme Consolidation](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO/blob/main/THEME_CONSOLIDATION.md)**: Theme ecosystem architecture

## Support status

- **Verified:** BIOS + UEFI boot in QEMU, live Hyprland session, MVP tools
  present in the shipped image, installer dry-run safety in QEMU.
- **Experimental:** installer end-to-end install in VM, Secure Boot signing
  (needs enrolled keys), snapshot/rollback features, NVIDIA hardware.

Report issues: <https://github.com/AaryanSinghChauhan09/SigmaOS-ISO/issues>

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
