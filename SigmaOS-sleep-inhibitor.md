# SigmaOS-sleep-inhibitor

**Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Power sleep inhibit lease manager for SigmaOS. Provides a `Block`/`Delay` inhibitor model (compatible with `systemd-inhibit` semantics) allowing services to hold typed leases that prevent or delay system sleep/suspend transitions.

## Features

- **Two inhibit modes** — `Block` (hard prevent) and `Delay` (defer until released)
- **Lease tracking** — unique IDs with `who`/`why` attribution per lease
- **Automatic clear** — `is_inhibited()` reflects live lease state; no periodic polling needed
- **Block-count separation** — `block_count()` distinguishes hard blockers from delay holders

## API

| Function | Description |
|---|---|
| `acquire(who, why, mode)` | Acquire an inhibit lease, returns lease ID |
| `release(id)` | Release a lease by ID |
| `is_inhibited()` | True if any leases are held |
| `block_count()` | Number of Block-mode leases |
| `lease_count()` | Total leases held |
| `get_lease(id)` | Retrieve lease by ID |

## Errors

| Error | Condition |
|---|---|
| `LeaseNotFound(id)` | `release()` called with unknown ID |
| `DuplicateId(id)` | Internal ID collision (never occurs in normal use) |

## Tests

6 AAA unit tests covering: acquire/is-inhibited, release clears inhibit, block-count vs delay, get-lease content, release-nonexistent error, lease-count decrement.

## See Also

- [SigmaOS-power-manager](SigmaOS-power-manager) — power state coordination
- [SigmaOS-service-supervisor](SigmaOS-service-supervisor) — service lifecycle
- [SigmaOS-cgroup-manager](SigmaOS-cgroup-manager) — resource limit management
