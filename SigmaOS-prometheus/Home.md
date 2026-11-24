# SigmaOS Prometheus

Prometheus integration for SigmaOS - monitoring and alerting system.

## Overview

SigmaOS Prometheus provides a monitoring and alerting toolkit for collecting metrics and generating alerts. Integration with SigmaOS monitoring and alerting systems.

## Features

- **Metrics collection**: Collect metrics from applications
- **Time-series database**: Store time-series data
- **Query language**: PromQL for querying
- **Alerting**: Alert rules and notifications
- **Service discovery**: Automatic service discovery
- **Grafana integration**: Native Grafana integration
- **Recording rules**: Pre-compute metrics
- **Federation**: Hierarchical monitoring

## Installation

```bash
sudo pacman -S sigmaos-prometheus
```

## Configuration

Prometheus is configured to use SigmaOS monitoring standards. Configuration is stored in `/etc/prometheus/`.

## Usage

```bash
# Start Prometheus
sudo systemctl start prometheus

# Enable on boot
sudo systemctl enable prometheus

# Access web interface
http://localhost:9090
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-prometheus)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
