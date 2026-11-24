# SigmaOS Initramfs

Hook-based initramfs image builder — mkinitcpio-style pipeline where
each hook declares kernel modules, binaries, and files to embed.

## Capabilities

- TOML hook definitions with `depends` and `order`
- Deterministic topological ordering (Kahn's algorithm)
- Cycle and missing-dependency detection
- JSON build plan for `sigmaos-rebuild` to execute
- `--dry-run` hook listing via CLI

## Interconnectivity

| Repo | Relationship |
|------|-------------|
| `sigmaos-rebuild` | Consumes initramfs build plans during rebuild |
| `sigmaos-dkms` | DKMS modules feed hook `modules` lists |
| `sigmaos-ISO` | ISO build embeds the resulting image |

## Status

Implemented locally (Rust crate, 3 tests passing). GitHub repo creation
pending rate-limit window.
