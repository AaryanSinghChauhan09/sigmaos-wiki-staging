# SigmaOS-pockets

**Category:** Package Management | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Debian-style release pockets for SigmaOS: packages live in named pockets (`stable`, `testing`, `unstable`, `experimental`, plus `updates`, `security`, `backports`, `proposed-updates`) and apt-style pin priorities decide which pocket's version becomes the install candidate. This is the policy layer `sigmaos-update-system` consults before handing candidates to `sigmaos-pkg-solver`.

## Features

- **Pocket model** — `PocketDb` maps pocket names to package records
- **Default priorities** — stable 990 > updates/security/testing 500 > unstable 400 > backports/proposed/experimental
- **Pin rules** — apt `preferences`-style `Pin { package glob, pocket glob, version constraint, priority }`; highest matching pin wins
- **Candidate selection** — `candidate(name)` mirrors apt: highest priority, then highest version
- **`apt policy` view** — `policy(name)` lists every pocket's version + effective priority
- **JSON persistence** — `save`/`load` with merged default priorities

## API

| Item | Description |
|---|---|
| `PocketDb::new/add/entries/candidate/policy/candidates` | pocket database operations |
| `PocketDb::priority_of` | pin-then-default priority resolution |
| `Pin::matches` | glob + version-scoped pin matching |
| `pocket::*` | well-known pocket name constants |
| `PocketDb::solver_repo_json` | export in pkg-solver `{candidates,installed}` format |
| `PocketDb::upgradable` | installed-vs-candidate upgrade list (Version-ordered) |

## CLI

```sh
sigmaos-pockets --db pockets.json policy firefox
sigmaos-pockets --db pockets.json candidate firefox
sigmaos-pockets --db pockets.json add stable packages.json
sigmaos-pockets --db pockets.json pin --package 'linux*' --pocket security --priority 1000

# apt list --upgradable analogue (installed JSON -> old -> new)
sigmaos-pockets --db pockets.json upgradable --installed installed.json

# Feed pocket-selected candidates into the dependency solver:
sigmaos-pockets --db pockets.json export --installed installed.json --out repo.json
sigmaos-pkg-solver --repo repo.json solve firefox 'kernel>=6.0'
```

## Tests

10 AAA unit tests: default ordering, pin override, security-update priority, policy listing, glob pins, version-scoped pins, save/load round-trip, whole-db candidate view.

## See Also

- [SigmaOS-pkg-core](SigmaOS-pkg-core) — package database & records
- [SigmaOS-pkg-solver](SigmaOS-pkg-solver) — dependency solver
- [SigmaOS-update-system](SigmaOS-update-system) — rolling-release update manager
