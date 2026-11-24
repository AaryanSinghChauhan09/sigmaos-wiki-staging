# SigmaOS System Profile

Declarative whole-system configuration — a NixOS-style `system.toml`
that composes every component's config into one system definition.

## Capabilities

- Load/validate/save `system.toml` profiles
- Resolve enabled components and read their config files
- JSON output of the effective system view
- `--list` enabled components, `--validate` warnings

## Interconnectivity

| Repo | Relationship |
|------|-------------|
| `sigmaos-config-system` | Base config primitives |
| `sigmaos-shell-config` | Example composed component |
| `sigmaos-update-system` | Profile versioning for rolling releases |

## Status

Implemented locally (Rust crate, 3 tests passing). GitHub repo creation
pending rate-limit window.
