# SigmaOS Configuration System

Declarative configuration system for SigmaOS - NixOS-inspired configuration management.

## Overview

SigmaOS Configuration System provides a declarative configuration management system inspired by NixOS. System configuration is expressed as code, enabling reproducible, version-controlled system state.

## Features

- **Declarative**: Describe what the system should look like, not how to get there
- **Reproducible**: Same configuration produces same system state
- **Version-controlled**: Configuration in git for rollback and audit
- **Atomic**: Changes are applied atomically
- **Rollback**: Easy rollback to previous configurations
- **Modular**: Configuration split into modules
- **Type-safe**: Type checking for configuration values
- **Validation**: Configuration validation before application

## Configuration Language

SigmaOS uses a TOML-based configuration language for simplicity and familiarity:

```toml
# /etc/sigmaos/config.toml

[system]
hostname = "sigmaos-desktop"
timezone = "UTC"
locale = "en_US.UTF-8"

[network]
dhcp = true
wifi = true

[desktop]
environment = "hyprland"
theme = "sigmaos-dark"

[security]
firewall = true
automatic_updates = true

[packages]
included = ["firefox", "thunderbird", "vscode"]
```

## Modules

Configuration is split into modules for organization:

- **system**: Core system settings
- **network**: Network configuration
- **desktop**: Desktop environment settings
- **security**: Security policies
- **packages**: Package management
- **users**: User configuration
- **services**: Service configuration

## Commands

```bash
# Apply configuration
sudo sigmaos-config apply

# Validate configuration
sudo sigmaos-config validate

# Rollback to previous configuration
sudo sigmaos-config rollback

# List configurations
sudo sigmaos-config list

# Show current configuration
sudo sigmaos-config show
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-config-system)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
