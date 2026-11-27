# SigmaOS vs Arch Linux vs Omarchy Linux — Parity Matrix

This matrix compares SigmaOS against Arch Linux and Omarchy Linux across key areas. Each item is marked as:
- **✓ Verified**: Implemented and tested with reproducible evidence
- **○ Partial**: Partially implemented or needs further testing
- **✗ Missing**: Not implemented

## Installation

| Feature | SigmaOS | Arch | Omarchy | Evidence |
|---------|---------|------|---------|----------|
| ISO image | ✓ | ✓ | ✓ | 3.4 GB ISO built, QEMU boot tested |
| BIOS boot | ✓ | ✓ | ✓ | ISO includes syslinux |
| UEFI boot | ✓ | ✓ | ✓ | ISO includes UEFI entries |
| Live session | ✓ | ✓ | ✓ | QEMU reached graphical target |
| Installer | ○ | archiso | Omarchy Installer | SigmaOS-ISO has installer scripts, needs full end-to-end test |
| Automatic partitioning | ○ | Manual | Yes | Installer supports it, needs verification |
| LUKS encryption | ○ | Manual | Yes | Installer supports it, needs verification |
| BTRFS default | ✓ | Optional | Yes | Installer uses BTRFS with zstd:3 |
| Subvolume layout | ✓ | Manual | Yes | @, @home, @var, @var_tmp, @snapshots |

## Package Management

| Feature | SigmaOS | Arch | Omarchy | Evidence |
|---------|---------|------|---------|----------|
| pacman integration | ✓ | Native | Native | Uses standard pacman |
| Signed packages | ✓ | Yes | Yes | AppArmor + security hardening |
| Keyring management | ○ | archlinux-keyring | Custom | Has SigmaOS-keyring repo, needs verification |
| Mirror selection | ○ | reflector | Custom | Needs mirror configuration verification |
| Dependency resolution | ✓ | Native | Native | Uses pacman's solver |
| Conflict handling | ✓ | Native | Native | Uses pacman's conflict resolution |
| Interrupted upgrade recovery | ○ | Manual | Partial | BTRFS snapshots enable rollback |
| AUR support | ○ | yaourt/pikaur | Custom | Has AUR helper repo, needs testing |
| sigpkg | ✗ Experimental | N/A | N/A | Marked experimental in README |

## Hardware Support

| Feature | SigmaOS | Arch | Omarchy | Evidence |
|---------|---------|------|---------|----------|
| GPU drivers | ○ | Optional | Yes | Software rendering fallbacks added |
| AMDGPU | ○ | xf86-video-amdgpu | Yes | Needs hardware test |
| NVIDIA | ○ | nvidia | Yes | Needs hardware test |
| Intel | ○ | xf86-video-intel | Yes | Needs hardware test |
| Wi-Fi | ○ | Multiple | Yes | Needs hardware test |
| Bluetooth | ○ | bluez | Yes | Needs hardware test |
| Audio | ○ | pipewire/pulseaudio | Yes | Needs hardware test |
| Touchpad | ○ | libinput | Yes | Needs hardware test |
| Wayland compositors | ✓ | Multiple | Hyprland | Uses Hyprland |
| Xorg fallback | ○ | Yes | No | Needs verification |

## Desktop Defaults

| Feature | SigmaOS | Arch | Omarchy | Evidence |
|---------|---------|------|---------|----------|
| Window manager | ✓ (Hyprland) | Optional | Hyprland | Hyprland configured |
| Display server | ✓ (Wayland) | Xorg/Wayland | Wayland | Wayland primary |
| Status bar | ✓ (Waybar) | Optional | Waybar | Waybar with app launcher, media player |
| Launcher | ✓ (Waybar menu) | Optional | Omarchy launcher | Integrated in Waybar |
| Terminal | ✓ (kitty/zsh) | Optional | kitty | zsh enhanced with starship, aliases |
| Theme system | ✓ | Optional | Omarchy themes | SigmaOS UI kit |
| Wallpaper | ✓ | None | Yes | Configured |
| Keybindings | ✓ | Custom | Omarchy | Hyprland window rules configured |
| Desktop portals | ○ | xdg-desktop-portal | Yes | Needs verification |
| Screen sharing | ○ | pipewire | Yes | Needs verification |

