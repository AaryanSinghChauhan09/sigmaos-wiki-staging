# SigmaOS Speedtest

Network latency and throughput measurement for SigmaOS — dependency-free
(std + serde only), safe code only.

## Overview

`SigmaOS-speedtest` measures TCP connect latency (`ping`) and download
throughput (`download`, capped at `max_bytes`) against a host:port,
plus `ping_stats` for min/avg/max over N samples. Results are serde-
serializable structs (`PingResult`, `ThroughputResult`). All sockets
use `connect_timeout`/`set_read_timeout` so tests and CLI runs are
bounded.

## Features

- **TCP ping**: connect latency in ms with typed errors
  (`InvalidAddr`, `NoAddr`, `Timeout`)
- **Throughput**: bytes downloaded, duration, and computed Mbps
- **Statistics**: min/avg/max latency over repeated pings
- **Tests**: 5 unit tests run entirely on loopback listeners — no
  external network required

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-speedtest)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
