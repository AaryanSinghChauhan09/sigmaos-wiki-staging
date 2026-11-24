# SigmaOS-shell-config

SigmaOS-shell-config is a component of the SigmaOS operating system project that provides shell configuration management.

## Structure

- `src/lib.rs` - library implementation
- `src/main.rs` - CLI entry point
- `docs/` - architecture, principles, testing, security docs
- `COMPONENT.tomL` - component manifest
- `tools-sigmaos.sh` - interconnect helper

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-shell-config)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
