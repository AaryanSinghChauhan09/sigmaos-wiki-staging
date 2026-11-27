# SigmaOS-process-isolator

**Category:** Security | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Per-process capability and namespace isolation policy manager for SigmaOS. Provides a typed Rust layer for declaring, enforcing, and auditing Linux capability sets and namespace flags (PID, net, mount) per process — the enforcement backbone of SigmaOS app sandboxing.

## Features

- **8 typed capabilities** — `NetAdmin`, `SysAdmin`, `Kill`, `Chown`, `DacOverride`, `Setuid`, `Setgid`, `SysPtrace`
- **Minimal-by-default** — `IsolationPolicy::minimal()` starts with zero capabilities and all namespaces enabled
- **Namespace flags** — `use_pid_namespace`, `use_net_namespace`, `use_mount_namespace`, `read_only_root`
- **Policy registry** — per-PID policies with duplicate-registration protection

## API

| Function | Description |
|---|---|
| `register_policy(policy)` | Register isolation policy for a PID |
| `revoke_policy(pid)` | Remove policy for a PID |
| `check_capability(pid, cap)` | Assert capability is allowed for PID |
| `get_policy(pid)` | Retrieve full policy for a PID |
| `policy_count()` | Number of registered policies |

## Errors

| Error | Condition |
|---|---|
| `AlreadyExists(pid)` | Duplicate policy registration |
| `NotFound(pid)` | No policy registered for PID |
| `CapabilityDenied { pid, cap }` | Capability not in allowed set |

## Tests

6 AAA unit tests covering: minimal-policy denies all caps, explicitly-allowed cap passes, revoke decrements count, duplicate-policy rejection, minimal-policy namespace flags, check-cap unknown-pid.

## See Also

- [SigmaOS-pledge-caps](SigmaOS-pledge-caps) — capability pledge reduction
- [SigmaOS-mount-namespace](SigmaOS-mount-namespace) — mount namespace isolation
- [SigmaOS-app-sandbox](SigmaOS-app-sandbox) — application sandboxing
