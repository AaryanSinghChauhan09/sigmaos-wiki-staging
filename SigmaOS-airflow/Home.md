# SigmaOS Apache Airflow

Apache Airflow integration for SigmaOS - open-source workflow orchestration platform.

## Overview

SigmaOS Apache Airflow provides a workflow orchestration platform for authoring, scheduling, and monitoring data pipelines programmatically.

## Features

- **DAGs**: Workflows as code
- **Scheduler**: Intelligent scheduling
- **Executor**: Multiple executor types
- **Web UI**: Monitor and manage pipelines
- **Hooks**: Integrations with external systems
- **Operators**: Extensible operator library
- **XCom**: Cross-task communication
- **Sensors**: Wait for external events

## Installation

```bash
sudo pacman -S sigmaos-airflow
```

## Configuration

Airflow is configured to use the SigmaOS configuration system. Edit `/etc/sigmaos/airflow/airflow.cfg` for customization.

## Usage

```bash
# Start Airflow
sudo systemctl start sigmaos-airflow

# Enable on boot
sudo systemctl enable sigmaos-airflow

# Access web interface
http://localhost:8080
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-airflow)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
