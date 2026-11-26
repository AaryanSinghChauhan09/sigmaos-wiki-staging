# SigmaOS Configuration System

Typed, validated system configuration — a NixOS-inspired `Config`
model covering desktop, window manager, terminal, shell, network,
power, accessibility, performance, security, updates, and logging.

## Capabilities

- `Config` schema with per-section structs and secure defaults
  (`apply_defaults` fills theme/WM/shell/terminal)
- `ConfigValidator` — per-section checks: font sizes, transparency/
  opacity 0–1, WM/shell type allowlists, power profiles, log levels,
  update channels, and "at least one of SELinux/AppArmor" for security
- Dotted-key get/set: `desktop.theme`, `window_manager.gaps`,
  `updates.check_interval`, … via `set_value`/`get_value`
- `ConfigManager` + `ConfigLoader` for file load/validate/generate

## Commands

```bash
sigmaos-config load [--file F] [--config-dir D]
sigmaos-config validate --file F
sigmaos-config generate [--output DIR]
sigmaos-config show [--file F]
sigmaos-config set <section.key> <value> [--file F]
sigmaos-config get <section.key> [--file F]
```

## Structure

- `src/schema.rs` - Config model, defaults, dotted-key accessors
- `src/validator.rs` - per-section validation rules
- `src/config.rs` / `loader.rs` - manager + TOML loader
- `src/main.rs` - CLI entry point

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

6 unit tests (defaults validate, set/get round-trip, invalid key/value
rejection, validator range/security rules).

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-config-system)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
