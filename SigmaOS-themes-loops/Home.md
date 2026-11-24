# SigmaOS Themes Loops

The live background loops for the built-in SigmaOS themes: a quiet version of a theme's still that keeps moving, which the SigmaOS desktop plays in the still's place while animations are on.

## Overview

The loops ship as the `sigmaos-themes-loops` package, which installs `<theme>/<name>.mp4` to `/usr/share/sigmaos/themes/<theme>/backgrounds/loops/<name>.mp4`.

## How Loops Work

A loop plays in place of the still with the same name in that theme's `backgrounds/` in the SigmaOS desktop, so `lumon/01-united-in-severance.mp4` belongs to `themes/lumon/backgrounds/01-united-in-severance.webp`. Its first frame is that still and its last frame leads straight back into it.

## Loop Requirements

The `bin/check` script holds every loop to the format the SigmaOS desktop asks for, so the hand-over from the still and each restart stay seamless:

- H.264 with no B-frames
- One keyframe
- Colour tags
- Twenty seconds or less
- The still's shape at no larger than its size

## Add or Change a Loop

To add or change a loop, open a pull request in this repository. Once it merges, cut a release tagged with the date, `vYYYY.MM.DD` (or `vYYYY.MM.DD.1` for a second one that day). The SigmaOS package repository picks the release up and updates `sigmaos-themes-loops` to it.

## Available Themes

This repository includes loops for the following built-in SigmaOS themes:

- catppuccin
- catppuccin-latte
- hackerman
- lumon
- ristretto
- rose-pine
- vantablack
- white

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-themes-loops)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
