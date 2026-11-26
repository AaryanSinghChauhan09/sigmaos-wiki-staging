# SigmaOS Package Core

pacman-style package database core — package records, version
constraints, dependency resolution, and install/remove bookkeeping.

## Capabilities

- `Package` model: name/arch/version/description + `depends`,
  `provides`, `conflicts` (Arch PKGBUILD-style fields)
- `Version` + `Constraint`: `=`, `>=`, `<`, `<=`, `^` (caret), `~`
  (tilde) matching, `parse_dep` splits `name>=1.2` style entries
- `PackageDb`: JSON-persisted `packages` + `installed` maps with
  atomic save/load
- `install` — conflict check against installed packages
- `remove` — refuses removal while an installed package depends on it
- `resolve` — dependency order honoring version constraints (cycle
  detection, skips satisfied installed deps)
- `orphans` — installed packages nothing depends on (pacman `-Qtd`)
- `search`, `list_installed`, `topo_order`

## Commands

```bash
sigmaos-pkg-core list | search <q> | deps <name> | add <file.json>
sigmaos-pkg-core install <name> <version> | remove <name>
sigmaos-pkg-core orphans | path
# global: --db <path> overrides the default data-dir db.json
```

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

8 unit tests (dep parsing, constraint matching, resolution, orphans).

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-pkg-core)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
