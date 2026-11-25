# Console, Input & Initramfs

Boot path now reaches userspace: the kernel mounts the initramfs
cpio into its VFS and opens an interactive console.

## VGA text console (`src/console.rs`)

`TextConsole<B: ScreenBuf>` — an 80x25 text console over a generic
cell buffer (testable without hardware). Features: scroll region,
newline, backspace, scrollback-free scrolling, `attr::make` colors
(fg/bg/bright/blink nibbles). `VgaBuf` in `arch.rs` maps it onto
the memory-mapped VGA buffer at `0xB8000` (u16 cells: ASCII +
attr byte).

## PS/2 keyboard (`src/ps2.rs`)

`Keyboard` decodes i8042 scancode set 1: make/break codes, shift,
caps-lock and ctrl modifiers, `Key::Char(char)` / `Enter` /
`Backspace` events. `Ps2Port` trait abstracts port I/O; `Ps2Hw`
in `arch.rs` does the real `inb`/`outb` on ports 0x60/0x64.

## Initramfs in the boot path

`boot_ok` scans PVH modules for the `070701` cpio newc magic,
loads it via `vfs::load_cpio_newc` into a `Vfs`, and prints the
node tree. `/init` (sigma-sh, ~580 KB) is present in the image.

## Boot sequence now

```
PVH entry -> long mode -> IDT -> parse_pvh
  -> log memory regions
  -> mount initramfs cpio into VFS
  -> VGA banner + keyboard->console/serial echo loop
```

Bugs fixed along the way: xtask's `hex8_usize` emitted raw bytes
instead of ASCII hex (no parser could read its archives), and the
cpio trailer used `ino=1` so the `ino==0&&check==0` trailer check
never fired — now detected by name `TRAILER!!!` and xtask writes
`ino=0` per spec.
