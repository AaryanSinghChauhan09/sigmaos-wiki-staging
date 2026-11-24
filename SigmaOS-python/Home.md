# SigmaOS Python

Python integration for SigmaOS - Python programming language runtime.

## Overview

SigmaOS Python provides the Python programming language runtime with SigmaOS-specific configurations and package management.

## Features

- **Python runtime**: Latest Python version
- **Package management**: pip and virtual environment support
- **SigmaOS bindings**: SigmaOS-specific Python bindings
- **Development tools**: Development tools and libraries
- **Jupyter integration**: Jupyter notebook support
- **Data science libraries**: Pre-installed data science libraries
- **Themes**: SigmaOS theme integration for Python tools

## Installation

```bash
sudo pacman -S sigmaos-python
```

## Configuration

Python is configured to use SigmaOS package management. Virtual environments are created in `~/.local/share/venv/`.

## Usage

```bash
# Run Python
python

# Create virtual environment
python -m venv myenv
source myenv/bin/activate

# Install packages
pip install package-name
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-python)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
