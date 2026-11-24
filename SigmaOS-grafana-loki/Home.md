# SigmaOS Grafana Loki

Grafana Loki integration for SigmaOS - log aggregation system.

## Overview

SigmaOS Grafana Loki provides a log aggregation system for collecting, storing, and querying logs. Integration with SigmaOS logging and monitoring systems.

## Features

- **Log aggregation**: Collect logs from multiple sources
- **Label-based**: Organize logs with labels
- **Query language**: LogQL for querying
- **Grafana integration**: Native Grafana integration
- **Storage**: Efficient log storage
- **Retention**: Configurable log retention
- **Multi-tenancy**: Support for multiple tenants
- **Performance**: High-performance log processing

## Installation

```bash
sudo pacman -S sigmaos-grafana-loki
```

## Configuration

Loki is configured to use SigmaOS logging standards. Configuration is stored in `/etc/loki/`.

## Usage

```bash
# Start Loki
sudo systemctl start loki

# Enable on boot
sudo systemctl enable loki

# Access API
http://localhost:3100
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-grafana-loki)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
