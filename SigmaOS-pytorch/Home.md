# SigmaOS PyTorch

PyTorch integration for SigmaOS - open-source machine learning framework.

## Overview

SigmaOS PyTorch provides an open-source machine learning framework for Python. Integration with SigmaOS ML/DL systems and GPU support.

## Features

- **Machine learning**: Neural network training and inference
- **Python**: Python API
- **GPU support**: CUDA and ROCm support
- **Dynamic graphs**: Dynamic computation graphs
- **Distributed**: Distributed training
- **Themes**: SigmaOS theme integration
- **Documentation**: Comprehensive documentation
- **Community**: Large community and ecosystem

## Installation

```bash
sudo pacman -S sigmaos-pytorch
```

## Usage

```python
import torch
import torch.nn as nn

# Create a simple neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create model
model = Net()
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-pytorch)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
