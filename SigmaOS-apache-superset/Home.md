# SigmaOS Apache Superset

Apache Superset integration for SigmaOS - modern data exploration and visualization platform.

## Overview

SigmaOS Apache Superset provides a modern business intelligence platform for data exploration, visualization, and dashboard creation. Built on Apache Superset with SigmaOS integration.

## Features

- **Data exploration**: Interactive data exploration with SQL Lab
- **Visualization**: Rich chart types and dashboards
- **Database support**: Connect to SQL databases, data warehouses, and analytical engines
- **Security**: Row-level security and role-based access control
- **API**: REST API for programmatic access
- **Caching**: Query caching for performance
- **Scheduling**: Dashboard refresh scheduling
- **Embedding**: Embed dashboards in applications

## Databases Supported

- PostgreSQL
- MySQL
- SQLite
- ClickHouse
- DuckDB
- Apache Spark
- Apache Druid
- Presto/Trino
- Snowflake
- BigQuery

## Installation

```bash
sudo pacman -S sigmaos-apache-superset
```

## Configuration

Superset is configured to use the SigmaOS configuration system. Edit `/etc/sigmaos/superset/config.py` for customization.

## Usage

```bash
# Start Superset
sudo systemctl start sigmaos-superset

# Enable on boot
sudo systemctl enable sigmaos-superset

# Access web interface
http://localhost:8088
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-apache-superset)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
