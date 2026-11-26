# SigmaOS Shell Config

Declarative manager for the SigmaOS desktop shell (Quickshell-based):
bar, dock, launcher, and theme configuration as validated TOML.

## Capabilities

- `ShellConfig` model: `bar` (position/height/modules/autohide),
  `dock` (position/icon size/pinned apps), `launcher`
  (provider/max results/fuzzy), `theme` (#RRGGBB colors + font)
- Strict validation: bar height 1–200, icon size 1–256, hex colors
  must be `#RRGGBB` with valid digits, launcher results 1–500
- `sigmaos-system-profile`-style subcommands: `validate`, `default`,
  `apply` (atomic write to `~/.config/sigmaos/shell.toml`), `path`
- `module <name> on|off` toggles a bar module in the user config —
  Omarchy-style live shell customization
- `ShellConfig::set_module_enabled` for programmatic edits

## Structure

- `src/lib.rs` - config model, validation, defaults, apply
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

5 unit tests (hex color validation, module toggling, range checks, TOML roundtrip, malformed-input rejection).

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-shell-config)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
