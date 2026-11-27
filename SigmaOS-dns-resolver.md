# SigmaOS-dns-resolver

> **Category:** Networking | **Language:** Rust | **License:** GPL-3.0-or-later

Declarative DNS resolver configuration with split-horizon (private/public zone separation) and DNS-over-TLS (DoT) upstream support. Manages zone configs and record sets in memory; designed for integration with the SigmaOS network stack via `SigmaOS-network-manager`.

## Key Types

| Type | Description |
|------|-------------|
| `RecordType` | `A`, `AAAA`, `CNAME`, `MX`, `TXT` |
| `DnsRecord` | name, kind, value, TTL |
| `ZoneConfig` | Domain zone with records + optional DoT upstream |
| `Resolver` | Multi-zone registry with resolve-by-name lookup |

## Split-Horizon Example

```toml
# /etc/sigma/dns.toml
[[zone]]
domain = "sigmaos.internal"
dot_upstream = "tls://1.1.1.1"

[[zone.record]]
name = "gateway"
type = "A"
value = "192.168.1.1"
ttl = 60
```

## Tests (6 AAA)
- `test_add_a_record_and_resolve_aaa`
- `test_missing_record_returns_none_aaa`
- `test_dot_upstream_set_aaa`
- `test_zone_count_aaa`
- `test_cname_record_type_aaa`
- `test_ttl_zero_allowed_aaa`

## See Also
- [SigmaOS-network-manager](SigmaOS-network-manager)
- [SigmaOS-time-sync](SigmaOS-time-sync)
- [SigmaOS-pf-firewall](SigmaOS-pf-firewall)
