# SigmaOS Docker

Docker integration for SigmaOS - container platform for application isolation and deployment.

## Overview

SigmaOS Docker provides container platform capabilities for building, shipping, and running applications in containers. Integration with SigmaOS package management and security.

## Features

- **Containers**: Application isolation
- **Images**: Build and share container images
- **Compose**: Multi-container applications
- **Registry**: Private and public registries
- **Volumes**: Data persistence
- **Networks**: Container networking
- **Security**: Rootless containers, AppArmor integration
- **Logging**: Integration with SigmaOS logging

## Installation

```bash
sudo pacman -S sigmaos-docker
```

## Configuration

Docker is configured to use SigmaOS security policies. Edit `/etc/docker/daemon.json` for customization.

## Usage

```bash
# Start Docker
sudo systemctl start docker

# Enable on boot
sudo systemctl enable docker

# Run a container
docker run hello-world

# Build an image
docker build -t myapp .
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-docker)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
