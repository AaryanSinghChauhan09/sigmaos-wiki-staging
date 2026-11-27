# SigmaOS-zsh

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
Shared shell config (aliases, functions, environment, init) is pulled from [omadots](https://github.com/SigmaOS-io/omadots) at package build time. This repo only contains the zsh-specific bits. Config is sourced directly from `/usr/share/` so package updates take effect immediately.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `bin/`, `shell/`, `templates/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference

```sh
graph LR
    bashrc[~/.bashrc] -->|exec zsh| zshrc[~/.zshrc]
    zshrc --> zoptions & all
    all --> envs & aliases & functions & inits

    style zoptions fill:#68f,stroke:#333,color:#fff
    style envs fill:#4a9,stroke:#333,color:#fff
    style aliases fill:#4a9,stroke:#333,color:#fff
    style functions fill:#4a9,stroke:#333,color:#fff
    style inits fill:#4a9,stroke:#333,color:#fff
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `zsh`
- `component.id` = `sigmaos-zsh`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

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
