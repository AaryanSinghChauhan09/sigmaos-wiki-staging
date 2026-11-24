# SigmaOS Plugin Registry

Rails control plane for the SigmaOS plugin registry (plugins.sigmaos.org). Provides hosted registry and static data plane for plugin management.

## Overview

The SigmaOS Plugin Registry is a Rails application that serves as the control plane for the plugin ecosystem. It manages plugin metadata, validation, and publishes the registry data that the marketplace frontend reads.

## Features

- **Plugin metadata**: Central registry of available plugins
- **Validation**: Automated plugin validation and verification
- **Hosted registry**: API and data plane for plugin distribution
- **Accounts**: User accounts for plugin submission and management
- **Publishing**: Automated catalog build and publication

## Architecture

- **Database**: Turso/libSQL for plugin metadata
- **Authentication**: Better Auth for user accounts
- **API**: REST API for plugin queries and submissions
- **Static data**: CDN-hosted plugin catalog

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-plugin-registry)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
