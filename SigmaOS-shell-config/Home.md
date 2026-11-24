# SigmaOS Shell Config

Shell configuration management for SigmaOS, providing unified zsh and bash configuration with enhanced productivity features.

## Overview

SigmaOS Shell Config provides a unified shell configuration for zsh and bash with enhanced productivity features, aliases, and tools integration.

## Features

- **Enhanced zsh**: Larger history, better completion, AUTO_PUSHD
- **Aliases**: Git, tmux, and productivity aliases
- **Tools integration**: eza, zoxide, fzf, starship
- **Fuzzy search**: fzf history search and file navigation
- **Smart prompts**: Starship prompt with SigmaOS theme
- **Directory jumping**: zoxide for intelligent directory navigation

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
