# SigmaOS-wayland-portal

**Category:** Desktop  
**License:** GPL-3.0-or-later  
**Rolling release:** Yes

Sandboxed desktop portal. Applications inside SigmaOS jails communicate with the portal broker instead of accessing system resources directly.

## Supported Interfaces

| Request | Description |
|---------|-------------|
| `FileChooser` | Show a file picker dialog |
| `Notification` | Post a system notification |
| `ScreenCapture` | Request a screen capture session |
| `ClipboardRead` | Read clipboard content |

## Tests: 6 AAA

## See Also
- [SigmaOS-jails](SigmaOS-jails)
- [SigmaOS-pledge-caps](SigmaOS-pledge-caps)
- [SigmaOS-pf-firewall](SigmaOS-pf-firewall)
