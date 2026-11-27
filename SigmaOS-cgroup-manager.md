# SigmaOS-cgroup-manager

**Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

cgroup v2 resource limit manager for SigmaOS. Provides a typed Rust interface for creating, populating, and enforcing resource limits on cgroup slices — CPU quota, memory ceiling, and PID count — without shell scripts or raw cgroupfs writes.

## Features

- **Typed limits** — `cpu_quota_us`, `cpu_period_us`, `memory_max_bytes`, `pids_max`
- **Slice lifecycle** — create, attach PIDs, detach PIDs, query limits
- **Duplicate-attach prevention** — rejects same PID added twice to same slice
- **Slice isolation** — independent slice state; no cross-slice interference

## API

| Function | Description |
|---|---|
| `create(name, limits)` | Create a new cgroup slice with resource limits |
| `attach_pid(cgroup, pid)` | Attach a process to a slice |
| `detach_pid(cgroup, pid)` | Remove a process from a slice |
| `get_limits(cgroup)` | Retrieve configured limits for a slice |
| `pid_count(cgroup)` | Number of PIDs in a slice |
| `slice_count()` | Total slices tracked |

## Errors

| Error | Condition |
|---|---|
| `NotFound(name)` | Operation on unknown slice |
| `AlreadyExists(name)` | Duplicate slice creation |
| `PidAlreadyMember { cgroup, pid }` | PID already attached to slice |

## Tests

6 AAA unit tests covering: slice count, memory limit retrieval, attach PID count, duplicate-PID rejection, detach decrement, duplicate-create rejection.

## See Also

- [SigmaOS-mount-namespace](SigmaOS-mount-namespace) — mount namespace isolation
- [SigmaOS-app-sandbox](SigmaOS-app-sandbox) — application sandboxing
- [SigmaOS-sleep-inhibitor](SigmaOS-sleep-inhibitor) — power inhibit leases
