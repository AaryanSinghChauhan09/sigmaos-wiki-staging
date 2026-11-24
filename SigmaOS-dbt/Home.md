# SigmaOS dbt

dbt (data build tool) integration for SigmaOS - transformation framework for data teams.

## Overview

SigmaOS dbt provides a transformation framework that enables data teams to transform data in their warehouse by writing SELECT statements.

## Features

- **SQL-based**: Write transformations in SQL
- **Modular**: Reusable models and macros
- **Testing**: Data tests and assertions
- **Documentation**: Auto-generated documentation
- **Version control**: All code in version control
- **Incremental models**: Efficient incremental runs
- **Hooks**: SQL hooks for pre/post processing
- **Adapters**: Support for multiple warehouses

## Installation

```bash
sudo pacman -S sigmaos-dbt
```

## Configuration

dbt is configured to use the SigmaOS configuration system. Edit `~/.dbt/profiles.yml` for database connections.

## Usage

```bash
# Initialize a dbt project
dbt init

# Run transformations
dbt run

# Run tests
dbt test

# Generate documentation
dbt docs generate
dbt docs serve
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-dbt)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
