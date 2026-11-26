# SigmaOS App Environment

Sandboxed application environment profiles for SigmaOS — env vars, filesystem mounts, network access, and resource hints that render into launch commands.

## Capabilities

- `AppProfile`: command argv, `KEY=VALUE` env map, `Mount`s (ro/rw), network flag, workdir
- `ProfileStore`: add (validates non-empty id + command), get/remove/list, `render_launch` → `LaunchSpec`
- `LaunchSpec::to_shell()` renders `env KEY='quoted' ... cmd args` with proper single-quote escaping (commit `e147048` added tests covering quoting edge cases)
- `save`/`load` atomic JSON persistence; `builtin_profiles()` seeds browser/terminal/files
- 5 unit tests; `#![forbid(unsafe_code)]`

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-app-env)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
