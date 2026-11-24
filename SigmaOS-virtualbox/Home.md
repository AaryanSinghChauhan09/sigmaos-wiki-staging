# SigmaOS VirtualBox

VirtualBox integration for SigmaOS - virtualization platform.

## Overview

SigmaOS VirtualBox provides a virtualization platform for running multiple operating systems. Integration with SigmaOS security and theme systems.

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
sudo pacman -S sigmaos-virtualbox
```

## Configuration

VirtualBox is configured to use SigmaOS security policies. VMs are stored in `~/VirtualBox VMs/`.

## Usage

```bash
# Start VirtualBox
sigmaos-virtualbox

# Start a VM headless
VBoxHeadless --startvm "VM Name"

# List VMs
VBoxManage list vms
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-virtualbox)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
