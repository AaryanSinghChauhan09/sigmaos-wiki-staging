# SigmaOS BI Analytics

Business-intelligence metrics and dashboards for SigmaOS — define metrics over JSON record datasets, compute aggregations, and render dashboards. Safe Rust, serde-based.

## Capabilities

- `Metric` definitions: field + aggregation (`count`/`sum`/`avg`/`min`/`max`), optional `group_by`, optional field/value filter
- `compute()` returns `Scalar` or `Grouped` results; group keys are unquoted strings (commit `07ecb6b` fixed keys rendering as `"us"`)
- `Dashboard`/`Widget` model with `save_dashboard`/`load_dashboard` JSON persistence and `render_widget` text output
- CLI: `metric <dataset> <field> --agg --group-by`, `dashboard <file>`, `inspect <dataset>`
- 5 unit tests covering aggregations, group-by, filters, error paths, and round-trips

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-bi-analytics)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
