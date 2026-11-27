# SigmaOS-owe

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
`owe` plays video files, `GIF`, and still images as the Hyprland background. Video containers include `mp4`, `mkv`, `webm`, `mov`, `avi`, `mpeg`, `ts`, `wmv`, `flv`, `ogv`, and `3gp`. It joins the SigmaOS theme switch through existing contracts only. It changes no packaged SigmaOS file.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `bench/`, `config/`, `docs/`, `hooks/`, `packaging/`, `protocols/`, `qml-plugin/`, `src/`, `systemd/`, `test/`, `third_party/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `owe`
- `component.id` = `sigmaos-owe`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`
- **Config directory:** `config/` contains runtime configuration templates.

## Dependencies
Standard SigmaOS runtime environment (no external Rust crate dependencies).

## Testing
Verify component integrity and scripts in the repository root:

```sh
# Check repository scripts and configuration
ls -la
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
