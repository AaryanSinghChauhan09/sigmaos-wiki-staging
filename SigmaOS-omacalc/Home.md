# SigmaOS Omacalc

> Forked from omacom/omacalc (MIT). See SIGMAOS_FORK.md.

A dead-simple calculator built with Qt Quick and C++ that automatically follows the SigmaOS theme and system dark/light mode.

## Install

Install via the SigmaOS Package Repository via the `omacalc` package.

## Usage

The keypad covers the basics: the four arithmetic operators with the usual
precedence (`×` and `÷` before `+` and `−`), decimals, percent, sign toggle,
and backspace. The expression builds up above the display and stays visible
with the result after `=`, so `42 × 3 + 7` reads back exactly as it was entered.
From the keyboard, `^` raises to a power ahead of everything else, so
`2 × 3 ^ 2` gives `18`.

Numbers are grouped with thousands separators as you type, in the display and
the expression line alike, so `1234567.89` reads as `1,234,567.89`. The
fraction is left ungrouped.

Percent follows the familiar calculator convention: with a pending `+` or `−`
it takes that percentage of the running total (`200 + 10 % =` gives `220`),
while with `×`, `÷`, or `^` - or on its own - it simply divides by 100.

Everything works from the keyboard too:

- `0-9`, `.`, `+`, `-`, `*` or `x`, `/`, `^`, and `%` enter digits and operators.
  The numpad enters digits whether or not NumLock is on.
- `Enter` or `=` calculates.
- `Backspace` deletes the last digit.
- `C` or `Escape` clears.
- `S` toggles the sign.
- `Ctrl+C` or `Super+C` copies the result, without separators.
- `Ctrl+V` or `Super+V` pastes a number, with or without separators.

Colors follow the current SigmaOS theme (`~/.local/state/sigmaos/current/theme/colors.toml`)
and re-tint live when the theme changes. Text follows the desktop text size -
`sigmaos display text size`, or GNOME's `text-scaling-factor`.

## Requirements

- Qt 6: `qt6-base`, `qt6-declarative`
- `xdg-desktop-portal` and a portal backend

The iA Writer Mono font is bundled under the SIL Open Font License 1.1; see
`fonts/OFL.txt`. The font is copyright Information Architects Inc. and based on
IBM Plex, copyright IBM Corp.

## Development

`bin/build` compiles `build/omacalc` with CMake, and `bin/test` builds and runs the tests offscreen. Building needs `cmake`, `make`, and a C++ compiler on top of the Qt packages above.

## License

MIT

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-omacalc)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
