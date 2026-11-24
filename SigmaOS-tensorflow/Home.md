# SigmaOS TensorFlow

TensorFlow integration for SigmaOS - open-source machine learning framework.

## Overview

SigmaOS TensorFlow provides an open-source machine learning framework for Python. Integration with SigmaOS ML/DL systems and GPU support.

## Features

- **Machine learning**: Neural network training and inference
- **Python**: Python API
- **GPU support**: CUDA and ROCm support
- **Keras**: High-level API with Keras
- **Distributed**: Distributed training
- **Themes**: SigmaOS theme integration
- **Documentation**: Comprehensive documentation
- **Community**: Large community and ecosystem

## Installation

```bash
sudo pacman -S sigmaos-tensorflow
```

## Usage

```python
import tensorflow as tf
from tensorflow import keras

# Create a model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    keras.layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-tensorflow)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
