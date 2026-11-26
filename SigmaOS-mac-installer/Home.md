# SigmaOS Mac Installer

A macOS app that installs [SigmaOS](https://github.com/AaryanSinghChauhan09/SigmaOS) on an Apple Silicon Mac, next to macOS. The app is named **SigmaOS Installer** (`org.sigmaos.installer`).

## What it does

- Inspects the Mac model, macOS version, power, FileVault state, and free disk space before asking for credentials.
- Plans the partition layout and disk allocation, requires an explicit backup confirmation, installs through a privileged helper, and finishes setup in macOS Recovery.
- Reads signed release catalogs and channels; released apps default to the `stable` channel offering SigmaOS 4.5.

## Supported Macs

Support is decided by each release's signed catalog (`scripts/supported-models.json`), not by the app alone. Covered families include M1, M2, and M3 boards plus MacBook Neo. M3 Ultra and M4-and-later boards stay fail-closed until officially supported and physically qualified.

## Install

```sh
brew install SigmaOS/mac/omarchy
```

Or download `SigmaOS-Mac-Installer-<version>.dmg` plus its `.sha256` from the [releases page](https://github.com/AaryanSinghChauhan09/SigmaOS-mac-installer/releases), verify the digest, and move the app to `/Applications`.

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-mac-installer)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
