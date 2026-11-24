# SigmaOS MongoDB

MongoDB integration for SigmaOS - document-oriented NoSQL database.

## Overview

SigmaOS MongoDB provides a document-oriented NoSQL database for flexible data storage. Integration with SigmaOS data management and security systems.

## Features

- **Document model**: BSON document storage
- **Schema-less**: Flexible document structure
- **Indexing**: Rich indexing capabilities
- **Aggregation**: Powerful aggregation framework
- **Replication**: Replica set support
- **Sharding**: Horizontal scaling
- **GridFS**: File storage
- **Change streams**: Real-time data change notifications

## Installation

```bash
sudo pacman -S sigmaos-mongodb
```

## Configuration

MongoDB is configured to use SigmaOS data standards. Configuration is stored in `/etc/mongodb/`.

## Usage

```bash
# Start MongoDB
sudo systemctl start mongod

# Enable on boot
sudo systemctl enable mongod

# Connect to database
mongosh
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-mongodb)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
