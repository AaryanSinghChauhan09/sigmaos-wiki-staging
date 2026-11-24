# SigmaOS Raven

Raven integration for SigmaOS - Windows application runner.

## Overview

SigmaOS Raven provides a tool for running Windows applications on Linux. Integration with SigmaOS theme system and security policies.

## Features

- **Windows apps**: Run Windows applications
- **Wine integration**: Built on Wine
- **App management**: Manage Windows applications
- **Dependency installation**: Install Windows dependencies
- **Themes**: SigmaOS theme integration
- **Performance**: Optimized for performance
- **Security**: Sandboxed execution
- **Sharing**: Share applications with other users

## Installation

```bash
sudo pacman -S sigmaos-raven
```

## Configuration

Raven is configured to use the SigmaOS theme system. Applications are stored in `~/Raven/`.

## Usage

```bash
# Start Raven
sigmaos-raven

# Install a Windows app
raven install app.exe

# Run a Windows app
raven run app.exe
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-raven)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