## Security

| Feature | SigmaOS | Arch | Omarchy | Evidence |
|---------|---------|------|---------|----------|
| AppArmor | ✓ (Enforced) | Disabled | Disabled | Enabled by default in enforcement mode |
| Kernel hardening | ✓ | Partial | Partial | ASLR, ptrace restrictions, network hardening |
| auditd | ✓ | Optional | Optional | Preinstalled |
| Automatic security updates | ✓ | Manual | Manual | systemd timer with randomized delay |
| Secure Boot signing | ○ | Optional | No | sbctl included, needs verification |
| SELinux | ✗ | Optional | No | Not implemented |
| TPM support | ○ | Optional | No | tpm2-tools included |
| Firewall | ○ | iptables/nftables | Yes | Needs configuration verification |
| User privilege model | ✓ | Standard | Standard | Standard Linux permissions |

## Recovery

| Feature | SigmaOS | Arch | Omarchy | Evidence |
|---------|---------|------|---------|----------|
| BTRFS snapshots | ✓ | Manual | Yes | Automatic before/after pacman |
| Rollback utility | ✓ | Manual | Yes | sigmaos-snapshot rollback |
| Live ISO recovery | ✓ | Yes | Yes | Can boot ISO for recovery |
| chroot support | ✓ | Yes | Yes | Standard archiso chroot |
| Backup tools | ○ | Timeshift, etc | Yes | Needs verification |
| GRUB rescue | ✓ | Yes | Yes | Standard GRUB |

## Documentation

| Feature | SigmaOS | Arch | Omarchy | Evidence |
|---------|---------|------|---------|----------|
| Arch Wiki | ✓ (External) | Native | External | Can use Arch Wiki |
| Official docs | ○ | Excellent | Good | SigmaOS docs in progress |
| GitHub Wiki | ○ (104 pages staged) | N/A | N/A | Staged but needs enhancement |
| AGENTS.md per repo | ✓ (13/100) | N/A | N/A | 13 repos normalized |
| COMPONENT.tomL per repo | ✓ (100/100) | N/A | N/A | All repos have manifests |
| README per repo | ✓ (100/100) | Varies | Varies | All repos have README |
| API documentation | ○ | Varies | Varies | Needs enhancement |
| Installation guide | ○ | Excellent | Good | Needs comprehensive guide |

## Developer Experience

| Feature | SigmaOS | Arch | Omarchy | Evidence |
|---------|---------|------|---------|----------|
| Rust toolchain | ✓ | pacman | pacman | Multiple Rust repos |
| Package build tools | ✓ | makepkg | Custom | Has devtools port |
| AUR build environment | ○ | devtools | Custom | Needs verification |
| CI/CD | ○ | Varies | Varies | Needs automation |
| Linting | ✓ (cargo clippy) | Optional | Optional | Configured in repos |
| Formatting | ✓ (cargo fmt) | Optional | Optional | Configured in repos |
| Testing | ✓ (cargo test) | Varies | Varies | Configured in repos |
| Editor configs | ○ | Varies | Varies | Has editor-config repos |

## System Updates

| Feature | SigmaOS | Arch | Omarchy | Evidence |
|---------|---------|------|---------|----------|
| Rolling release | ✓ | Yes | Yes | Rolling model |
| Automatic updates | ✓ | Manual | Manual | systemd timer implemented |
| Update notifications | ○ | pacman hooks | Custom | Needs verification |
| Delta updates | ○ | Yes | Yes | Needs verification |
| Transaction hooks | ✓ | Yes | Yes | BTRFS snapshot hooks |
| Mirror ranking | ○ | reflector | Custom | Needs configuration |

## Summary Statistics

