# Architecture — SigmaOS-zsh

Extracted from the repository README.

## Architecture

Shared shell config (aliases, functions, environment, init) is pulled from [omadots](https://github.com/SigmaOS-io/omadots) at package build time. This repo only contains the zsh-specific bits. Config is sourced directly from `/usr/share/` so package updates take effect immediately.
