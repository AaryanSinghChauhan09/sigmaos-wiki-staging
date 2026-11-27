# SigmaOS-time-sync

> **Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later

NTP/PTP time synchronization daemon for SigmaOS. Manages multiple time sources with stratum-aware selection, records offset samples in a ring buffer, and computes a rolling mean offset for drift correction. Supports marking a preferred source (e.g., local PTP grandmaster) that overrides stratum ordering.

## Key Types

| Type | Description |
|------|-------------|
| `SyncProtocol` | `Ntp` or `Ptp` |
| `TimeSource` | Host, protocol, stratum, preferred flag |
| `SyncSample` | Offset in milliseconds + source label |
| `TimeManager` | Manages sources, ring-buffer history, mean offset computation |

## Source Selection Algorithm

```
1. If any source has preferred=true → use it
2. Otherwise → pick source with lowest stratum
```

## Ring Buffer

The sample history has a configurable capacity. When full, the oldest sample is evicted (FIFO). The mean offset is computed over the current window for use in clock slewing.

## Tests (6 AAA)
- `test_add_source_and_count_aaa`
- `test_mean_offset_no_samples_returns_none_aaa`
- `test_mean_offset_computed_correctly_aaa`
- `test_capacity_ring_buffer_aaa`
- `test_preferred_source_wins_aaa`
- `test_lowest_stratum_chosen_when_no_preferred_aaa`

## See Also
- [SigmaOS-network-manager](SigmaOS-network-manager)
- [SigmaOS-dns-resolver](SigmaOS-dns-resolver)
- [SigmaOS-audit-log](SigmaOS-audit-log)
