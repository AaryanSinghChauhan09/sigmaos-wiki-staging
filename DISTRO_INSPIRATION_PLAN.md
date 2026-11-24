# Distro Inspiration Plan

Per project policy: when GitHub repo-creation quota is exhausted,
plan new components inspired by other Linux/BSD distros.

## Adoptable mechanisms

### From Arch Linux
- **pacman-style binary packages** — `sigmaos-pkg-core` already models
  this; add delta packages and `.pkg.tar.zst` payload support.
- **ABS-like ports** — `sigmaos-ports` covers the tree; add `makepkg`-style
  `PKGBUILD`→build-plan translation for community ports.
- **mkinitcpio hooks** — hook-based initramfs assembly; candidate for
  `sigmaos-rebuild` (already orchestrates initramfs step).

### From Debian
- **APT solver semantics** — versioned provides/depends, phased updates;
  extend `sigmaos-pkg-core` resolver with version constraints.
- **debian-installer flow** — tasksel-like component selection during
  install; candidate for `sigmaos-installer`.
- **Stable/Testing/Unstable pockets** — pocket model for `sigmaos-update-system`.

### From Linux Mint
- **Update manager UX** — kernel vs. regular update separation,
  flatpak/snap awareness; informs `sigmaos-update-system` policy layer.
- **Timeshift-style snapshots** — `sigmaos-recovery-system` already
  tracks snapshots; add scheduled snapshot policies.

### From NixOS
- **Declarative system config** — `configuration.nix`-like single-file
  system definition; `sigmaos-config-system` already does TOML — add a
  `system.toml` profile that composes all component configs.
- **Generations** — bootable config generations map to
  `sigmaos-recovery-system` rollback entries.

### From Omarchy
- **Multi-repo component layout** — already adopted: every component is
  its own repo wired via `tools-sigmaos.sh`.
- **Opinionated defaults + easy overrides** — shell-config/desktop-env
  ship sane defaults, user TOML overrides win.

### From *BSD
- **Ports tree maturity** — `sigmaos-ports` should track
  `MOVES`/`pkg-descr` metadata equivalents.
- **jails / bhyve** — lightweight isolation; candidate for
  `sigmaos-app-env` sandbox profiles.

## Near-term candidates (need repos when quota resets)

1. `sigmaos-pkg-solver` — SAT/heuristic dependency solver split from pkg-core
2. `sigmaos-system-profile` — NixOS-style declarative whole-system config
3. `sigmaos-initramfs` — mkinitcpio-style hook pipeline
4. `sigmaos-pockets` — Debian-style release pockets for updates
5. `sigmaos-jails` — BSD-jail-inspired sandbox profiles for app-env

## Progress

- `sigmaos-system-profile` — IMPLEMENTED locally (candidate #2 above).
  Repo creation pending GitHub rate limit.
- `sigmaos-initramfs` — IMPLEMENTED locally (Arch mkinitcpio hooks).
  Repo creation pending GitHub rate limit.
