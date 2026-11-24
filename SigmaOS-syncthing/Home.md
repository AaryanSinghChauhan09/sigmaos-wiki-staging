# SigmaOS Syncthing

Syncthing integration for SigmaOS - continuous file synchronization.

## Overview

SigmaOS Syncthing provides continuous file synchronization between devices. Peer-to-peer synchronization with SigmaOS integration.

## Features

- **Continuous sync**: Automatic file synchronization
- **Peer-to-peer**: Direct device-to-device sync
- **Encrypted**: End-to-end encryption
- **Cross-platform**: Works across platforms
- **Selective sync**: Choose which folders to sync
- **Versioning**: Keep old versions of files
- **Web UI**: Web-based management interface
- **Themes**: SigmaOS theme integration for web UI
- **Discovery**: Automatic device discovery
- **Relay server**: Relay for NAT traversal

## Installation

```bash
sudo pacman -S sigmaos-syncthing
```

## Configuration

Syncthing is configured to use the SigmaOS theme system. Configuration is stored in `~/.config/syncthing/`.

## Usage

```bash
# Start Syncthing
sudo systemctl start syncthing@user

# Enable on boot
sudo systemctl enable syncthing@user

# Access web interface
http://localhost:8384
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-syncthing)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
