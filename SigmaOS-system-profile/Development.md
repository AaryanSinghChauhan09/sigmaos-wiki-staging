# Development — SigmaOS-system-profile

## Build & Test

```sh
cargo test
cargo clippy --all-targets -- -D warnings
cargo fmt --check
```

## Conventions

## Rules

- Single `main` branch; feature branches only for work needing tests,
  merged after tests pass.
- GPL-3.0-or-later. SigmaOS identity only; no upstream project references.
- Docs live in the GitHub Wiki; keep `docs/` minimal staging content.
- Follow SOLID, DRY, KISS, YAGNI; fail-fast errors; secure defaults.
- Component manifest: `COMPONENT.toml`. Interconnect: `tools-sigmaos.sh`.
- No hardcoded paths outside `~/.config/sigmaos/` and `~/.local/state/sigmaos/`.

## Related

- [Home](Home.md)
