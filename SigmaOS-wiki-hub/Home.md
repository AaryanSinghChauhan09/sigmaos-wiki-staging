# SigmaOS Wiki Hub

Searchable documentation index for SigmaOS — scans a tree of markdown
files and builds a categorized, full-text-searchable index with JSON
export.

## Overview

`SigmaOS-wiki-hub` walks a directory for `.md` files (no symlink
following) and builds a `WikiIndex` of `WikiPage`s: title extracted
from the first `# ` heading (filename fallback), category from the
first directory under the root (`general` for root-level files), and
full content. Pages sort by title. The index saves/loads as JSON
under the XDG cache dir.

## Features

- **Indexing**: recursive markdown scan with title/category extraction
- **Search**: case-insensitive substring match over title + content
- **Grouping**: `by_category` into a sorted map; `toc` renders a
  markdown table of contents
- **Persistence**: `save`/`load` JSON roundtrip
- **Tests**: 5 unit tests cover markdown-only indexing, title
  fallback, search, category grouping, toc, and persistence — and
  caught a real bug where root-level files were categorized by their
  own filename instead of `general`

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-wiki-hub)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
