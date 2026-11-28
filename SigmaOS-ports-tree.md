# SigmaOS-ports-tree

**Category:** Package Management | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Pending publication

## Purpose

BSD-ports-inspired ports tree index — the metadata layer over `sigmaos-ports`. Every ported package gets a `(category, name)` record with pkg-descr-style description/comment, dependency names, license, maintainer, plus MOVES relocation history.

## Features

- **Port records** — name/category/version/description/comment/depends/license/homepage/maintainer
- **MOVES history** — relocation log per port (BSD `MOVES` equivalent)
- **Queries** — category listing, case-insensitive search, cross-category duplicate detection
- **Atomic JSON persistence** + `sigma-ports` CLI (categories/list/show/search/add/move/history/duplicates)

## Tests

7 AAA unit tests: add/get, duplicate rejection, categories, search, duplicates, moves, save/load.

## See Also

- [SigmaOS-ports](SigmaOS-ports) — ports build engine
- [SigmaOS-pkg-core](SigmaOS-pkg-core) — package database
