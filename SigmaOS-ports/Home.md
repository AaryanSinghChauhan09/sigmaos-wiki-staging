# SigmaOS Ports

Ports tree database for SigmaOS — a categorized, dependency-aware
registry of buildable software entries, inspired by BSD ports.

## Overview

`SigmaOS-ports` is a Rust library + CLI (`sigmaos-ports`) that manages
a ports collection: each `Port` has a name, category, version,
description, dependency list, license, maintainer, and build state
(`available` / `building` / `installed` / `failed`). The database is
JSON-backed with atomic save (write-temp-then-rename) and lives under
the XDG data dir by default.

## Features

- **Categories**: ports grouped into named categories
- **Dependency-ordered build plans**: `build_plan` topologically sorts
  a target's dependencies (deps before dependents) and reports cycles
  and missing ports as typed errors
- **State tracking**: mark ports `building`/`installed`/`failed` and
  query by state
- **Search**: case-insensitive match on name and description
- **Persistence**: `save`/`load` JSON roundtrip
- **Tests**: 5 unit tests cover categories, build-plan ordering,
  cycle/missing detection, state transitions, search, and persistence

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-ports)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
