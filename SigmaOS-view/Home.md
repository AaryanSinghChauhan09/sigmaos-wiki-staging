# SigmaOS-view

> Part of [SigmaOS](https://github.com/AaryanSinghChauhan09) — a modular, rolling-release operating system.

## Overview
SigmaOS's picture viewer and media player, listed in the launcher as Media Viewer. Open a photo, a video or a song, or a whole folder, and look at it: the controls along the bottom and the title across the top, or nothing but the picture once Tab puts them away. Step through a folder with the arrows, zoom with the wheel, and watch the clips between the photos in the same window.

## Architecture
- **Language / Runtime:** `multi-language` (Tier: `standard`, Stability: `active`)
- **Repository Layout:** `CMakeLists.txt`, `bin/`, `plans/`, `screenshots/`, `share/`, `src/`, `tests/`

## Design Principles
- **Single Responsibility & Modularity:** Scoped as an independent SigmaOS component repository with explicit contracts.
- **SOLID & Clean Code:** Follows DRY, KISS, YAGNI, defensive programming, and secure defaults.
- **Rolling Release:** Continuously integrated with no static version release tags.

## CLI Reference
Library / configuration component (no standalone CLI binary declared; see `src/lib.rs` or repository scripts).

## Configuration
Component metadata is declared in `COMPONENT.toml`:
- `component.name` = `sigmaos-view`
- `component.id` = `sigmaos-view`
- `component.kind` = `component`
- `component.license` = `GPL-3.0-or-later`
- `component.metadata.category` = `sigmaos`
- `component.metadata.branch` = `main`
- `component.metadata.docs` = `github-wiki`

## Dependencies
C++17 / CMake / Qt6 toolchain (see `CMakeLists.txt`).

## Testing
Verify component integrity and scripts in the repository root:

```sh
# Check repository scripts and configuration
ls -la
```

## Contributing
See [SigmaOS Development Guidelines](../Development-Guidelines)
