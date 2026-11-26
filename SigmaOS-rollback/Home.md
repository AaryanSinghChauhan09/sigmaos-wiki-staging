# SigmaOS Rollback

Pacman-style transaction journal: records the changes each transaction
made and plans the inverse steps needed to undo the most recent one.

## Capabilities

- `RollbackManager::record(id, steps)` — journals a completed
  transaction; duplicate ids rejected, bounded capacity evicts oldest
- `Step { action, target }` — `Action::Install`, `Action::Remove`, or
  `Action::Modify { backup }` (backup = path to the pre-change copy)
- `rollback_last()` — returns `Vec<InverseStep>` for the most recent
  non-rolled-back transaction, in reverse order (Install→Remove,
  Remove→Install, Modify→restore-from-backup)
- `mark_rolled_back(id)` — flag a transaction undone when the rollback
  was performed by an external tool (e.g. the package manager itself)
- `next_id()` — `txn-N` id generator
- `history()` / `len()` / `is_empty()` — journal inspection

The manager plans; the caller executes the inverse steps — keeping the
crate free of filesystem and package-manager coupling.

## Usage

```rust
use rollback::{Action, RollbackManager, Step};

let mut m = RollbackManager::new(16);
let id = m.next_id();
m.record(id.clone(), vec![
    Step { action: Action::Install, target: "firefox".into() },
    Step { action: Action::Modify { backup: "/var/backups/hosts".into() },
           target: "/etc/hosts".into() },
])?;

for step in m.rollback_last()? {
    // execute the inverse: remove firefox, restore /etc/hosts
}
```

## Build & Test

```sh
cargo build
cargo test
cargo clippy --all-targets -- -D warnings
cargo fmt --check
```

9 tests covering step inversion order, rolled-back skipping, capacity
eviction, and duplicate-id rejection.

## License

Apache-2.0

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-rollback)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
