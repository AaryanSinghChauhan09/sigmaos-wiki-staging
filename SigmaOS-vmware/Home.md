# SigmaOS VMware

VMware integration for SigmaOS - VMware virtualization platform.

## Overview

SigmaOS VMware provides VMware virtualization platform support for running multiple operating systems. Integration with SigmaOS security and theme systems.

## Features

- **Virtualization**: Run multiple operating systems
- **Snapshots**: Save and restore VM states
- **Shared folders**: Share files between host and guest
- **USB support**: USB device passthrough
- **Networking**: Multiple networking modes
- **Security**: SigmaOS security integration
- **Themes**: SigmaOS theme integration
- **Headless mode**: Run VMs without GUI

## Installation

```bash
sudo pacman -S sigmaos-vmware
```

## Configuration

VMware is configured to use SigmaOS security policies. VMs are stored in `~/VMware/`.

## Usage

```bash
# Start VMware
sigmaos-vmware

# Start a VM headless
vmrun start "VM.vmx" nogui

# List VMs
vmrun list
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-vmware)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
