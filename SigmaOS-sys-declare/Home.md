# SigmaOS-sys-declare

> sys-declare

## Status

- **Component**: sys-declare
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-sys-declare

## Overview

**Declarative system configuration with diff-and-apply semantics.**

Describe the desired state of every SigmaOS component in a `SystemSpec`.
The engine diffs against the current state and produces a minimal `DiffPlan`.
Only the deltas are applied — idempotent, atomic, and rollback-safe.

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
