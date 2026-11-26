# SigmaOS GenOffice

Offline-capable document suite integration layer for SigmaOS —
a document model covering ODF, OOXML, PDF, Markdown, HTML, CSV/TSV,
and SVG, plus an app registry for the suite's components.

## Capabilities

- `DocumentFormat` — Odf, Ooxml, Pdf, Markdown, Html, Csv, Svg with
  `mime_type()` mapping
- `DocumentFormat::from_extension` / `from_path` — format detection
  from file extensions (case-insensitive; `odt/ods/odp` → Odf,
  `docx/xlsx/pptx` → Ooxml, etc.)
- `GenOfficeDocument` — path, format, title, `offline_ready` flag for
  documents verified to work without network access
- `GenOfficeSuite` — registry of suite app names (`register_app`,
  `has_app`, `apps`)

## Build & Test

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
cargo fmt --check
```

6 tests covering mime types, format detection, and suite registry.

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-genoffice)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
