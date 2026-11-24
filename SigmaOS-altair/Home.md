# SigmaOS Altair

Altair integration for SigmaOS - declarative visualization library for Python.

## Overview

SigmaOS Altair provides a declarative visualization library for Python. Integration with SigmaOS data science and visualization systems.

## Features

- **Declarative**: Describe visualizations declaratively
- **Grammar of graphics**: Based on grammar of graphics
- **Interactive**: Interactive visualizations with Vega-Lite
- **Python**: Python API
- **Themes**: SigmaOS theme integration
- **Documentation**: Comprehensive documentation
- **Examples**: Example visualizations
- **Performance**: Optimized for performance

## Installation

```bash
sudo pacman -S sigmaos-altair
```

## Usage

```python
import altair as alt
import pandas as pd

# Create a visualization
chart = alt.Chart(data).mark_point().encode(
    x='x:Q',
    y='y:Q',
    color='category:N'
)

# Display the chart
chart.show()
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-altair)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
