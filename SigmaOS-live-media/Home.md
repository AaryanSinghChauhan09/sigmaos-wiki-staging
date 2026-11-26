# SigmaOS Live Media

Live wallpaper / animated background manager for the SigmaOS desktop —
declarative TOML config, atomic apply, battery-saver pause policy.

## Overview

`SigmaOS-live-media` manages animated wallpapers of four kinds:
`video` (mp4/webm), `shader` (GLSL), `sequence` (image frame
directory), and `image` (static fallback). A `LiveMediaConfig` lists
wallpapers with per-entry `Playback` options (loop, volume,
pause-on-battery). Config is TOML, validated on load (non-empty
list, known active wallpaper, non-empty names), and `apply` writes it
atomically (temp file + rename) to the XDG config dir.

## Features

- **Validation**: rejects empty wallpaper lists, unknown `active`
  names, and empty wallpaper names
- **Path resolution**: relative media paths join `wallpapers_dir`,
  absolute paths pass through
- **Persistence**: `to_toml`/`load`/`apply` roundtrip
- **Tests**: 4 unit tests cover validation, resolution, and the
  TOML/apply/load roundtrip

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-live-media)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
