# SigmaOS Polars

Polars integration for SigmaOS - fast DataFrame library for Rust and Python.

## Overview

SigmaOS Polars provides a high-performance DataFrame library for data manipulation. Written in Rust with Python bindings, it offers excellent performance for large datasets.

## Features

- **Performance**: Multi-threaded, lazy evaluation
- **Memory efficient**: Zero-copy operations
- **Data structures**: DataFrame and Series
- **Data I/O**: Read/write from multiple formats
- **Data manipulation**: Filtering, grouping, joining
- **Type system**: Strong typing with null handling
- **SQL**: SQL interface
- **Python and Rust**: Native Python and Rust APIs

## Installation

```bash
sudo pacman -S sigmaos-polars
```

## Usage

```python
import polars as pl

# Read data
df = pl.read_csv('data.csv')

# Manipulate data
df_filtered = df.filter(pl.col('column') > 0)
df_grouped = df.groupby('column').mean()

# Write data
df.write_csv('output.csv')
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-polars)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
