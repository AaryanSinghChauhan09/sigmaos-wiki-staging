# SigmaOS-omafind

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
Local, on-device semantic file search for [SigmaOS](https://sigmaos.org). Press `SUPER + CTRL + G`, describe what you're looking for, and Omafind finds it: *a dog on the beach* finds the photo, *the clause about pets in the lease* finds the page of the PDF, *where they talk about sleep* finds the moment in the recording. Photos, screenshots (with the text on them), PDFs (scans too), documents (txt, md, html, docx, odt, epub), audio, video and, opt-in, code. Nothing leaves the machine.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `Cargo.toml`, `assets/`, `crates/`, `evals/`, `install.sh`, `packaging/`, `scripts/`, `systemd/`, `target/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `omafind`
- `component.id` = `sigmaos-omafind`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
Standard SigmaOS runtime environment (no external Rust crate dependencies).

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
