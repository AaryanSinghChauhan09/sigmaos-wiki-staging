# SigmaOS Redis

Redis integration for SigmaOS - in-memory data structure store.

## Overview

SigmaOS Redis provides an in-memory data structure store used as a database, cache, and message broker. Integration with SigmaOS caching and messaging systems.

## Features

- **In-memory**: Fast in-memory data storage
- **Data structures**: Strings, lists, sets, sorted sets, hashes
- **Pub/Sub**: Publish/subscribe messaging
- **Persistence**: RDB and AOF persistence
- **Replication**: Master-slave replication
- **Clustering**: Redis Cluster support
- **Lua scripting**: Server-side scripting
- **Streams**: Log-based data structure

## Installation

```bash
sudo pacman -S sigmaos-redis
```

## Configuration

Redis is configured to use SigmaOS caching standards. Configuration is stored in `/etc/redis/redis.conf`.

## Usage

```bash
# Start Redis
sudo systemctl start redis

# Enable on boot
sudo systemctl enable redis

# Connect to Redis
redis-cli
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-redis)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
