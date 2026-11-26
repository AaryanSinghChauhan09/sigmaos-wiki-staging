# SigmaOS Mac Lab

SigmaOS Mac Lab tests SigmaOS on real Apple Silicon Macs and publishes what it finds. Hand it a kernel and it boots that kernel exactly once, runs tests (including Wayland GUI tests), collects logs, and restores the Mac to its known-good kernel.

## Pieces

| Binary | Runs on | Job |
|---|---|---|
| `labd` | any Linux box, or a Mac | Controller: devices, leases, job queue, recovery ladder, notifications, artifact and log store |
| `lab-agent` | each test Mac (SigmaOS/Asahi, aarch64) | Heartbeat; stages kernels, arms the one-shot boot, runs tests, uploads logs |
| `oobd` | the mini, as a root LaunchDaemon | Out-of-band hard reset for lab-owned Macs through the pinned `macvdmtool` |
| `lab` | your machine | CLI, and `lab mcp` for agents |

## How a job runs

1. **Stage** the artifact beside the known-good kernel without touching it.
2. **Boot once** with a one-shot flag that clears before booting the test entry.
3. **Watch** for the tagged check-in (`maclab.job=<id>` on the kernel command line).
4. **Test** — `boot-health` always runs, followed by builtin or custom tests.
5. **Recover** to the known-good kernel; if recovery needs a person, the lab says exactly what to press.

```sh
lab run m1air --kernel kernel-7.2.0-rc1-lab1.tar.zst --gui-test gui-smoke
```

AI agents get the same operations over MCP (`lab mcp`).

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-maclab)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