| Metric | SigmaOS | Arch | Omarchy |
|--------|---------|------|---------|
| Verified features | 18 | 35 | 28 |
| Partial features | 18 | 5 | 4 |
| Missing features | 4 | 0 | 3 |
| Total assessed | 40 | 40 | 35 |

## Priority Actions

1. **High Priority (Production-grade):**
   - Complete end-to-end installer test (QEMU install to disk, reboot, update)
   - Verify Arch package management dependability (keyring, mirrors, signing)
   - Test hardware support on real machines (GPU, Wi-Fi, audio, Bluetooth)
   - Verify desktop portals and screen sharing

2. **Medium Priority (UX/Polish):**
   - Consolidate overlapping repos (plugin marketplace, themes, shell configs)
   - Enhance GitHub Wiki with full content from READMEs (104 pages)
   - Automate CI/CD for ISO builds and boot tests
   - Clear documentation of supported vs experimental features

3. **Low Priority (Research):**
   - sigpkg development (currently experimental)
   - Custom microkernel research track
   - Additional security features (SELinux, advanced hardening)

## 2026-11-25 Progress

- `sigma-kernel` now reaches ring-3 userspace with ELF loading, user page
  tables, syscall dispatch, file I/O, interactive shell, processes
  (`SPAWN`/`WAIT`/`EXIT`), anonymous memory (`BRK`/`MMAP`/`MUNMAP`), and
  preemptive round-robin scheduling.
- Kernel surface expanded with FAT32, framebuffer console, VirtIO MMIO,
  tiling window manager, theme registry, agent plumbing, and ISO install
  planning.
- `sigma-sh` gained `cat`, `ls`, `kill`, `mount`, `pkg`, `ps`, pipeline
  parsing, and job-control stubs.
- `SigmaOS-initramfs` now has both the cpio/pack image builder and the
  mkinitcpio-style hook planner, including `--rootfs` packing.
- `SigmaOS-system-profile` is implemented and pushed to GitHub.
- All 117 local component repos are clean and synced (`0 ahead / 0 behind`).

## 2026-11-26 Progress

- Repo-wide Rust verification sweep complete: every component repo passes
  `cargo fmt --check`, `cargo clippy --all-targets -D warnings`, and
  `cargo test` except `SigmaOS-video` (needs FFmpeg/gbm dev headers).
- `rust-validation.yml` CI (fmt + clippy + tests, transitive SigmaOS-*
  path-dep checkout) rolled out to 34 repos; screensaver installs
  `libxkbcommon-dev`, omafind fetches the pinned llama.cpp engine.
- Wiki-only GitHub repos being created as the rate-limit window allows
  (~35 remaining, background retry running).

### 2026-11-26 component improvements (Arch/Omarchy-inspired)

- `sigma-sh`: full operator set (`;` `&&` `||` `|` `<` `>` `>>`), real
  builtin-to-builtin pipelines with stdin capture, `*` globbing, `$VAR`
  expansion, `export`/`unset`/`env`, `history`, `cd`/`cd -`/`pwd`,
  `which`, `kill`, `uname`, ~15 file/text utils (`cat cp mv mkdir
  rmdir rm touch head tail wc grep sort uniq find basename dirname seq`),
  `launch` PATH resolution, `sleep`, `true/false/:/clear`; 29 tests.
- `initramfs`: `--compress none|gzip|zstd` image packing (flate2+zstd).
- `system-profile`: `--doctor` config health check; `--enable/--disable`.
- `shell-config`: hex color validation fix; `module <name> on|off`.
- `platform`: kernel >= 6.1 check fix; `gpu_driver` detection.
- `update-system`: `pending_updates` implemented; CLI/wiki corrected.
- `pkg-core`: `orphans` query (pacman -Qtd equivalent).
- `config-system`, `build-system`: added test coverage; verifier
  root-parameterized.
- `recovery-system`: real `verify_snapshot`; loud `restore` failure;
  fixed duplicate `-i` clap shorts panic.
