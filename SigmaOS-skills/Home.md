# SigmaOS-skills

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS-skills: Universal Agent Skill Registry and Execution Engine. Provides deterministic cataloging, capability matching, trigger resolution, and event lifecycle tracking for AI and developer agent skills. Skills component for SigmaOS

## Architecture
- **Language / Runtime:** `rust` (Tier: `2`, Stability: `beta`)
- **Key Structs:** `Skill`
- **Key Enums:** `SkillCategory`
- **Public Functions:** `as_str`, `new`, `with_capability`, `with_trigger`
- **Provides:** `component`
- **Component Dependencies:** `SigmaOS-system`

## Design Principles
- **Memory Safety:** Enforces `#![forbid(unsafe_code)]` at the crate root.
- **Fail-Fast Error Handling:** Uses typed error enums (`thiserror`) and explicit `Result` propagation without silent failures.
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
- **Binary:** `SigmaOS-skills`

```sh
SigmaOS-skills --help
```

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `SigmaOS-skills`
- `component.tier` = `2`
- `component.stability` = `beta`
- `component.language` = `rust`

## Dependencies
Standard SigmaOS runtime environment (no external Rust crate dependencies).

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
