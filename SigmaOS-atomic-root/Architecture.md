# Architecture — SigmaOS-atomic-root

Extracted from the repository README.

## Architecture

```
 ┌─────────────────────────────────────────────┐
 │              SlotManager                    │
 │  slot_a: RootSpec { hash, path }            │
 │  slot_b: RootSpec { hash, path }  ← update │
 │  active: A  ──atomic_switch──▶  active: B   │
 └─────────────────────────────────────────────┘
```
