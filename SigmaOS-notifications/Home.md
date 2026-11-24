# SigmaOS Notifications

Unified notification daemon with urgency levels and action support for SigmaOS.

## Overview

SigmaOS Notifications is a notification daemon that provides desktop notification capabilities following the freedesktop.org notification specification. It supports urgency levels, action buttons, and integrates with the SigmaOS desktop environment.

## Features

- **Unified daemon**: Single notification daemon for all applications
- **Urgency levels**: Low, normal, critical notification priorities
- **Action support**: Interactive notification buttons
- **libnotify compatible**: Standard freedesktop.org notification API
- **Theme integration**: Follows SigmaOS theme for notification appearance
- **Sound support**: Notification sounds with optional mute

## Usage

Applications send notifications using libnotify or the D-Bus notification API:

```bash
notify-send "Title" "Message"
```

## Integration

Works with:
- SigmaOS Notification Center (Quickshell plugin)
- Desktop applications (libnotify-based)
- System services (systemd timers, etc.)

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

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-notifications)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
