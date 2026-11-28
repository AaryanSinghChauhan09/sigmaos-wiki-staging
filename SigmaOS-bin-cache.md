# SigmaOS-bin-cache

**Category:** Package Management | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Signed reproducible binary package cache — the binary half of SigmaOS's source+binary hybrid packaging track. Ports build once from source; the payload is cached by a reproducibility key so later installs skip rebuilding.

## Features

- **Reproducibility key** — `(package, version, arch, source_rev, toolchain, flags_hash)`; identical inputs share an entry
- **Content addressing** — payload stored under its SHA-256; verified on every fetch
- **Corruption eviction** — hash mismatch drops the entry and errors
- **Signature metadata** — detached `Signature { key_id, blob, signed_unix }`; `require_signatures` policy (crypto delegated to sigmaos-crypto-keys)
- **Hit counters + builder provenance**
- **Atomic writes** — tmp+rename for index and payloads
- **`sigma-bincache` CLI** — put/get/list/show/evict/require-sigs

## Tests

7 AAA unit tests: round-trip, key uniqueness, corruption eviction, signature policy, find/package queries, save/load, evict.

## See Also

- [SigmaOS-ports](SigmaOS-ports) — ports tree
- [SigmaOS-build-system](SigmaOS-build-system) — package build system
- [SigmaOS-pkg-solver](SigmaOS-pkg-solver) — dependency solver
- [SigmaOS-crypto-keys](SigmaOS-crypto-keys) — key management
