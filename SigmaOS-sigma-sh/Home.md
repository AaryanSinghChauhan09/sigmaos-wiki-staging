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
lists the last 100 commands. `export NAME=value` / `unset NAME` manage a
shell environment, and `$NAME` / `${NAME}` expand in command args.
`cmd1 && cmd2` runs the second command only when the first is a
known builtin that didn't hit "command not found". `cmd1 || cmd2`
runs the second command only when the first fails. `*` globs expand in
arguments against the filesystem (`echo /*`, `cat /boot/vmlinuz*`);
unmatched patterns pass through unchanged. `true`/`:`/`false`/`clear`
are builtins (`false` fails for `&&`/`||`), and `launch` resolves bare
program names through the PATH dirs. `cmd > file` truncates and
`cmd >> file` appends via `Fs::write_file` — all builtin output routes
through the redirect-aware `emit` path. `mkdir`, `rmdir`, `rm`, and
`touch` mutate the filesystem via `Fs::create_dir`/`remove_path`/
`write_file`. `cp`/`mv` copy via read+write (`mv` removes the source),
and `head -n N`, `tail -n N`, `wc` work on file contents. `grep`
searches file contents (substring match) with `-i` `-v` `-n` `-c`.
`sort [-r]`, `uniq`, and recursive `find [dir]` round out the text
and filesystem tools. `basename`, `dirname`, and `seq` cover path
manipulation and number sequences. `env [NAME]` reads variables and
`sleep <secs>` pauses via `System::sleep`. `kill [-SIG] <pid>` sends a
signal via `System::kill(pid, sig)` — `-9`/`-KILL`/`-SIGKILL` select the
signal (default SIGTERM; host runs `kill -s <sig> <pid>`). Failing builtins
(`cd`, `ls`, `cat`, `which`, `env` misses, `kill` misses, `false`, unknown
commands) set the status used by `&&`/`||`. `cmd1 | cmd2` pipes stdout of
each stage into the next stage's stdin — `cat`, `head`/`tail`, `wc`,
`grep`, `sort`, and `uniq` read piped input when given no file argument,
so `seq 3 | grep 2` and `cat /var/log/x | wc` work like a real shell.
`cmd < file` feeds a file as the command's stdin (`grep err < /var/log/x`,
`wc < file`), overriding any piped input for that command. `uname`
prints the OS name via `System::uname` (host reports `std::env::consts::OS`).
`src/bin/sigma-sh.rs`
is the std host frontend; SigmaOS-native `sigma-init` (`/init`) and
`sigma-child` are built with the `sigmaos-target` feature for
x86_64-unknown-none and packed by `SigmaOS-xtask` (the host `sigma-sh`
binary is not packed). The `no_std` utility bins are gated behind
`sigmaos-target`. 29 lib tests.
