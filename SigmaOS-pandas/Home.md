# SigmaOS Pandas

Pandas integration for SigmaOS - Python data analysis library.

## Overview

SigmaOS Pandas provides the Python pandas library for data manipulation and analysis. Essential for data science and data wrangling workflows.

## Features

- **Data structures**: DataFrame and Series
- **Data I/O**: Read/write from multiple formats
- **Data cleaning**: Missing data handling
- **Data manipulation**: Filtering, grouping, merging
- **Time series**: Time series functionality
- **Visualization**: Plotting integration
- **Performance**: Optimized operations
- **Integration**: Works with NumPy, SciPy, and more

## Installation

```bash
sudo pacman -S sigmaos-pandas
```

## Usage

```python
import pandas as pd

# Read data
df = pd.read_csv('data.csv')

# Manipulate data
df_filtered = df[df['column'] > 0]
df_grouped = df.groupby('column').mean()

# Write data
df.to_csv('output.csv')
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-pandas)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
