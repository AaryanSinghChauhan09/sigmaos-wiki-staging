# SigmaOS-container-engine

> **Category:** Virtualization | **Language:** Rust | **License:** GPL-3.0-or-later

OCI-compatible container runtime for SigmaOS app isolation. Provides rootless containers with environment variable propagation, lifecycle management (create → start → stop), and a `ContainerManager` registry. Designed for sandboxing desktop apps and system services without requiring root or external container daemons.

## Architecture

```
ContainerSpec ──► Container (Created)
                      │
                 .start() ──► Running
                      │
                 .stop()  ──► Stopped
```

## Key Types

| Type | Description |
|------|-------------|
| `ContainerSpec` | Image, ID, env vars, rootless flag |
| `Container` | Instance with lifecycle state machine |
| `ContainerState` | `Created` / `Running` / `Stopped` / `Failed` |
| `ContainerManager` | Registry; create, start, stop, count_running |

## Security Properties
- **Rootless by default** — all containers run as the calling user
- **Environment isolation** — env vars explicitly declared in `ContainerSpec`
- **No ambient capabilities** — integrates with `SigmaOS-pledge-caps`

## Tests (6 AAA)
- `test_create_and_start_container_aaa`
- `test_stop_running_container_aaa`
- `test_start_unknown_container_returns_false_aaa`
- `test_container_env_vars_propagated_aaa`
- `test_rootless_default_true_aaa`
- `test_multiple_containers_count_aaa`

## See Also
- [SigmaOS-jails](SigmaOS-jails)
- [SigmaOS-pledge-caps](SigmaOS-pledge-caps)
- [SigmaOS-wayland-portal](SigmaOS-wayland-portal)
