# SigmaOS Grafana

Grafana integration for SigmaOS - open-source analytics and interactive visualization platform.

## Overview

SigmaOS Grafana provides a comprehensive analytics and visualization platform for metrics, logs, and traces. Connect to multiple data sources and create powerful dashboards.

## Features

- **Dashboards**: Create and share dashboards
- **Data sources**: Connect to Prometheus, Loki, Tempo, Elasticsearch, and many more
- **Visualization**: Multiple visualization types
- **Alerting**: Alert rules and notifications
- **Plugins**: Extensive plugin ecosystem
- **Annotations**: Event annotation on graphs
- **Variables**: Template variables for dynamic dashboards
- **Permissions**: Role-based access control

## Installation

```bash
sudo pacman -S sigmaos-grafana
```

## Configuration

Grafana is configured to use the SigmaOS configuration system. Edit `/etc/sigmaos/grafana/grafana.ini` for customization.

## Usage

```bash
# Start Grafana
sudo systemctl start sigmaos-grafana

# Enable on boot
sudo systemctl enable sigmaos-grafana

# Access web interface
http://localhost:3000
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-grafana)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
