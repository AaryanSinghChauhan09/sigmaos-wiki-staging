# SigmaOS-telemetry-exporter

**Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

Local-only OpenMetrics / Prometheus text exporter for SigmaOS telemetry. Formats counters and gauges deterministically for local observability without any external network phone-home.

## Features

- **Typed metrics** — enforces `Counter` (non-negative) and `Gauge` (signed float) invariants
- **Strict metric naming** — validates ASCII alphanumeric + underscore identifiers
- **Deterministic OpenMetrics output** — sorted `# HELP`, `# TYPE`, sample lines, and `# EOF` trailer

## API

| Function | Description |
|---|---|
| `record(sample)` | Validate and store a counter or gauge sample |
| `metric_count()` | Number of distinct registered metrics |
| `render_openmetrics()` | Render all metrics in OpenMetrics text format |

## Tests

6 AAA unit tests covering: counter OpenMetrics formatting, negative counter rejection, negative gauge acceptance, invalid metric name rejection, metric overwrite, empty EOF output.

## See Also

- [SigmaOS-telemetry-local](SigmaOS-telemetry-local) — local telemetry collector
- [SigmaOS-oom-guardian](SigmaOS-oom-guardian) — OOM policy guard
- [SigmaOS-service-supervisor](SigmaOS-service-supervisor) — service supervision
