# SigmaOS-xtask

Build runner and QEMU orchestrator (`cargo xtask` equivalent as a
standalone `xtask` binary). Commands: `build-kernel` (x86_64-unknown-
none), `build-userspace` (host `sigma-sh` plus `sigmaos-target`
`sigma-init`/`sigma-child` for x86_64-unknown-none), `initramfs`
(cpio newc writer packing native `/init` and `/child` only),
`kernel-elf`
(links MB2 header via sigma-bootloader), `qemu` / `qemu-debug`
(q35, serial stdio, optional isa-debug-exit timeout), `test-qemu`,
`status` (toolchain + repo presence report). Root auto-detected via
`--root`, `$SIGMAOS_SRC`, or sibling layout.
