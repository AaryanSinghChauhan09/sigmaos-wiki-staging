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
is the std host frontend; SigmaOS-native `sigma-init` (`/init`),
`sigma-child`, and `sh` are built with the `sigmaos-target` feature for
x86_64-unknown-none and packed by `SigmaOS-xtask` (the host `sigma-sh`
binary is not packed). The `no_std` utility bins are gated behind
`sigmaos-target`. `sh` (`/sh`) is a bare-metal interactive shell: it
wires the Shell engine to console fd 0/1 and the initramfs VFS, and
boots to an interactive `sigma>` prompt after `/init` spawns it.
Console input works over serial RX and the PS/2 keyboard; `ps`, `mem`,
`uname`, `time`, `launch`/`wait` are backed by real syscalls — verified
in QEMU (`launch /child` runs concurrently, `wait` reports exit status
42, `ps` shows live process states). `launch` forwards the shell's
exported variables as the child's envp — `export FOO=bar` then
`launch /child` delivers `env0=FOO=bar` (commit `7c17c7d`).
`SysFs::write_file` uses open/write/close against the writable VFS,
so `>`/`>>` redirects, `touch`, `cp`/`mv` file writes all work
in-guest (commit `266490e`). `create_dir`/`remove_path` ride the
MKDIR/UNLINK/RMDIR syscalls, so `mkdir`, `rmdir`, `rm` work too
(commit `4e749d4`). `ls -l` prints type/permissions/size via the
STAT syscall (commit `b2d6c76`). `jobs`/`fg`/`bg` are real: launch
records jobs, fg waits on a pid or `[n]` selector, jobs marks reaped
entries done (commit `3289ff8`). `cd` syncs the kernel cwd via
CHDIR so spawned children inherit it (commit `f5892d4`). A trailing
`&` is accepted as a background marker (commit `becf3e5`).
`launch prog > file` / `>> file` redirects the child's stdout/stderr
into the file via the SPAWN stdout_fd arg (commit `9ed41ae`).
`launch prog < in` feeds the child's stdin via stdin_fd (commit
`069d539`). `launch prog 2> file` / `2>> file` (including inline
`2>file`) routes the child's stderr alone via the stderr_fd SPAWN
arg (commits `9bd90f0`/`f53384f`/`62b849a`), verified in QEMU with
the sigma-child `stderr` marker arg. `&>`/`&>>` (incl. inline
`&>file`) redirects both streams; launch shares one fd so stdout and
stderr interleave in the file (commit `baa2625`).
`cmd1 | cmd2` pipelines now use real kernel pipes when a `launch`
stage is involved (commit `eb4381a`): the producer's stdout_fd and
the consumer's stdin_fd point at opposite ends of a `pipe()` pair,
the shell closes its copies after spawning, and blocking pipe
read/write in the kernel (commit `9522487`) handles empty/full
sleeps, EOF on last-writer close, and EPIPE on last-reader close.
Builtin→launch feeds captured text through a deferred pipe write;
launch→builtin drains the pipe to stdin. Verified in QEMU:
`echo pipe-data | launch /child pipe` echoes then EOF, and
`launch /child gen | launch /child pipe > /p.txt` streams the
producer's output through the pipe. This also fixed a latent kernel
bug where `pipe()` returned two fds pointing at the same slot —
the write end overwrote the read end. Multi-stage pipelines
(`a | b | c`), >4KiB payloads through the 4KiB buffer, and
launch→builtin drains are all verified in QEMU.
New coreutils builtins (commit `d26a8e5`): `printf` (format specs +
escapes), `test`/`[` (recursive-descent expression parser with
`-e`/`-f`/`-d`/`-s`/`-n`/`-z`, string and integer comparisons, `!`,
`-a`/`-o`, parens), `tr` (`-d`, `a-z` ranges), `cut` (`-d`/`-f`/`-c`,
attached getopt forms, open ranges), `nl`, and `tee`. The parser
now handles single quotes everywhere and splits pipelines/`;`/`&&`/
`||` quote-aware, so `echo "a|b"` and `'quoted args'` behave like
POSIX sh. Expansion is quote-aware (commit `6218679`): single quotes
suppress `$` and globbing, double quotes suppress globbing only —
`echo /c*` globs while `'/c*'`/`"/c*"` print literally.
Commit `5c8c531` adds `xargs` (`-I STR` replacement, `-n N` grouping)
and `paste` (`-d` delimiter, multi-file/stdin column join), and fixes
`printf` bypassing pipeline capture and `>` redirection (it wrote via
`io.write` directly) — `printf ... | cmd` and `printf ... > file` now
behave like POSIX. Commit `0bceb75` adds `2>&1` (stderr follows
stdout's redirect target — shares the fd with `> out`, flows into
pipes via the kernel stderr->stdout fallback). Commit `0a04fc5`
adds `od` (hex+ASCII / `-c` char dump), `fold -w`, and
`expand`/`unexpand -t` tab/space conversion — all reading file or
piped stdin via a shared `input_bytes` helper.
Commit `1c1d131` adds POSIX command substitution `$(...)`: the inner
line runs through the full executor (pipelines, `;` lists) and its
stdout is substituted with trailing newlines stripped. The tokenizer
and all metachar splitters are now paren-aware so `$(echo a; echo b)`
doesn't split, and pipelines preserve an outer capture so
`"$(echo x | cat)"` yields `x`. Single quotes still suppress it.
Commit `6d11343` adds shell functions: `name() { ...; }` defs
(functions override builtins, `command` bypasses), `return [n]`,
`shift`, and positional params `$1..$N`/`$#`/`$@`/`$*` — bodies run
through the full executor so pipelines/substitution compose.
Also fixed trailing `;`/`&&`/`||` leaking into args. 54 lib tests.
Commit `11853ca` adds compound commands: `if/then/elif/else/fi`,
`for VAR [in items]; do ...; done` (bare `for VAR` iterates `$@`,
the loop var is a shell env var), `while`/`until ...; do ...; done`
with a 100k-iteration safety cap, and `break`/`continue` scoped by
loop depth. Compounds parse into a CNode tree via a recursive-descent
parser over quote-aware `;`-tokens; nesting works (`then for ...`,
`if` inside `for` bodies), and trailing `; cmd` after `fi`/`done`
runs as a sibling. Whole-line `VAR=value [VAR2=value2]` assignments
set env vars with `$`/`$()` expansion. `break`/`continue` are scoped
by loop depth. Commit `8fc6c8b` adds `$(( ))` arithmetic expansion
(`+ - * / %`, unary signs, parens, literals, env-var names) — the
tokenizer and splitters now count all unquoted parens inside a
substitution so nested `$(( ))` doesn't split args. QEMU-verified
counting `while` loops (`i=$((i+1))`). Commit `69dcc3a` adds
`case WORD in pat[|pat]) LIST ;; ... esac` — glob patterns via
glob_match, `|` alternation, `$`-expanded word, bodies through the
full executor. QEMU-verified. Commit `322cad9` adds the `read`
builtin (line-at-a-time from pipes or console, multi-var field
splitting, POSIX EOF semantics) and compound pipeline stages —
`prod | while read l; do ...; done` now works via a persistent
`stdin_rest` cursor and pre-`;` pipeline detection. QEMU-verified.
Commit `aca1c23` adds `${var op word}` expansion —
`:-`/`-` defaults, `:=`/`=` assign+default, `:+`/`+` alternates,
`:?`/`?` errors, `${#var}` length, with recursive word expansion
and nested `${...}` matching. Commit `18c5580` adds affix trimming
`${var#pat}`/`${var%pat}`/`${var##pat}`/`${var%%pat}` (shortest/longest
glob affix removal). Commit `5e07223` adds `readonly` (immutable vars
across assignment/export/unset/${}:=) and `local` (function-scoped
vars restored on return via local_stack). `select` loops and `. FILE`/`source FILE` script execution added (vars/functions persist). QEMU-verified. `hostname`/`arch` builtins added; initramfs now ships /etc/hostname and /etc/os-release. `fork` builtin wired to kernel fork(2) (QEMU-verified: parent/child both ran). `exec COMMAND [ARGS...]` builtin wired to kernel exec(2) — POSIX image replacement, QEMU-verified (`exec /child` turned the shell pid into sigma-child). Bare `wait` now waits for ANY child (kernel WAIT_ANY, QEMU-verified). `uname` gained POSIX flags (-a/-s/-n/-r/-m/-o; QEMU-verified `uname -a` -> "sigmaos sigmaos 0.1.0 x86_64 SigmaOS"). `dmesg` builtin reads the kernel ring buffer via the new DMESG syscall (QEMU-verified boot-log replay). Added `id`/`whoami`/`groups`/`tty`/`printenv`/`set`/`yes` builtins and `free [-m|-g]`/`nproc` (procps-style MEMINFO report, QEMU-verified). `pushd`/`popd`/`dirs` dir-stack builtins and `alias`/`unalias` with first-word expansion (QEMU-verified). `echo` gained -n/-e/-E/-- flags with backslash escapes. `fc` (history rerun/list) and `times` added. `type` (alias/function/builtin/PATH resolution via new BUILTIN_NAMES table) and `builtin` added — QEMU-verified all outcomes. `df [path]` reports filesystem kind + node count via the new STATFS syscall (QEMU-verified: `df /bin` -> initramfs). 70 lib tests.
All three user binaries link non-PIE at image base 0x600000
(`.cargo/config.toml`) and use naked `_start` stubs that align RSP
to 16 bytes before calling Rust main. 43 lib tests.
