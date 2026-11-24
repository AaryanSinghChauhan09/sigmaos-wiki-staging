# SigmaOS Update System

Software update system for SigmaOS - automatic updates and security patches.

## Overview

SigmaOS Update System provides automatic software updates, security patches, and version management. Integrates with pacman and provides a unified update experience.

## Features

- **Automatic updates**: Scheduled automatic updates
- **Security updates**: Prioritized security patches
- **Rolling release**: Continuous updates without version locks
- **Notification**: Update notifications
- **Rollback**: Rollback capability for failed updates
- **Testing**: Update testing before deployment
- **Bandwidth control**: Limit update bandwidth
- **Package groups**: Group updates by category

## Commands

```bash
# Check for updates
sigmaos-update check

# Apply updates
sigmaos-update apply

# Automatic updates
sigmaos-update auto

# Rollback update
sigmaos-update rollback

# List available updates
sigmaos-update list
```

## Configuration

Edit `/etc/sigmaos/update.conf` for configuration:

```ini
[updates]
automatic = true
security_only = false
notify = true
rollback_enabled = true
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-update-system)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
