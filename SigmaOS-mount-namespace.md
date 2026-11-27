# SigmaOS-mount-namespace

**Category:** Security | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Mount namespace isolation tracker for SigmaOS. Models per-namespace mount tables in memory, enabling services to reason about mount point isolation without direct kernel calls — critical for container workloads and app sandboxing.

## Features

- **Multi-namespace** — creates independent namespaces with monotonic IDs
- **Mount types** — `ReadOnly`, `ReadWrite`, `Bind`, `Tmpfs`
- **Conflict detection** — rejects duplicate mount targets within a namespace
- **Surgical removal** — `remove_mount()` by namespace + target path

## API

| Function | Description |
|---|---|
| `create_namespace()` | Create a new isolated namespace, returns ID |
| `add_mount(entry)` | Add a mount to a namespace |
| `remove_mount(ns_id, target)` | Remove a mount by target path |
| `mount_count(ns_id)` | Number of mounts in a namespace |
| `namespace_count()` | Total namespaces tracked |

## Errors

| Error | Condition |
|---|---|
| `NamespaceNotFound(id)` | Operation on unknown namespace |
| `MountConflict { ns, target }` | Duplicate mount target in namespace |
| `MountNotFound { target, ns }` | Remove of non-existent mount |

## Tests

6 AAA unit tests covering: namespace count, mount add, duplicate target rejection, remove decrement, add-to-missing-ns error, remove-nonexistent error.

## See Also

- [SigmaOS-app-sandbox](SigmaOS-app-sandbox) — application sandboxing
- [SigmaOS-pledge-caps](SigmaOS-pledge-caps) — capability-based privilege reduction
- [SigmaOS-cgroup-manager](SigmaOS-cgroup-manager) — cgroup v2 resource limits
