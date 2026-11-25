# SigmaOS-sigma-sh

Rescue shell for boot debugging. Command parser (whitespace +
double-quote aware), builtins `help ls pwd echo cat mem ps time
launch reboot exit`, and trait-based Io/Fs/ProcTable/MemInfo/System
backends so the shell is fully testable on host. `src/bin/sigma-sh.rs`
ships std implementations (real /proc, ps, spawn) and is packed into
the initramfs as `/bin/sigma-sh` and `/init`. 7 lib tests.
