# SigmaOS KDE Connect

KDE Connect integration for SigmaOS - device integration and file sharing.

## Overview

SigmaOS KDE Connect provides device integration and file sharing between devices. Integration with SigmaOS communication and file sharing systems.

## Features

- **Device pairing**: Pair devices
- **File sharing**: Share files between devices
- **Clipboard sync**: Sync clipboard
- **Notifications**: Notification sync
- **Media control**: Media playback control
- **Themes**: SigmaOS theme integration
- **Security**: SigmaOS security integration
- **Documentation**: Comprehensive documentation

## Installation

```bash
sudo pacman -S sigmaos-kde-connect
```

## Configuration

KDE Connect is configured to use the SigmaOS theme system. Configuration is stored in `~/.config/kdeconnect/`.

## Usage

```bash
# Start KDE Connect
sigmaos-kde-connect

# Pair a device
kdeconnect-cli --pair device-id

# Share a file
kdeconnect-cli --share-file file.txt device-id
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-kde-connect)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
