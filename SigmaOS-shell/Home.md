# SigmaOS Shell

The Quickshell/QML desktop shell providing bar, dock, launcher, and notifications for the SigmaOS Hyprland session.

## Components

- **Bar** — top panel with workspace switcher, clock, system tray, battery, network modules
- **Dock** — pinned application launcher with running indicators
- **Launcher** — fuzzy application search via `.desktop` entry scanning
- **NotificationCenter** — transient toast notifications with auto-dismiss
- **Theme** — color/font token singleton matching `sigmaos-shell-config`
- **ConfigStore** — watches `~/.config/sigmaos/shell.toml` for live reload
- **AppIndex** — scans user/system/flatpak `.desktop` files

## Interconnectivity

| Repo | Relationship |
|------|-------------|
| `sigmaos-shell-config` | Writes `shell.toml` consumed by ConfigStore |
| `sigmaos-hyprland` | Window manager bindings (workspaces, dispatch) |
| `sigmaos-notification-center` | Notification backend via Quickshell `NotificationServer` |
| `sigmaos-live-media` | Wallpaper surface behind the shell |
| `sigmaos-quickshell` | QML runtime that hosts this shell |

## Configuration

`~/.config/sigmaos/shell.toml` — bar position/height/modules, dock pins, launcher settings, theme tokens, keybindings.

## Principles

- Each widget has single responsibility (KISS/SRP)
- Config injection via `required property var config` (DIP/ISP)
- Loose coupling between shell and config service
- Secure defaults; no hardcoded paths outside `~/.config/sigmaos/`
