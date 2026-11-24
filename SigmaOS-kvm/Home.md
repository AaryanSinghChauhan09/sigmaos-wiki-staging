# SigmaOS KVM

KVM integration for SigmaOS - Kernel-based Virtual Machine.

## Overview

SigmaOS KVM provides Kernel-based Virtual Machine support for running multiple operating systems with near-native performance. Integration with SigmaOS security and theme systems.

## Features

- **Virtualization**: Near-native performance with KVM
- **Management**: libvirt integration for VM management
- **Snapshots**: Save and restore VM states
- **Networking**: Virtual networking with bridge support
- **USB support**: USB device passthrough
- **Security**: SigmaOS security integration
- **Headless mode**: Run VMs without GUI
- **Live migration**: Migrate running VMs between hosts

## Installation

```bash
sudo pacman -S sigmaos-kvm
```

## Configuration

KVM is configured to use SigmaOS security policies. VMs are managed via libvirt and stored in `/var/lib/libvirt/`.

## Usage

```bash
# Start libvirt
sudo systemctl start libvirtd

# Enable on boot
sudo systemctl enable libvirtd

# List VMs
virsh list --all

# Start a VM
virsh start vm-name

# Connect to VM console
virsh console vm-name
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-kvm)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
