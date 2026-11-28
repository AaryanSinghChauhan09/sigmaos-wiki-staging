# Development — SigmaOS-cards

## Build & Test

```sh
mkdir -p build && cd build
cmake ..
make
make test
```

## Conventions

## Rules

- Single `main` branch; feature branches only for work needing tests,
  merged after tests pass.
- No `unsafe` code (crate has `#![forbid(unsafe_code)]`).
- No hardcoded secrets — env vars or secret manager only.
- GPL-3.0-or-later. SigmaOS identity only; no upstream project references.
- Docs live in the GitHub Wiki; keep `docs/` minimal staging content.
- Follow SOLID, DRY, KISS, YAGNI; fail-fast errors; secure defaults.
- Component manifest: `COMPONENT.tomL`. Interconnect: `tools-sigmaos.sh`.

## Related

- [Home](Home.md)
