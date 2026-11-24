# SigmaOS UI

A cross-framework UI kit for apps that look and feel like SigmaOS, in any toolkit. It has three parts:

- **One token contract** ([`spec/tokens.md`](spec/tokens.md)): colors, interactive states, borders, rounding, spacing, type and motion, resolved from the live SigmaOS theme and followed live through theme switches.
- **The same primitives in every framework** ([`spec/components.md`](spec/components.md)): Button, Toggle, TextField, Dropdown, Slider, Card, MenuRow, ConfirmDialog and the rest, with the same names, states and metrics.
- **A way to check they agree** ([`bin/review`](bin/review)): token parity for every theme, plus every gallery section rendered in each framework, side by side.

## Framework Bindings

| Binding | Where | Status |
|---|---|---|
| Qt Quick | [`qt/`](qt) | The SigmaOS shell's own QML kit |
| Rune | [`rune/`](rune) | `sigmaos-rune`: a rune-kit `Kit` built from the live theme |
| GTK 4 / libadwaita | [`gtk/`](gtk) | `libsigmaos-gtk-1`: restyles stock GTK and libadwaita widgets |
| KDE / Qt Widgets | [`kde/`](kde) | `SigmaOSWidgets`: palette, proxy style, KDE color scheme |
| GPUI | [`gpui/`](gpui) | `sigmaos-gpui`: full kit as GPUI elements |
| Ratatui (terminal) | [`tui/ratatui/`](tui/ratatui) | `sigmaos-ratatui`: full kit on the terminal's cell grid |
| Bubble Tea (terminal, Go) | [`tui/bubbletea/`](tui/bubbletea) | Full kit as Lip Gloss-style values |
| Textual (terminal) | [`tui/textual/`](tui/textual) | `SigmaOSApp`: full kit as Textual widgets |
| Electron / web | [`web/`](web) | `@sigmaos/ui`: CSS custom properties, Web Components |
| Tauri | [`web/tauri/`](web/tauri) | `tauri-plugin-sigmaos`: Tauri plugin for theme integration |
| Rust, any framework | [`crates/sigmaos-theme`](crates/sigmaos-theme) | The resolver and watcher, with no UI dependency |
| C, any language | [`crates/sigmaos-theme-ffi`](crates/sigmaos-theme-ffi) | `libsigmaos-theme`: C library for theme resolution |

## Try It

```sh
bin/build
build/qt/sigmaos-qt-gallery                  # follows your theme; switch themes and watch
target/release/sigmaos-rune-gallery
tui/ratatui/target/release/sigmaos-ratatui-gallery   # the terminal kit, in this terminal
build/bubbletea/sigmaos-bubbletea-gallery    # the same on Bubble Tea
build/textual/sigmaos-textual-gallery        # the same kit in Textual
bin/review --open                            # every binding vs Qt, 6 themes × 2 roundings, every section
target/release/sigmaos-theme                 # the resolved tokens as JSON
```

## Use It

It's a library: apps depend on it rather than copying it. Documentation in [`docs/`](docs/README.md) covers each route, with a minimal app, the live theme, previews in other themes, snapshots, pinning and troubleshooting.

## Key Principles

What makes an app read as SigmaOS:

1. **Corners come from Hyprland** (`radius`, usually 0: sharp). Don't round things because they look nicer rounded.
2. **Controls are foreground glass**, not accent-filled: a faint foreground fill and border, stronger under the cursor.
3. **One font**: fontconfig's `monospace`, at the token sizes. Bold only for selection and titles.
4. **Flat**: no drop shadows, no gradients except a theme's border gradient.
5. **Keyboard-first**: every control is focusable, and focus looks like hover.
6. **Follow the theme live**: never cache colors at startup; bindings re-resolve on theme switch.

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-ui)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
