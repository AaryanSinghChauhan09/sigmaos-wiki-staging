# SigmaOS-sigma-sh

Rescue shell for boot debugging. Command parser (whitespace +
double-quote aware), builtins `help ls pwd echo cat mem ps time
launch reboot exit`, and trait-based Io/Fs/ProcTable/MemInfo/System
backends so the shell is fully testable on host. `src/bin/sigma-sh.rs`
is the std host frontend; SigmaOS-native `sigma-init` (`/init`) and
`sigma-child` are built with the `sigmaos-target` feature for
x86_64-unknown-none and packed by `SigmaOS-xtask` (the host `sigma-sh`
binary is not packed). The `no_std` utility bins are gated behind
`sigmaos-target`. 7 lib tests.
