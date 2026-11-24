# SigmaOS QEMU

QEMU integration for SigmaOS - machine emulator and virtualizer.

## Overview

SigmaOS QEMU provides a machine emulator and virtualizer for running multiple operating systems. Integration with SigmaOS security and theme systems.

## Features

- **Emulation**: Emulate various CPU architectures
- **Virtualization**: KVM acceleration for near-native performance
- **Snapshots**: Save and restore VM states
- **Networking**: Multiple networking modes
- **USB support**: USB device passthrough
- **Security**: SigmaOS security integration
- **Headless mode**: Run VMs without GUI
- **Block devices**: Multiple disk image formats

## Installation

```bash
sudo pacman -S sigmaos-qemu
```

## Configuration

QEMU is configured to use SigmaOS security policies. VM images are stored in `~/.local/share/qemu/`.

## Usage

```bash
# Start QEMU with KVM
qemu-system-x86_64 -enable-kvm -m 2048 -smp 2 disk.img

# Start QEMU without KVM
qemu-system-x86_64 -m 2048 -smp 2 disk.img

# Create a disk image
qemu-img create -f qcow2 disk.img 10G
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-qemu)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
