# SigmaOS DKMS

Dynamic Kernel Module Support state tracker for SigmaOS — records
out-of-tree kernel modules and their per-kernel-release build status.

## Overview

`SigmaOS-dkms` is a Rust library + CLI (`sigmaos-dkms`) that tracks
DKMS-managed modules: each `KernelModule` has a name, version, and a
map of kernel release → status (`none`/`built`/`installed`/`failed`).
The database is JSON-backed with atomic save (write-temp-then-rename)
and lives under the XDG data dir by default. Actual build/install is
delegated to `dkms(8)` — this component owns the state database.

## Features

- **Module registry**: add/remove modules with validation
- **Per-kernel status**: set/query build status for each kernel release
- **Gap detection**: `missing_for_kernel` lists modules not built or
  installed for a given release (failed and absent both count as
  missing)
- **Persistence**: `save`/`load` JSON roundtrip
- **Tests**: 3 unit tests cover the module lifecycle, per-kernel
  status semantics, `missing_for_kernel`, and persistence

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-dkms)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
