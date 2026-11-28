# SigmaOS-pkg-solver

**Category:** Package Management | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Backtracking dependency solver for SigmaOS, split from `sigmaos-pkg-core` per the Distro Inspiration Plan. Where pkg-core walks a single-candidate-per-name graph, pkg-solver performs real version selection across multi-version repositories — the apt/edsp/alpm-style layer.

## Features

- **Version selection** — newest-satisfying-first candidate ordering
- **Virtual `provides`** — dependency names resolve to any real package offering them (installed or candidate)
- **Two-way conflicts** — enforced against selections, candidates, and the installed set
- **Unit propagation + MRV branching** — forced picks first, then branch on the requirement with fewest viable candidates
- **Minimal-change rules** — installed packages satisfy deps in place; roots prefer the best candidate (upgrade path)
- **Apt-style error reporting** — unsatisfiable requirements name the constraining sources
- **Node budget guard** — `DEFAULT_NODE_BUDGET` prevents exponential blowup

## API

| Item | Description |
|---|---|
| `Universe` | candidates + installed `Package` records (pkg-core types) |
| `Solver::solve(roots)` | returns `Solution { install, upgrade, keep }` |
| `SolveError` | `Unsatisfiable`, `Conflict`, `InstalledConflict`, `InstalledUnsatisfied`, `BudgetExceeded`, `SelfConflict` |

## CLI

```sh
sigmaos-pkg-solver --repo repo.json solve firefox 'kernel>=6.0' [--json]
sigmaos-pkg-solver --repo repo.json explain firefox
```

Repo JSON: `{ "candidates": [...], "installed": [...] }` of pkg-core `Package` records.

## Tests

15 AAA unit tests: chains, diamonds, backtracking on conflicts, provides, installed keep/upgrade semantics, root pinning, unsat explanations.

## See Also

- [SigmaOS-pkg-core](SigmaOS-pkg-core) — package database & records
- [SigmaOS-pockets](SigmaOS-pockets) — release pocket candidate selection
- [SigmaOS-update-system](SigmaOS-update-system) — rolling-release update manager
