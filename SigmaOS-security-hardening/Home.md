# SigmaOS Security Hardening

Security hardening for SigmaOS - AppArmor, kernel hardening, and security policies.

## Overview

SigmaOS Security Hardening provides comprehensive security features including AppArmor enforcement, kernel hardening, secure defaults, and security auditing.

## Features

- **AppArmor**: Mandatory Access Control enforcement
- **Kernel hardening**: Hardened kernel parameters
- **Secure defaults**: Security enabled by default
- **Security updates**: Automatic security patching
- **Audit logging**: Comprehensive security logging
- **Firewall**: Firewall enabled by default
- **SELinux**: Optional SELinux support
- **Signed packages**: Package signature verification
- **Secure boot**: Secure boot support
- **Encrypted storage**: Encrypted filesystem support

## Commands

```bash
# Check security status
sudo sigmaos-security status

# Run security audit
sudo sigmaos-security audit

# Apply security policies
sudo sigmaos-security apply

# Update security policies
sudo sigmaos-security update

# View security logs
sudo sigmaos-security logs
```

## Configuration

Edit `/etc/sigmaos/security.conf` for configuration:

```ini
[security]
apparmor = true
kernel_hardening = true
firewall = true
audit_logging = true
secure_boot = true
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-security-hardening)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
