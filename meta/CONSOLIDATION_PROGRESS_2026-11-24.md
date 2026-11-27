# SigmaOS Consolidation Progress — 2026-11-24

## Completed Today

### 1. ISO Pipeline — Network Resilience
- **Problem**: E2E installer test failed on slow QEMU mirrors due to pacman's 10s download stall timeout aborting whole pacstrap transactions.
- **Fix**: Added `DisableDownloadTimeout` to:
  - `iso/archiso/airootfs/etc/pacman.conf` (live system)
  - `iso/archiso/pacman.conf` (build profile)
  - `sigmaos-install` runtime patch (installed system)
- **Result**: Slow-but-alive mirrors (300 KiB/s) can now complete downloads; retry logic covers dead mirrors.
- **Committed**: `76feb0d` — pushed to SigmaOS-ISO/main.

### 2. CI — Installer E2E Workflow
- **Created**: `.github/workflows/installer-e2e.yml`
  - Runs weekly (Mondays 06:00 UTC) + manual dispatch
  - Downloads latest release ISO (handles split .part assets + sha256 validation)
  - Executes `scripts/ci/qemu_installer_e2e.sh` with 40m install + 10m boot timeouts
  - Uploads serial logs on failure
- **Note**: Currently running (`45365476458`) — first automated E2E test.
- **Committed**: `3cd91ca` — pushed to SigmaOS-ISO/main.

### 3. Repo Consolidation — Archived Empty Stubs
Archived 7 empty/scaffolding repos on GitHub (preserved in canonicals):
- `SigmaOS-cards-checkmate-dup` → canonical = SigmaOS-cards
- `SigmaOS-m1n1-done` → canonical = SigmaOS-m1n1
- `SigmaOS-omarchy-pkgs-sigmaos` → canonical = SigmaOS-omarchy-pkgs (private)
- `SigmaOS-site-crt2` → canonical = SigmaOS-site-crt
- `SigmaOS-omarchy-plugin-marketplace-tools` → canonical = SigmaOS-plugin-marketplace-tools
- `SigmaOS-omachee-plugin-marketplace-tools` → canonical = SigmaOS-plugin-marketplace-tools
- `SigmaOS-omakub` → upstream push blocked by secret scanning (user decision)
- **Documented**: `docs/REPO_CONSOLIDATION.md` updated with archival table.

### 4. Repo Consolidation — PENDING-PUSH.txt Resolved
- **Status**: All 51 previously-pending repos now exist on GitHub.
- **Verification**: Local HEADs verified synced for every repo.
- **Action**: Marked PENDING-PUSH.txt as resolved (retained for history; safe to delete).

### 5. Component Manifests Normalized
- **Problem**: 100 repos had mixed `COMPONENT.toml` vs `COMPONENT.tomL`:
  - 32 had proper manifests (name/id/metadata)
  - 68 had broken template stubs with `$(basename $d)` placeholders
- **Fix**: Bulk script:
  - Repos with proper manifest: removed the broken `COMPONENT.tomL` dup
  - Repos with only stub: generated proper `COMPONENT.toml` with name/id/metadata
- **Result**: All 100 repos now have consistent `COMPONENT.toml` (no `COMPONENT.tomL`).
- **Committed**: 100 individual commits (`chore: normalize component manifest to COMPONENT.toml`).
- **Pushed**: All committed to GitHub.

### 6. Branch Hygiene
- **Problem**: SigmaOS-configurator used `master` branch; all others used `main`.
- **Fix**: Migrated SigmaOS-configurator:
  - Cherrypicked manifest commit from `master` to `main`
  - Pushed `main` with complete history
  - Deleted `master` branch on GitHub
- **Result**: All SigmaOS-* repos now use `main` as canonical branch.
- **Documented**: `docs/REPO_CONSOLIDATION.md` updated.

### 7. GitHub Wiki Staging
- **Generated**: 104 component Home.md files in `sigmaos-wiki-staging/`
  - Each with repo name, short description, links to SigmaOS/ISO/main
  - Extracted from COMPONENT.tomL descriptions or README.md first paragraphs
- **Tool**: `push-wikis.sh` script created to push to initialized wikis
- **Limitation**: GitHub only materializes `<repo>.wiki.git` after manual Wiki tab visit — no API/CLI bootstrap.
- **Status**: Staging complete; awaiting one-time browser visit per repo.

## Previously Completed (Earlier Sessions)

### ISO / CI Pipeline
- **Release `sigmaos-desktop-2026.11.24-uefi`**: 2.9GB, verified BIOS + UEFI boot in QEMU
- **Firmware boot test**: `scripts/ci/qemu_firmware_boot.sh` tests both SeaBIOS and OVMF
- **Installer dry-run test**: `scripts/ci/qemu_installer_dryrun.sh` hardened with liveness checks
- **Installer E2E script**: `scripts/ci/qemu_installer_e2e.sh` (local; now in CI)

### Plugin Marketplace Consolidation
- **Merged**: SigmaOS-plugin-marketplace-site + -worker → SigmaOS-plugin-marketplace-tools
- **Archived**: -site and -worker repos on GitHub
- **Documented**: `docs/REPO_CONSOLIDATION.md` with absorption table

### Wiki Staging (Previous)
- **Sigma/main wiki**: `wiki/` directory with component pages (Init-System, Monitoring, etc.)
- **Wiki migration plan**: `docs/WIKI_MIGRATION_PLAN.md`

## Remaining from Principles List

### High Priority
1. **GitHub Wikis per component**: Open Wiki tab once per SigmaOS-* repo, then run `push-wikis.sh`
2. **Archive "absorbed" repos**: After canonical repos document absorbed content
3. **Replace scaffolds**: Some still need real implementations (e.g., SigmaOS-notifications vs SigmaOS-notification-center)
4. **Rolling release model**: Remove release tags (documented as principle, not yet executed)

### Medium Priority
5. **LFS decision for plugin-marketplace-assets**: 11,889 preview images (~GBs)
6. **Consolidate theme ecosystem**: Single-theme repos → theme-registry entries
7. **Consolidate shell config**: fish/zsh → shell-config

### Long-Term / High Effort
8. **Private repos to public**: When GitHub quota refills
9. **Web browser / professional tools clones**: Per user's 200+ item list (platforms, skills, etc.)
10. **NixOS-like configuration system**: Documented as principle; not implemented

## Stats

- **Repos**: 100 SigmaOS-* on GitHub (199 total under account)
- **Wikis staged**: 104 component Home.md files
- **Manifests normalized**: 100 repos
- **Branches unified**: 100 repos on `main`
- **Archived stubs**: 7 empty repos
- **CI workflows**: 4 (boot-smoke, build-iso, installer-e2e, hygiene)
