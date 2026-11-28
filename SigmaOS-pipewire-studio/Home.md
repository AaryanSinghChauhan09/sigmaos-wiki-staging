# SigmaOS-pipewire-studio

> pipewire-studio

## Status

- **Component**: pipewire-studio
- **State**: Implemented — source code present
- **Source**: https://github.com/AaryanSinghChauhan09/SigmaOS-pipewire-studio

## Overview

SigmaOS component: **pipewire-studio** — audio graph manager (PipeWire-inspired). The system audio graph is a set of Nodes (sinks, sources, filters, virtual devices) exposing Ports; Links connect output to input ports; Policy rules auto-route streams. Graph bookkeeping layer — real-time scheduling stays in the audio server.

- `src/lib.rs` — library implementation
- `src/main.rs` — CLI entry point
- `docs/` — architecture, principles, testing, security docs

## See Also

- [SigmaOS-ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO) — the shipping Arch-based distribution image
- [sigmaos-wiki-staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging) — centralized wiki planning repository
