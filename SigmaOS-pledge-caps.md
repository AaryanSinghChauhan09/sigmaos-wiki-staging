# SigmaOS-pledge-caps

**Category:** Security  
**License:** GPL-3.0-or-later  
**Rolling release:** Yes

Declarative capability-based privilege reduction. After initialization, a process declares the minimum `Cap` set it requires. All other capabilities are dropped irrevocably — inspired by OpenBSD's `pledge()`, expressed as a pure SigmaOS-native API.

## Capabilities

| Cap | Meaning |
|-----|---------|
| `FileRead` | Open and read files |
| `FileWrite` | Create, write, or unlink files |
| `NetOutbound` | Open outbound network connections |
| `NetInbound` | Accept inbound connections |
| `Exec` | Spawn child processes |
| `BindPrivilegedPort` | Bind to ports < 1024 |
| `SetClock` | Modify the system clock |
| `KernelModules` | Load/unload kernel modules |
| `SetId` | Change process UID/GID |

## Tests: 5 AAA

## See Also
- [SigmaOS-jails](SigmaOS-jails)
- [SigmaOS-pf-firewall](SigmaOS-pf-firewall)
- [SigmaOS-atomic-root](SigmaOS-atomic-root)
