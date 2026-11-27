# SigmaOS-secrets-vault

**Category:** Security | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Local scoped secret and keyring manager for SigmaOS. Provides a lockable, versioned secret store organized by `(scope, key)` pairs — replacing fragmented keyrings and plaintext `.env` files.

## Features

- **Lock/unlock enforcement** — `lock()` blocks all reads, writes, and deletes with `VaultError::Locked`
- **Automatic secret versioning** — updating an existing `(scope, key)` increments its `version`
- **Scoped isolation** — secrets are partitioned by non-empty `scope` and `key` identifiers

## API

| Function | Description |
|---|---|
| `set(scope, key, value)` | Store or rotate a secret, returning its version |
| `get(scope, key)` | Retrieve a secret entry if unlocked |
| `delete(scope, key)` | Remove a secret entry if unlocked |
| `lock()` / `unlock()` | Toggle vault access state |
| `secret_count()` | Total stored secrets |

## Tests

6 AAA unit tests covering: set/get round-trip, version increment on rotation, locked-vault blocking, unlock restoration, empty identifier rejection, secret deletion.

## See Also

- [SigmaOS-crypto-keys](SigmaOS-crypto-keys) — PKI key management
- [SigmaOS-app-sandbox](SigmaOS-app-sandbox) — application sandboxing
- [SigmaOS-audit-log](SigmaOS-audit-log) — tamper-evident audit journal
