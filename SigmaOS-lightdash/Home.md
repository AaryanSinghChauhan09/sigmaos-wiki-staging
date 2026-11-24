# SigmaOS Lightdash

Lightdash integration for SigmaOS - open-source business intelligence built on dbt.

## Overview

SigmaOS Lightdash provides a modern BI platform that works directly with your dbt project. Explore data, build charts, and share insights.

## Features

- **dbt integration**: Works directly with dbt models
- **SQL-free**: No SQL required for basic queries
- **Visualization**: Charts and dashboards
- **Data modeling**: Leverage dbt data models
- **Permissions**: Role-based access control
- **API**: REST API for programmatic access
- **Version control**: Data models in version control
- **Collaboration**: Share insights with team

## Installation

```bash
sudo pacman -S sigmaos-lightdash
```

## Configuration

Lightdash is configured to use the SigmaOS configuration system. Edit `/etc/sigmaos/lightdash/config.yaml` for customization.

## Usage

```bash
# Start Lightdash
sudo systemctl start sigmaos-lightdash

# Enable on boot
sudo systemctl enable sigmaos-lightdash

# Access web interface
http://localhost:8080
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-lightdash)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
