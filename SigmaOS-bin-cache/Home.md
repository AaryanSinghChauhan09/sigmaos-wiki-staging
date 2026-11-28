# SigmaOS-bin-cache

> bin-cache

## Status

- **Component**: bin-cache
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-bin-cache

## Overview

SigmaOS component: **bin-cache** — content-addressed binary package cache. Ports build from source once; the payload is stored keyed by content hash + build metadata (toolchain, source revision, flags). Later installs fetch the cached binary — verified by SHA-256 and an optional detached signature record — instead of rebuilding. Atomic tmp+rename writes; corrupted entries are evicted on read.

- `src/lib.rs` — library implementation
- `src/main.rs` — CLI entry point
- `docs/` — architecture, principles, testing, security docs

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
