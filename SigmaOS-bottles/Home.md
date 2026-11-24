# SigmaOS Bottles

Bottles integration for SigmaOS - Windows application runner.

## Overview

SigmaOS Bottles provides a tool for running Windows applications on Linux using Wine. Integration with SigmaOS theme system and security policies.

## Features

- **Windows apps**: Run Windows applications
- **Wine integration**: Built on Wine
- **Bottle management**: Manage isolated environments
- **Dependency installation**: Install Windows dependencies
- **Themes**: SigmaOS theme integration
- **Performance**: Optimized for performance
- **Security**: Sandboxed execution
- **Sharing**: Share bottles with other users

## Installation

```bash
sudo pacman -S sigmaos-bottles
```

## Configuration

Bottles is configured to use the SigmaOS theme system. Bottles are stored in `~/Bottles/`.

## Usage

```bash
# Start Bottles
sigmaos-bottles

# Create a new bottle
bottles create

# Run a Windows app
bottles run app.exe
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-bottles)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
