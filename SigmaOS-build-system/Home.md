# SigmaOS Build System

Reproducible build orchestration library — TOML `BuildManifest` →
per-package builds → verification, Arch `PKGBUILD`-aware.

## Capabilities

- `BuildManifest`: name/version/description + package list +
  `BuildOptions` (parallel, clean, verbose, reproducible)
- `BuildSystem::build()` — optional clean (`build/` + `target/` wipe),
  builds each package via `PackageBuilder`, then runs
  `BuildVerifier::verify_build`
- `BuildVerifier` — manifest sanity (name/version non-empty),
  per-package `packages/<name>/` + `PKGBUILD` presence, and
  `build/<name>/` output checks; collects errors/warnings into
  `VerificationResult { valid, errors, warnings }`
- `verify_build_at(manifest, root)` — verify against an explicit root
  for tests/chroots; `verify_build` defaults to `.`
- `PackageBuilder` supports multiple `PackageFormat`s

## Structure

- `src/builder.rs` - manifest, options, BuildSystem orchestration
- `src/package.rs` - package build formats
- `src/verifier.rs` - manifest/package/checksum verification
- `src/main.rs` - thin CLI stub (library is the product)

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

3 verifier unit tests (valid tree, missing package dir, empty name).

## License

GPL-3.0-or-later

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-build-system)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
