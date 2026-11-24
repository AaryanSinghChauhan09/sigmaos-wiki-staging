# SigmaOS PostHog

PostHog integration for SigmaOS - open-source product analytics platform.

## Overview

SigmaOS PostHog provides a comprehensive product analytics platform with session replay, feature flags, and surveys. All-in-one product insights.

## Features

- **Event tracking**: Custom event tracking
- **Session replay**: Watch user sessions
- **Feature flags**: Remote feature configuration
- **Surveys**: In-app surveys and feedback
- **Dashboards**: Pre-built and custom dashboards
- **Insights**: Funnels, retention, and paths
- **Webhooks**: Real-time data export
- **Permissions**: Role-based access control

## Installation

```bash
sudo pacman -S sigmaos-posthog
```

## Configuration

PostHog is configured to use the SigmaOS configuration system. Edit `/etc/sigmaos/posthog/config.yaml` for customization.

## Usage

```bash
# Start PostHog
sudo systemctl start sigmaos-posthog

# Enable on boot
sudo systemctl enable sigmaos-posthog

# Access web interface
http://localhost:8000
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-posthog)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
