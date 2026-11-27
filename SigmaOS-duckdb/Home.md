# SigmaOS-duckdb

DuckDB integration layer — query planner wrappers and embedded analytics in Rust for SigmaOS.

## Overview

`SigmaOS-duckdb` provides typed query plan construction, schema validation, SQL rendering, and cost estimation for embedded analytical queries.

## Features

- `AnalyticsSession` for registering table schemas and validating query plans
- `QueryPlan` builder with projections, filters, `GROUP BY`, `ORDER BY`, and `LIMIT`
- Identifier sanitization and deterministic SQL generation

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-duckdb)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