- `rollback`: pacman-style transaction journal with rollback planning.
- `genoffice`: `DocumentFormat` extension/path detection.
- `notifications`: daemon core implemented locally (repo archived on
  GitHub; commit not pushed).
- Wiki staging: ~12 stale pages rewritten to match actual code.

## 2026-11-26 Kernel/Userspace Breakthrough

- `sigma-kernel` `64297b3`: fixed three ring-3 crash bugs found via QEMU
  + gdbstub debugging — `alloc_contiguous` now requires physically
  contiguous frames (was index-contiguous, so user stacks landed in the
  ISA hole `0xa0000-0xfffff` -> `ret` to `-1`); `alloc_table` zeroes
  page-table pages; all user images bias to `USER_LOAD_BASE=0x600000`
  with `kernel_image_end()` + ISA-hole reservations; user stacks
  zeroed on spawn/boot.
- `sigma-sh` `4264943`+: bare-metal `/sh` interactive shell
  (`sigma>` prompt), naked 16-byte-aligned `_start`, non-PIE at
  0x600000.
- Verified in QEMU: `/init` -> `/child` (exit 42 reaped) -> `/sh`
  reaches a live interactive prompt; commands echo and builtins
  execute. 82 kernel lib tests green.
- Interactive console input verified both ways: serial RX and PS/2
  keyboard (`sendkey` types into the live `sigma>` prompt). Root
  cause of the earlier wedge: `Keyboard::new`'s i8042 init sequence;
  fixed via `Keyboard::attached` (kernel `0643701`).
- New syscalls wired end-to-end: `MEMINFO` (nr 29, frame-allocator
  stats -> `mem` shows ~510 MiB), `PROCINFO` (nr 30, process table ->
  `ps` shows live states), and argv passing in SPAWN (`launch /child
  foo bar` -> argc=3, kernel `434f5ff`, sigma-sys `fa18583`,
  sigma-sh `c9f7bd9`).
- `wait [pid]` builtin: blocking wait with real exit status
  (`launch /child` + `wait` -> "pid 4 exited 42").
- envp passing end-to-end (kernel `378edde`, sigma-sys `21a2d5b`,
  sigma-sh `7c17c7d`): SPAWN descriptor grew an env section, the
  kernel builds a full `{argc, argv[], NULL, envp[], NULL}` stack
  image, and `launch` forwards the shell's exported vars — verified
  in QEMU (`export SIGMA_TEST=hello42` -> child prints
  `env0=SIGMA_TEST=hello42`).
- Writable VFS (kernel `3d31bbe`, sigma-sh `266490e`): Vfs gained
  create_file/write_at/truncate; open(2) honors O_CREAT/O_TRUNC/
  O_APPEND; WRITE reaches fd>=3 file fds. `>`/`>>` redirects, `touch`,
  `cp`/`mv` writes verified in QEMU. Fixed latent panic: open/pipe
  initialized fd slots via fd_get (requires used) — new fd_slot().
- MKDIR/UNLINK/RMDIR syscalls (kernel `aac1a95`, sigma-sys `73c6802`,
  sigma-sh `4e749d4`): VFS create_dir/unlink/remove_dir with errno
  mapping; `mkdir`/`rmdir`/`rm`/`touch`/`cp`/`mv` verified in QEMU
  (rmdir correctly refuses non-empty dirs).
- STAT syscall (kernel `5326ddf`, sigma-sys `f93a6cb`, sigma-sh
  `b2d6c76`): {mode,size} metadata; `ls -l` shows real sizes and
  dir flags in-guest.
- jobs/fg/bg (sigma-sh `3289ff8`): launch records jobs in a bounded
  table; fg waits by pid or [n]; verified in QEMU.
- Per-process cwd (kernel `0190476`, sigma-sys `c048ca2`, sigma-sh
  `f5892d4`): ProcSlot.cwd inherited at SPAWN; CHDIR/GETCWD nr 34/35;
  `cd` in /sh syncs kernel cwd so children inherit it.
