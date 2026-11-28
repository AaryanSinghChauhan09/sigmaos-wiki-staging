# SigmaOS-audit-log

> SigmaOS SigmaOS-audit-log component

## Status

- **Component**: audit-log
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-audit-log

## Overview

**Structured security audit logging with tamper-evident event chaining.**

Each `AuditEvent` is chained to the previous via its SHA-256 hash. Any
retroactive modification breaks the chain and is detected by `verify_chain()`.

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
