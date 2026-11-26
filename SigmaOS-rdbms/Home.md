# SigmaOS RDBMS

Database interoperability primitives for SigmaOS — SQL identifier quoting per dialect and libpq-style connection-string parsing/building. Safe Rust, no unsafe code.

## Capabilities

- `quote_ident`/`quote_qualified`: per-dialect quoting — Postgres/Standard `"..."`, MySQL `` `...` ``, SQL Server `[...]` — with correct embedded-delimiter escaping and NUL/empty rejection
- `parse_conn_string`: libpq `key=value` pairs with single-quote values (`''` escape), `host`/`port`/`dbname`|`database`/`user`/`password` keys plus verbatim extras
- `build_conn_string`: serializes `ConnParams` back to `key=value` form
- 7 unit tests covering dialects, escapes, aliases, and round-trips (commit `c5ad6f2`)

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-rdbms)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
