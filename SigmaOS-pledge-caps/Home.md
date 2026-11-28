# SigmaOS-pledge-caps

> pledge-caps

## Status

- **Component**: pledge-caps
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-pledge-caps

## Overview

**Declarative capability-based privilege reduction for SigmaOS processes.**

After initialization, a process declares the minimum `Cap` set it requires.
All other capabilities are dropped irrevocably — inspired by OpenBSD's `pledge()`,
expressed as a pure SigmaOS-native API with no foreign distro identity.

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
