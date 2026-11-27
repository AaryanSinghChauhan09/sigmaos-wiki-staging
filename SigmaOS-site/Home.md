# SigmaOS-site

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS site — static site builder. Builds a static site from a content directory: markdown-ish pages get a base HTML template with {{title}}/{{content}} substitution, assets are copied verbatim, and an index page links everything. SigmaOS component inspired by the corresponding SigmaOS repository. See `docs/OMARCHY_INSPIRATION.md` in the main SigmaOS repository.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Key Structs:** `SiteConfig`, `BuiltPage`, `BuildResult`
- **Key Enums:** `SiteError`
- **Public Functions:** `render`, `escape_html`, `markdown_to_html`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigmaos-site`
- **Subcommands / Actions:** `build`, `defaultconfig`, `saveconfig`, `preview`

```sh
sigmaos-site --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `site`
- `component.id` = `sigmaos-site`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `serde` (`1.0`)
- `serde_json` (`1.0`)
- `thiserror` (`1.0`)
- `log` (`0.4`)
- `env_logger` (`0.10`)
- `clap` (`4.0`)
- `walkdir` (`2.5`)

**Dev Dependencies:** `tempfile`

## Testing
Run the test suite and linter:

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
