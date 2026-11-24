# SigmaOS Metabase

Metabase integration for SigmaOS - simple, open-source business intelligence tool.

## Overview

SigmaOS Metabase provides an easy-to-use business intelligence tool for data analysis and visualization. No SQL required for basic queries.

## Features

- **Easy setup**: Quick configuration without complex setup
- **SQL queries**: SQL editor for advanced users
- **Visualizations**: Charts, graphs, and dashboards
- **Database support**: PostgreSQL, MySQL, MongoDB, and more
- **Pulse**: Scheduled reports via email or Slack
- **Embedding**: Embed charts in applications
- **Permissions**: Granular access control
- **Collections**: Organize questions and dashboards

## Installation

```bash
sudo pacman -S sigmaos-metabase
```

## Configuration

Metabase is configured to use the SigmaOS configuration system. Edit `/etc/sigmaos/metabase/config.yaml` for customization.

## Usage

```bash
# Start Metabase
sudo systemctl start sigmaos-metabase

# Enable on boot
sudo systemctl enable sigmaos-metabase

# Access web interface
http://localhost:3000
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-metabase)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
