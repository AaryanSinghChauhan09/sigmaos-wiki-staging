# SigmaOS Elasticsearch

Elasticsearch integration for SigmaOS - search and analytics engine.

## Overview

SigmaOS Elasticsearch provides a distributed search and analytics engine. Integration with SigmaOS data processing and logging systems.

## Features

- **Full-text search**: Powerful full-text search
- **Distributed**: Scalable distributed architecture
- **Analytics**: Real-time analytics capabilities
- **JSON documents**: Store and query JSON documents
- **Aggregations**: Powerful aggregation framework
- **Kibana integration**: Visualization with Kibana
- **Logstash integration**: Data ingestion with Logstash
- **Security**: Security and access control

## Installation

```bash
sudo pacman -S sigmaos-elasticsearch
```

## Configuration

Elasticsearch is configured to use SigmaOS data standards. Configuration is stored in `/etc/elasticsearch/`.

## Usage

```bash
# Start Elasticsearch
sudo systemctl start elasticsearch

# Enable on boot
sudo systemctl enable elasticsearch

# Access API
http://localhost:9200
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-elasticsearch)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
