# SigmaOS Notebooks

Dependency-free `.ipynb` (Jupyter notebook) parser and inspector for SigmaOS — parses notebook JSON with a minimal hand-rolled JSON parser (no serde), extracts cells, and reports statistics.

## Capabilities

- `parse_notebook()` parses nbformat JSON into typed cells (`code`, `markdown`, `raw`) with execution counts
- `Notebook::counts()`, `line_count()`, `code_source()`, and `source_of(CellType)` for export/lint
- CLI `sigmaos-notebooks <file.ipynb> [--code|--markdown|--stats]` — default prints cell counts and line totals; `--code`/`--markdown` dump concatenated cell sources (commit `2053532`)
- `#![forbid(unsafe_code)]`, 4 unit tests covering parsing, cell separation, and escape/unicode handling

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-notebooks)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
