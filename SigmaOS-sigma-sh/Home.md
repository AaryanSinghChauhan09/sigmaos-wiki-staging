# SigmaOS-sigma-sh

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS sigma-sh — POSIX-ish system shell and init (`sigma-init`). ~100 builtins covering aliases, functions, history, trap/EXIT, read/select loops, `.`/source, exec/fork/wait, job stubs (jobs/fg/bg), pushd/popd/dirs, mount/umount/df/dmesg, and coreutils-style text tools. Supports `if/for/while/until/case` compound commands, `[[ ]]` tests with `&&/||/!/glob/regex`, `$(( ))` arithmetic, `${var}` expansions with affix trimming, `>`/`>>`/fd redirection, and `|` pipelines that run real concurrent child processes over kernel pipes.

## Architecture
- **Language / Runtime:** `rust` (Tier: `standard`, Stability: `active`)
- **Traits:** `Io`, `Fs`, `ProcTable`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `sigma-sh`, `sigma-init`, `ls`, `cat`, `ps`, `pkg`, `kill`, `mount`, `sigma-child`, `sh`

```sh
sigma-sh --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-sigma-sh`
- `component.license` = `GPL-3.0-or-later`
- **Feature flags:** `default`, `sigmaos-target`

## Dependencies
**Rust Crates (`Cargo.toml`):**
- `sigmaos-sigma-sys` (`*`)

**SigmaOS Component Dependencies:** `sigmaos-sigma-sys`, `sigmaos-sigma-kernel`

## Testing
Run the Rust test suite and Clippy checks:

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