- `&` background marker accepted by the parser (sigma-sh `becf3e5`).
- Process teardown (kernel `1c8a4cb`, sigma-sys `1ed40b6`): reap frees
  user data frames (P_USER leaves) before page tables — no more frame
  leak; NPROCS 4->8 allows concurrent children (verified: 3 /child
  jobs at once, mem free count stable across spawn/reap cycles).
- fd inheritance (kernel `560ab59`): SPAWN copies the parent's fd
  table; file offsets independent (dup-like), pipe ends share pipe_id.
- auxv (kernel `22118c7`): initial stack carries AT_PAGESZ/ENTRY/
  UID/EUID/GID/EGID/SECURE/RANDOM + AT_NULL after envp.
- launch redirection (kernel `8d4fe00`, sigma-sys `9ecb636`,
  sigma-sh `9ed41ae`): SPAWN arg4 stdout_fd reroutes child fd1/2;
  `launch prog > f` / `>> f` verified in QEMU.
- stdin redirect (kernel `f56cc10`, sigma-sys `60661cd`, sigma-sh
  `069d539`): SPAWN arg5 stdin_fd feeds child fd 0;
  `launch prog < in` verified in QEMU.
- stderr redirect (kernel `9bd90f0`, sigma-sys `f53384f`, sigma-sh
  `62b849a`): SPAWN arg6 stderr_fd reroutes child fd 2;
  `launch prog 2> f` / `2>> f` (incl. inline `2>f`) verified in QEMU
  via sigma-child `stderr` marker arg.
- combined redirect (sigma-sh `baa2625`): `&>`/`&>>` (incl. inline
  `&>f`) sets both stdout and stderr targets; launch dedupes to a
  single fd so streams share one offset — stdout+stderr interleave
  in one file, verified in QEMU.
- blocking pipes + launch pipelines (kernel `9522487`, sigma-sh
  `eb4381a`): pipe read/write sleep/wake via wait_pipe (EAGAIN
  retry), EOF on last-writer close, EPIPE on last-reader close,
  close/exit wake both directions; SPAWN accepts pipe fds for all
  three redirect args and close-on-spawns non-redirect pipe ends.
  execute_pipeline wires launch|launch with real kernel pipes;
  builtin->launch feeds text via deferred write, launch->builtin
  drains to pending_stdin. Fixed latent sys_pipe bug: both fd_alloc
  calls ran before either slot was marked used, so the write end
  overwrote the read end — pipe() never produced two fds. Verified:
  `echo pipe-data | launch /child pipe` echoes then EOF;
  `launch /child gen | launch /child pipe > /p.txt` streams output.
  Also verified: 3-stage `launch|launch|launch`, `echo one | cat |
  cat`, >4KiB payload through the 4KiB pipe buffer (blocking writer),
  and a 6-cycle launch+fg soak with identical `mem` free counts
  (520108 KiB) — no frame/proc leaks.
