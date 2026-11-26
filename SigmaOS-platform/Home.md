# SigmaOS Platform

Hardware and platform capability detection — reads `/proc`, `/sys`, and
`os-release` to report what the machine can do. Pure safe reads, no
`unsafe`.

## Capabilities

- `detect()` → `PlatformInfo`: OS name/version, kernel release, arch,
  CPU model + core count, total memory, session type (Wayland/X11),
  init system (systemd/runit/sysvinit), hostname, uptime
- `gpu_driver` — DRM driver of the first GPU under `/sys/class/drm`
  (`amdgpu`, `i915`, `nouveau`, …), `None` when no GPU is present
- `cpu_feature(name)` — checks `/proc/cpuinfo` flags (e.g. `avx2`)
- `kernel_supported(release)` — SigmaOS targets kernel ≥ 6.1 LTS
- `memory_human()` — GiB formatting
- `--validate` — installer-style hardware check (≥2 GiB RAM, ≥2 cores,
  `sse4_2`, graphical session, systemd, ≥20 GiB free, kernel ≥ 6.1)
- `--cpu-feature NAME`, `--json` output

## Structure

- `src/lib.rs` - detection logic + tests
- `src/main.rs` - CLI entry point
- `COMPONENT.toml` - component manifest
- `tools-sigmaos.sh` - interconnect helper

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

4 unit tests (kernel boundary checks, memory formatting, cpu_feature vs /proc/cpuinfo, live `detect()`).

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-platform)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
