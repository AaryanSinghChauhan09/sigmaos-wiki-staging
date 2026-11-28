# SigmaOS-atomic-root

> atomic-root

## Status

- **Component**: atomic-root
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-atomic-root

## Overview

**Immutable root filesystem management with A/B boot slots.**

SigmaOS maintains two root filesystem slots (A and B). The inactive slot is
updated atomically; the active pointer is flipped in a single rename operation.
On failure, the system boots from the previous slot automatically — no manual
rollback required.

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
