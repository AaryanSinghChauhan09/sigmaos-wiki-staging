# SigmaOS-oom-guardian

**Category:** Security | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Out-of-memory policy guard for SigmaOS. Implements a typed OOM killer with `KillHighest`, `KillFixed`, and `Passthrough` policies — protecting critical system processes while enforcing predictable memory reclamation.

## Features

- **Three OOM policies** — `KillHighest` (score-based), `KillFixed` (targeted), `Passthrough` (kernel-delegated)
- **Process protection** — marked processes cannot be killed regardless of score
- **Kill audit trail** — `killed_count()` tracks OOM events for telemetry integration
- **Score-ordered selection** — highest `oom_score` process selected first under `KillHighest`

## API

| Function | Description |
|---|---|
| `register(entry)` | Register a process with OOM score and protection flag |
| `unregister(pid)` | Remove process from guard |
| `handle_oom()` | Execute OOM policy, returns killed PID |
| `is_protected(pid)` | Check if process is protected |
| `killed_count()` | Number of OOM kills performed |

## Errors

| Error | Condition |
|---|---|
| `NotFound(pid)` | PID not registered |
| `Protected(pid)` | Target process is marked protected |
| `NoEligible` | No killable process exists (all protected, or Passthrough) |

## Tests

6 AAA unit tests covering: kill-highest score, protected-fixed rejection, all-protected no-eligible, passthrough no-kill, killed-count tracking, is-protected check.

## See Also

- [SigmaOS-cgroup-manager](SigmaOS-cgroup-manager) — cgroup v2 resource limits
- [SigmaOS-telemetry-local](SigmaOS-telemetry-local) — local telemetry collection
- [SigmaOS-process-isolator](SigmaOS-process-isolator) — process isolation policy
