# SigmaOS Calc

A dead-simple calculator built with Qt Quick and C++ that automatically follows the SigmaOS theme and system dark/light mode.

## Overview

The keypad covers the basics: the four arithmetic operators with the usual precedence (`×` and `÷` before `+` and `−`), decimals, percent, sign toggle, and backspace. The expression builds up above the display and stays visible with the result after `=`, so `42 × 3 + 7` reads back exactly as it was entered.

## Features

- **Expression display**: Shows the full expression above the result
- **Thousands separators**: Numbers are grouped as you type (e.g., `1,234,567.89`)
- **Power operator**: `^` raises to a power ahead of everything else
- **Percent convention**: With `+` or `−` it takes that percentage of the running total (`200 + 10 % = 220`); with `×`, `÷`, or `^` it simply divides by 100
- **Keyboard support**: Full keyboard support including numpad

## Keyboard Shortcuts

- `0-9`, `.`, `+`, `-`, `*` or `x`, `/`, `^`, `%`: Enter digits and operators
- Numpad enters digits whether or not NumLock is on
- `Enter` or `=`: Calculate
- `Backspace`: Delete last digit
- `C` or `Escape`: Clear
- `S`: Toggle sign
- `Ctrl+C` or `Super+C`: Copy result (without separators)
- `Ctrl+V` or `Super+V`: Paste number (with or without separators)

## Theme Integration

Colors follow the current SigmaOS theme and re-tint live when the theme changes. Text follows the desktop text size (`sigmaos display text size`, or GNOME's `text-scaling-factor`).

## Requirements

- Qt 6: `qt6-base`, `qt6-declarative`
- `xdg-desktop-portal` and a portal backend

## Font

The iA Writer Mono font is bundled under the SIL Open Font License 1.1. The font is copyright Information Architects Inc. and based on IBM Plex, copyright IBM Corp.

## Development

`bin/build` compiles `build/sigmaos-calc` with CMake, and `bin/test` builds and runs the tests offscreen. Building needs `cmake`, `make`, and a C++ compiler on top of the Qt packages.

## License

MIT

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-omacalc)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
