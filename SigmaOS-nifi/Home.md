# SigmaOS Apache NiFi

Apache NiFi integration for SigmaOS - automated data flow platform.

## Overview

SigmaOS Apache NiFi provides an automated data flow platform for data routing, transformation, and system mediation logic.

## Features

- **Flow-based programming**: Visual data flow design
- **Processors**: Extensive processor library
- **Data provenance**: Track data lineage
- **Security**: Multi-tenant authorization
- **Site-to-site**: Secure data transfer
- **Monitoring**: Real-time flow monitoring
- **Templates**: Reusable flow templates
- **Clustering**: Distributed processing

## Installation

```bash
sudo pacman -S sigmaos-nifi
```

## Configuration

NiFi is configured to use the SigmaOS configuration system. Edit `/etc/sigmaos/nifi/nifi.properties` for customization.

## Usage

```bash
# Start NiFi
sudo systemctl start sigmaos-nifi

# Enable on boot
sudo systemctl enable sigmaos-nifi

# Access web interface
http://localhost:8080/nifi
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-nifi)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
