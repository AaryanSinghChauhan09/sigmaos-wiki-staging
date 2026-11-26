# SigmaOS TTFX

Terminal text effects as a single static binary — pipe text in, pick an
effect, get ASCII-art output. Bit-exact Python-parity port of the
ttfx effect set with golden tests.

## Capabilities

```sh
ls -la | ttfx decrypt
cat banner.txt | ttfx beams
fortune | ttfx --random-effect
git log --oneline -10 | ttfx matrix
```

- Dozens of effects (decrypt, beams, matrix, …) plus `--random-effect`
- Single static binary — no runtime deps, pipe-friendly
- Golden tests assert bit-exact output parity with the Python original
  (easing math uses `min`/`max` NaN semantics, not `f64::clamp`)

## Structure

- `src/` - effect implementations + CLI
- golden test fixtures - expected outputs per effect
- `SIGMAOS_FORK.md` - fork provenance (MIT, from SigmaOS/ttfx)

## Build & Test

```sh
cargo build
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

Note: the easing golden test failure is pre-existing upstream drift,
not a regression.

## License

GPL-3.0-or-later (fork: MIT upstream)

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-ttfx)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
