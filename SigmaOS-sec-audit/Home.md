# SigmaOS Security Audit

Read-only security scanner for SigmaOS — walks a directory tree and
reports permission and secret-hygiene findings. No writes, no deps
beyond walkdir/serde/thiserror.

## Overview

`SigmaOS-sec-audit` recursively scans a root and emits an
`AuditReport` of `Finding`s with `Info`/`Warning`/`Critical`
severity:

- **permissions**: world-writable files (warning); private-key file
  names (`id_rsa`, `id_ed25519`, `.pem`, …) readable by group/other
  (critical); setuid/setgid bits (info)
- **secrets**: text files ≤ 1 MiB containing patterns like
  `PRIVATE KEY-----`, `aws_secret_access_key`, `api_key =`,
  `password =` (warning, one finding per file)

`AuditReport::has_critical`/`count` summarize results and
`render_text` produces a human-readable report.

## Features

- **Recursive scan** via walkdir (no symlink following)
- **Severity model** with per-category counts
- **Tests**: 6 unit tests cover world-writable warnings, loose vs
  tight private-key perms, secret detection, setuid info findings,
  clean trees, and report rendering

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-sec-audit)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
