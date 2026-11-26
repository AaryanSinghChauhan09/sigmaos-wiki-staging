# SigmaOS Mac VM

Runs stock SigmaOS in a fast virtual machine on an Apple Silicon Mac, bridged to macOS so it can be used as a daily driver or as a low-commitment way to try SigmaOS before a native install.

## Capabilities

- Guest is stock SigmaOS; the repo holds the Mac-side app, VM runtime, and the single `sigmaos-mac-vm` guest package — no SigmaOS files are modified.
- macOS integrations include universal clipboard, AirPods, Touch ID, Retina display, Super shortcuts, clipboard, audio, camera, battery, and a shared folder.
- Package upgrades must work offline; the guest is treated as untrusted and everything the Mac side receives from it is validated.
- Canonical branch: `main`. See the repository README, `manual/`, and `docs/architecture.md` for usage and design.

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-mac-vm)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
