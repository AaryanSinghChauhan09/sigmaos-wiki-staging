# SigmaOS-telemetry-local

> **Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later

Zero-exfiltration, 100% local-only system metrics and anomaly ring buffer for SigmaOS (`#![forbid(unsafe_code)]`). Never opens network sockets; stores bounded metric samples locally and flags threshold anomalies for operator inspection.

## Key Types

| Type | Description |
|------|-------------|
| `MetricPoint` | Metric name, floating-point value, Unix timestamp (seconds) |
| `LocalTelemetry` | Bounded FIFO ring buffer with threshold anomaly query |

## Tests (6 AAA)
- `test_record_and_latest_aaa`
- `test_anomaly_detection_above_threshold_aaa`
- `test_ring_evicts_oldest_at_capacity_aaa`
- `test_latest_missing_metric_returns_none_aaa`
- `test_no_anomalies_when_below_threshold_aaa`
- `test_zero_capacity_clamped_to_one_aaa`

## See Also
- [SigmaOS-audit-log](SigmaOS-audit-log)
- [SigmaOS-service-supervisor](SigmaOS-service-supervisor)
- [SigmaOS-process-manager](SigmaOS-process-manager)
