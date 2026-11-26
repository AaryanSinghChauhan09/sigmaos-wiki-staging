# SigmaOS-sigma-sh

Rescue shell for boot debugging. Command parser (whitespace +
double-quote aware), builtins `help ls pwd cd echo cat which mem ps time
launch reboot exit`, and trait-based Io/Fs/ProcTable/MemInfo/System
backends so the shell is fully testable on host. `which` locates a
program on the standard PATH dirs (`/bin /sbin /usr/bin /usr/sbin`)
or verifies an explicit path. `cd` changes the working directory with
`.`/`..` normalization (`~` and bare `cd` go to `/`), and `cd -`
returns to the previous directory via `OLDPWD`. `;` separates commands
on one line (quote-aware, so `echo "a;b"` stays intact). `history`
lists the last 100 commands. `src/bin/sigma-sh.rs`
is the std host frontend; SigmaOS-native `sigma-init` (`/init`) and
`sigma-child` are built with the `sigmaos-target` feature for
x86_64-unknown-none and packed by `SigmaOS-xtask` (the host `sigma-sh`
binary is not packed). The `no_std` utility bins are gated behind
`sigmaos-target`. 12 lib tests.
