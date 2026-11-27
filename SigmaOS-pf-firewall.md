# SigmaOS-pf-firewall

**Category:** Security  
**License:** GPL-3.0-or-later  
**Rolling release:** Yes

Declarative stateful packet filter and default-deny network policy engine for SigmaOS. Provides rule-based traffic control with priority ordering and stateful connection tracking.

## Rule Model

- `FirewallRule { priority, direction, proto, port, action }`
- Actions: `Allow`, `Deny`
- Directions: `Inbound`, `Outbound`
- Default policy: **Deny all inbound, allow all outbound**

## Tests: 4 AAA

## See Also
- [SigmaOS-jails](SigmaOS-jails)
- [SigmaOS-pledge-caps](SigmaOS-pledge-caps)
- [SigmaOS-wayland-portal](SigmaOS-wayland-portal)
