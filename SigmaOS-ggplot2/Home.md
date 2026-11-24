# SigmaOS ggplot2

ggplot2 integration for SigmaOS - R visualization library.

## Overview

SigmaOS ggplot2 provides a powerful visualization library for R. Integration with SigmaOS data science and visualization systems.

## Features

- **Grammar of graphics**: Based on grammar of graphics
- **R**: R API
- **Themes**: SigmaOS theme integration
- **Documentation**: Comprehensive documentation
- **Examples**: Example visualizations
- **Performance**: Optimized for performance
- **Extension**: Extensible with packages
- **Community**: Large community and ecosystem

## Installation

```bash
sudo pacman -S sigmaos-ggplot2
```

## Usage

```r
library(ggplot2)

# Create a visualization
ggplot(mtcars, aes(x = wt, y = mpg, color = factor(cyl))) +
  geom_point() +
  labs(title = "MPG vs Weight")
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-ggplot2)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
