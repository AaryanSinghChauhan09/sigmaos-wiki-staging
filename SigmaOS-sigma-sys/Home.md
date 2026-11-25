# SigmaOS-sigma-sys

Userspace syscall shim crate (`no_std` + `alloc`). Defines the
`Syscall` trait and a first-write-wins `register()`/`active()`/`raw()`
dispatch, plus `errno` constants and safe wrappers in `api` for every
syscall number in the kernel ABI (`GETPID`, `TIME`, `WRITE`, `OPEN`,
`READ`, `SPAWN`, `REBOOT`, ...). The `arch` module carries the x86_64
`syscall` instruction behind the `x86_64` feature. 4 tests.
