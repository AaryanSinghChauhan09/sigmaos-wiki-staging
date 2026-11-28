# SigmaOS-ports-tree

> ports-tree

## Status

- **Component**: ports-tree
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-ports-tree

## Overview

SigmaOS component: **ports-tree** — ports tree index (BSD-ports-inspired). Every ported package has a category-keyed directory with port.toml metadata, pkg-descr (DESCRIPTION + COMMENT), and MOVES relocation history. This crate is the index sigmaos-ports queries; build recipes live in the tree itself.

- `src/lib.rs` — library implementation
- `src/main.rs` — CLI entry point
- `docs/` — architecture, principles, testing, security docs

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
