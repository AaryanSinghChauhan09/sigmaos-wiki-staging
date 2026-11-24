# SigmaOS Podman

Podman integration for SigmaOS - daemonless container engine.

## Overview

SigmaOS Podman provides a daemonless container engine for building, running, and managing containers. Integration with SigmaOS security and theme systems.

## Features

- **Containers**: Application isolation without a daemon
- **Images**: Build and share container images
- **Pods**: Group containers together
- **Rootless**: Run containers without root
- **Compose**: Multi-container applications (podman-compose)
- **Registry**: Private and public registries
- **Volumes**: Data persistence
- **Networks**: Container networking
- **Security**: Rootless containers, AppArmor integration
- **Logging**: Integration with SigmaOS logging
- **Docker compatibility**: Drop-in replacement for Docker

## Installation

```bash
sudo pacman -S sigmaos-podman
```

## Configuration

Podman is configured to use SigmaOS security policies. Edit `/etc/containers/containers.conf` for customization.

## Usage

```bash
# Run a container
podman run hello-world

# Build an image
podman build -t myapp .

# List containers
podman ps

# List images
podman images

# Start a pod
podman pod create --name mypod
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-podman)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
