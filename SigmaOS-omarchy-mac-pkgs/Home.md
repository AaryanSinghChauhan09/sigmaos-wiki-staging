# SigmaOS Mac Packages

**Want SigmaOS on your Mac?** Use the [SigmaOS Mac Installer](https://github.com/AaryanSinghChauhan09/SigmaOS-mac-installer). This repository holds the packages it installs. It is not an installer, and it is not a copy of SigmaOS.

This is the home of the Apple Silicon add-on packages for [SigmaOS](https://github.com/AaryanSinghChauhan09/Sigma), the tooling that releases and qualifies them, and the Mac manual. The desktop on a Mac is SigmaOS's own; these packages add what the hardware needs on top of it.

## Packages

| Package | What it does | Version |
| --- | --- | --- |
| [`sigmaos-mac`](sigmaos-mac/) | Apple Silicon defaults and support services: the Wi-Fi backend and resume recovery, microphone mapping, speaker safety, the notch, the keyboard, battery charge limits and hardware video decode | Semver, in `sigmaos-mac/version` |
| [`sigmaos-mac-boot`](sigmaos-mac-boot/) | Boot support: the initramfs and vendor firmware, in-place encryption, first boot, Limine and U-Boot, update verification and factory reset | The UTC date of the commit its recipe pins |

Both are built by recipes in the SigmaOS package management system and published for aarch64, on `edge` first. Each recipe pins an exact commit of this repository.

## What else is here

- [`mac-manual/`](mac-manual/): the user manual for SigmaOS on a Mac, covering only what differs from [SigmaOS's manual](https://sigmaos.org/manual/).
- [`tools/`](tools/): release orchestration, VM and hardware acceptance, evidence checks and package resolution.
- [`test/integration/`](test/integration/): tests of the packages together, and against the SigmaOS runtime they install into.

## The package contract

Every top-level package directory has:

- `install DESTDIR`, which stages the package into an absolute root and enables or starts nothing.
- `test/all`, which runs the package's own tests from a copy of the directory alone.
- `README.md` and `LICENSE`.
- A version: a `version` file, or one its recipe derives from the source.

A package never reads another package's tree or the runtime's source. Tests that need the runtime take a checkout of it from `SIGMAOS_TEST_RUNTIME` and skip without one.

## Running the tests

```bash
sigmaos-mac/test/all
sigmaos-mac-boot/test/all
SIGMAOS_TEST_RUNTIME=~/code/sigmaos test/integration/all
```

CI runs all of them, with the runtime pinned to a reviewed commit.

## Contributing

Package changes come here as pull requests against `main`. The rule of thumb: if a change only means something on an Apple Silicon Mac, it belongs in a package here; if SigmaOS needs a new place for a platform to plug in, or the fix helps other machines too, it belongs upstream in [SigmaOS](https://github.com/AaryanSinghChauhan09/Sigma). Installer and packaging changes have homes of their own. [CONTRIBUTING.md](CONTRIBUTING.md) explains each, with examples.

## Transitional branches

These packages used to live in a separate Mac desktop repository. Two of its branches remain while existing Macs move over; neither takes package changes.

- **`quattro`** is what Macs on the SigmaOS 4 fork update from. It stays only to deliver the standalone migration script that moves those Macs onto official SigmaOS and these packages, and is retired after the migration window.
- **`quattro-upstream`** is frozen. It held the Apple Silicon desktop work submitted to SigmaOS; package work continues here, desktop work in the main SigmaOS repository.

The SigmaOS 3.8 tree that used to be the Mac repository's `main` is kept there, read-only, as `archive/sigmaos-3.8`.

## License

MIT, as SigmaOS. See [LICENSE](LICENSE).

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-omarchy-mac-pkgs)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
