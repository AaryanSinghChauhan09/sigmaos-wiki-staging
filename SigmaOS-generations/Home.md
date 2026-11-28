# SigmaOS-generations

> generations

## Status

- **Component**: generations
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-generations

## Overview

SigmaOS component: **generations** — immutable system generations (NixOS-inspired). Every system state change produces a new Generation recording label, state hash, and timestamp. Activation is an atomic `active` pointer swap; rollback re-activates an older generation; GC keeps the active generation plus N newest. Single JSON doc, atomic tmp+rename writes.

- `src/lib.rs` — library implementation
- `src/main.rs` — CLI entry point
- `docs/` — architecture, principles, testing, security docs

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
