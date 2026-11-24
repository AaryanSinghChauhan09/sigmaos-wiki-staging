# SigmaOS Wine

Wine integration for SigmaOS - Windows compatibility layer.

## Overview

SigmaOS Wine provides a compatibility layer for running Windows applications on Linux. Integration with SigmaOS theme system and security policies.

## Features

- **Windows apps**: Run Windows applications
- **Compatibility**: Wide application compatibility
- **Wine prefix**: Manage Windows environments
- **Themes**: SigmaOS theme integration
- **Performance**: Optimized for performance
- **Dependencies**: Automatic dependency installation
- **Registry**: Windows registry emulation
- **DLL overrides**: Override Windows DLLs

## Installation

```bash
sudo pacman -S sigmaos-wine
```

## Configuration

Wine is configured to use SigmaOS security policies. Wine prefixes are stored in `~/.wine/`.

## Usage

```bash
# Run a Windows app
wine app.exe

# Create a new prefix
WINEPREFIX=~/.wine-custom wineboot

# Run with specific prefix
WINEPREFIX=~/.wine-custom wine app.exe
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-wine)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
