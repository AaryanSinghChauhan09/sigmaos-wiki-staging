# SigmaOS-network-filter

**Category:** Networking | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Stateless packet filter rule engine for SigmaOS. Implements an ordered, first-match rule evaluation model for TCP/UDP/ICMP/Any packets with Allow/Deny/Log actions — suitable as a policy layer above `SigmaOS-pf-firewall`.

## Features

- **Ordered rule evaluation** — first matching rule wins (Cisco/iptables semantics)
- **Protocol-aware matching** — `Proto::Any` wildcard or exact proto match
- **Port filtering** — optional src/dst port constraints per rule
- **Three actions** — `Allow`, `Deny`, `Log`
- **Default-allow** — no matching rule = implicit Allow

## API

| Function | Description |
|---|---|
| `add_rule(rule)` | Add an ordered filter rule |
| `remove_rule(id)` | Remove rule by ID |
| `evaluate(packet)` | Evaluate packet, return matched Action |
| `rule_count()` | Number of active rules |

## Errors

| Error | Condition |
|---|---|
| `DuplicateRule(id)` | Rule ID already exists |
| `RuleNotFound(id)` | Remove of non-existent rule |

## Tests

6 AAA unit tests covering: deny-rule blocks match, proto mismatch allows, empty-filter default-allow, removed-rule falls through, duplicate-id rejection, log-rule matches any.

## See Also

- [SigmaOS-pf-firewall](SigmaOS-pf-firewall) — stateful packet filter
- [SigmaOS-dns-resolver](SigmaOS-dns-resolver) — DNS resolution
- [SigmaOS-process-isolator](SigmaOS-process-isolator) — process namespace isolation
