# SigmaOS Omafind

Local, on-device **semantic** file search — press `SUPER + CTRL + G`,
describe what you're looking for, and Omafind finds it. Nothing leaves
the machine.

## Capabilities

- Natural-language queries over photos, screenshots (OCR text), PDFs
  (including scans), documents (txt/md/html/docx/odt/epub), audio,
  video, and opt-in code
- Finds the moment in a recording or the page in a PDF, with the
  matched passage shown under a preview
- GPUI Kit window + Hyprland 0.56 (Lua config) integration
- llama.cpp-backed local embeddings/ranking (`omafind-core::ranking`)
- Daemon architecture; UI drivable from an agent shell

## Structure

- `omafind-core` - indexing, ranking, query engine
- `omafind-app` - GPUI Kit window (excluded from workspace clippy; needs
  the full GUI system-lib stack)
- `SIGMAOS_FORK.md` - fork provenance (MIT, from SigmaOS/omafind)

## Build & Test

```sh
./scripts/fetch-engine.sh cpu   # llama.cpp headers for omafind-app
cargo clippy --workspace --exclude omafind-app -- -D warnings
cargo test --workspace --exclude omafind-app
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-omafind)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
