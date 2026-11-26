# SigmaOS Dots

Shared user dotfiles and shell configs for SigmaOS: starship, tmux, git, mise, shared bash/zsh shell config, fish config, zsh templates, and helper scripts. Consolidates the former `SigmaOS-fish` and `SigmaOS-zsh` split repos.

## Capabilities

- Component implementation lives in `SigmaOS-dots`
- `install.sh` copies `config/` to `~/.config` and `bin/` to
  `~/.local/bin`, then writes shell rc files for zsh/bash (fish uses
  the installed `~/.config/fish`). LazyVim is **opt-in** via
  `--with-lazyvim` — it is no longer cloned (or `~/.config/nvim`
  removed) on a plain install (commit `67b4e4b`).
- See the repository README for usage, screenshots, and component-specific details

## Interconnectivity

| Repo | Relationship |
|------|-------------|
| `Sigma` | Main SigmaOS release and integration surface |
| `SigmaOS-ISO` | Bootable ISO / desktop image |
| `SigmaOS-config-system` | Shared declarative configuration patterns |

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-dots)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
