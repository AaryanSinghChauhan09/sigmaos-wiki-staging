# SigmaOS MySQL

MySQL integration for SigmaOS - open-source relational database.

## Overview

SigmaOS MySQL provides an open-source relational database management system. Integration with SigmaOS data management and security systems.

## Features

- **ACID compliance**: Transaction support
- **SQL standard**: MySQL SQL dialect
- **Replication**: Master-slave replication
- **Clustering**: MySQL Cluster support
- **Partitioning**: Table partitioning
- **Full-text search**: Built-in full-text search
- **JSON support**: JSON data type
- **Performance**: High-performance queries

## Installation

```bash
sudo pacman -S sigmaos-mysql
```

## Configuration

MySQL is configured to use SigmaOS data standards. Configuration is stored in `/etc/mysql/`.

## Usage

```bash
# Start MySQL
sudo systemctl start mysqld

# Enable on boot
sudo systemctl enable mysqld

# Connect to database
mysql -u root -p
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-mysql)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