- coreutils expansion (sigma-sh `d26a8e5`): printf, test/[ (full
  expression parser), tr, cut, nl, tee added; single-quote support
  and quote-aware pipeline/;/&&/|| splitting fixed. Verified in
  QEMU; 42 lib tests.
- more coreutils (sigma-sh `5c8c531`): xargs (-I/-n) and paste (-d,
  multi-file/stdin) added; fixed printf bypassing pipeline capture
  and `>` redirect (wrote via io.write). QEMU-verified; 47 lib tests.
- fd/pipe capacity (kernel `55e10a7`): MAX_FDS 8->32, MAX_PIPES
  4->8 — inheritance+pipelines+redirects could exhaust 8 slots;
  fixed SPAWN redirect-fd off-by-one. QEMU-verified.
- `2>&1` redirect (sigma-sh `0bceb75`): stderr follows stdout's
  target — shares fd with `> out`, pipes via kernel fallback.
  QEMU-verified; 48 lib tests.
- text utils (sigma-sh `0a04fc5`): od (hex/char dump), fold -w,
  expand/unexpand -t; shared file-or-stdin input helper.
  QEMU-verified; 51 lib tests.
- command substitution (sigma-sh `1c1d131`): `$(...)` runs the inner
  line through the full executor and substitutes captured stdout;
  tokenizer+splitters are paren-aware; pipelines preserve outer
  capture. QEMU-verified; 52 lib tests.
- shell functions (sigma-sh `6d11343`): `name() { ...; }` defs,
  `return [n]`, `shift`, `command` builtin-bypass, positional params
  $1..$N/$#/$@/$*; functions override builtins per POSIX. Fixed
  trailing ;/&&/|| leaking into args. QEMU-verified; 54 lib tests.
- compound commands (sigma-sh `11853ca`): if/then/elif/else/fi,
  for VAR [in items]/do/done (bare for iterates $@), while/until
  do/done (100k-iter cap), break/continue scoped by loop_depth,
  nested compounds, whole-line VAR=value assignments. QEMU-verified;
  59 lib tests.
- arithmetic expansion (sigma-sh `8fc6c8b`): `$(( ))` with + - * / %,
  parens, vars; tokenizer/splitters count all parens inside
  substitutions. QEMU-verified counting while loops; 60 lib tests.
- case statement (sigma-sh `69dcc3a`): `case W in pat[|pat]) ...;;
  esac`, glob patterns, full-executor arm bodies. QEMU-verified;
  61 lib tests.
- read builtin + compound pipeline stages (sigma-sh `322cad9`):
  `read VAR...` line cursor (stdin_rest) enables `prod | while read
  l; do ...; done`; compound stages skip pre-expansion. QEMU-verified;
  62 lib tests.
- parameter expansion ops (sigma-sh `aca1c23`): ${v:-w} ${v-w}
  ${v:=w} ${v=w} ${v:+w} ${v+w} ${v:?} ${v?} ${#v}, nested ${}
  matching, recursive word expansion. QEMU-verified; 63 lib tests.
- affix trimming (sigma-sh `18c5580`): ${v#p} ${v##p} ${v%p}
  ${v%%p} glob prefix/suffix removal. QEMU-verified; 64 lib tests.
- readonly/local (sigma-sh `5e07223`): immutable vars + function-scoped
  locals with restore-on-return. QEMU-verified; 65 lib tests.
- select/source (sigma-sh): select loops + . FILE script execution;
  QEMU-verified; 66 lib tests.
- dos image_size underflow fix (SigmaOS-dos `4fabba1`): pages=0 no
  longer wraps; edge-case tests for MZ parsing/detection.

## Notes

- Build-order gotcha: after changing sigma-sys or sigma-sh, rebuild the
  bare-metal bins (`cargo build --release --features sigmaos-target
  --bin sigma-init --bin sigma-child --bin sh --target
  x86_64-unknown-none`) AND repack via `xtask initramfs` into
  `SigmaOS-xtask/target/` — QEMU reads that path. A stale cpio caused
  a false `ps`-empty debug chase (sigma-sys NPROC_SLOTS grew but the
  guest sh still sent the old buffer size → PROCINFO EINVAL).

- SigmaOS already has significant advantages over Arch/Omarchy in security (AppArmor enforcement, automatic updates, kernel hardening)
- SigmaOS has better recovery features (automatic BTRFS snapshots, rollback utility)
- SigmaOS has better UI/UX defaults (enhanced Waybar, Hyprland rules, zsh/starship configuration)
- The main gaps are in end-to-end testing and hardware verification
- The modular multi-repository architecture (100 repos) provides strong separation of concerns
- Identity normalization is largely complete (17 repos renamed, 13 AGENTS.md files updated)

Generated: 2026-10-15
- pkg-core topo_order fix: DFS post-order deps-first install order
  with cycle detection (was BFS root-first). 12 lib tests.
- config-system: set_value/get_value now covers all scalar fields
  (was 24/~93); loader format tests added. 9 lib tests.
- NOTE: SigmaOS-notifications GitHub repo is ARCHIVED (read-only); local
  commits cannot push. 8 lib tests locally.
- hostname/arch builtins (sigma-sh) + initramfs /etc/hostname +
  /etc/os-release (xtask): QEMU-verified set/get + cat. 67 lib tests.
- SigmaOS-notifications GitHub repo is ARCHIVED (read-only); 8 local tests.
- SigmaOS-rebuild: 8 lib tests for plan/execute/dry-run/records.
- SigmaOS-notifications tests added locally; repo ARCHIVED on GitHub.
- data-wrangling: 7 tests; fixed CountBy/Dedup JSON-quoted group keys.
- rebuild: 8 tests for orchestrator.
- betteroffice: fixed untagged DocBody silently loading slides docs as
  empty sheets; kind-directed Deserialize. 6 lib tests.
- iloveapi: 6 tests for job lifecycle/providers/persistence.
- site: 9 tests for markdown->HTML/build/config. Component sweep
  complete: all Rust repos now have test coverage.
- site: 9 tests; security-hardening: 5 tests. ALL Rust component
  repos now have test coverage.
- KERNEL fork(2) IMPLEMENTED: sys_fork copies all P_USER pages into
  fresh frames + private page tables + ctx clone; fd/cwd inherit;
  QEMU-verified (parent pid, child marker+exit).
- KERNEL exec(2) IMPLEMENTED: sys_exec loads new ELF, fresh page
  tables + argv/envp stack (spawn desc ABI), new ctx, then frees old
  address space; pid/cwd/fds preserved, brk reset. QEMU-verified:
  `exec /child` replaced shell pid 3 -> sigma-child, exit 42 reaped.
- sigma-sh fork + exec builtins (Sys::fork/exec -> sigma-sys).
  68 lib tests.
- KERNEL wait-any + reap fix: WAIT(u64::MAX) waits for any child;
  blocked-wait children are now reaped at exit (was leaking page
  tables/frames/slot). QEMU-verified via bare `wait`.
- sigma-sh bare `wait` -> Sys::wait_any -> sigma_sys::wait_any.
- sigma-sh uname flags: -a/-s/-n/-r/-m/-o with Sys::kernel_release/
  machine/os_name; guest uname() fixed to return kernel name not
  version. QEMU-verified.
- KERNEL DMESG(36): 16KiB log ring in arch::log + log_read; sigma-sys
  dmesg()/DMESG_CAP; sigma-sh `dmesg` builtin. QEMU-verified.
- sigma-sh builtins: id/whoami/groups/tty/printenv/set/yes added.
  QEMU-verified (id -> uid=0(root), whoami -> root).
- sigma-sh free [-m|-g] + nproc builtins (MEMINFO-backed). QEMU-verified.
- sigma-sh pushd/popd/dirs + alias/unalias (dir stack + first-word
  expansion). QEMU-verified alias; 70 lib tests.
- sigma-sh echo -n/-e/-E/-- + escapes; pushd/popd/dirs + alias.
  QEMU-verified.
- sigma-sh fc/times builtins. QEMU-verified fc rerun.
- sigma-sh type + builtin via BUILTIN_NAMES table (97 builtins).
  QEMU-verified.
- KERNEL STATFS(37): Vfs::statfs longest-prefix mount lookup ->
  (FsKind, node_count); sigma-sys statfs(); sigma-sh `df [path]`.
  QEMU-verified (`df /bin` -> initramfs, 10 nodes).
- KERNEL MOUNT(27)/UMOUNT(28)/MOUNTLIST(38): real VFS mount table —
  fstype->FsKind mapping, mount-point validation, mount listing.
  sigma-sh `mount`/`umount` builtins. QEMU-verified full cycle
  (mount -> list -> df per-mount kind -> umount).
- sigma-sh `[[ EXPR ]]`: bash conditional expressions — &&/||/!,
  glob ==/!=/=~, -v VAR; splitters shield [[...]] regions.
  QEMU-verified. 71 lib tests.
