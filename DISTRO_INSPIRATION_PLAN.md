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

~~1. `sigmaos-pkg-solver`~~ — DONE (backtracking solver, pushed)
2. `sigmaos-system-profile` — DONE (declarative `system.toml`, pushed)
3. `sigmaos-initramfs` — DONE (mkinitcpio hooks + cpio builder, pushed)
~~4. `sigmaos-pockets`~~ — DONE (release pockets + pins, pushed)
5. `sigmaos-jails` — DONE (sandbox profiles for app-env, pushed)

## Progress

- `sigmaos-system-profile` — IMPLEMENTED and pushed to GitHub
  (candidate #2 above; declarative `system.toml` profile).
- `sigmaos-pkg-solver` — IMPLEMENTED and pushed to GitHub
  (candidate #1 above; backtracking solver over pkg-core records:
  version selection, virtual provides, conflicts, MRV branching,
  minimal-change keep rules, apt-style errors; 15 tests).
- `sigmaos-pockets` — IMPLEMENTED and pushed to GitHub
  (candidate #4 above; Debian-style release pockets with apt-style
  pin priorities, `apt policy` view, candidate selection; 8 tests).
- `sigmaos-initramfs` — IMPLEMENTED and pushed (Arch mkinitcpio hooks
  merged with cpio/pack image builder).
