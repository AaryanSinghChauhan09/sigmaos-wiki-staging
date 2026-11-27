# SigmaOS Security Model

> Defense-in-depth, memory safety, least privilege, and cryptographic verification across all SigmaOS components.

## Core Security Principles

1. **Memory Safety (`#![forbid(unsafe_code)]`)**
   All userspace Rust components enforce `#![forbid(unsafe_code)]` at the crate root, eliminating undefined behavior, buffer overflows, and use-after-free vulnerabilities at compile time.

2. **Least Privilege & Sandboxing**
   - **`SigmaOS-app-env`**: Defines isolated application runtime profiles with explicit filesystem mount modes (`ro`/`rw`), environment allowlists, and opt-in network access.
   - **`SigmaOS-local-ai`**: Runs local model containers rootless with read-only root filesystems, dropped Linux capabilities, internal-only networks, and authenticated loopback endpoints.
   - **AppArmor & Mandatory Access Control**: System services and user applications are confined to minimal required capabilities via **`SigmaOS-security-hardening`**.

3. **Cryptographic Verification & Signing**
   - **`SigmaOS-signed`**: Artifact and package signature verification before installation or execution.
   - **`SigmaOS-openpgpkey`**: OpenPGP key management and trust verification for system packages and repositories.

4. **Continuous Security Auditing**
   - **`SigmaOS-sec-audit`**: Automated security auditing for configuration drift, unsafe permissions, exposed secrets, and policy compliance.
   - **Zero Hardcoded Secrets**: Passwords, tokens, and API keys must never be committed to source code; runtime secrets are injected via environment variables or secure keychains.
   - **Secure Defaults**: Production builds disable debug flags by default and fail closed on validation errors.

## Reporting Vulnerabilities
Report security issues privately through the repository's security advisory channel without exposing exploit details in public issues.

## Capability-Based Security (Added 2026-11)
- **[SigmaOS-pledge-caps](SigmaOS-pledge-caps)** — pledge/unveil-style capability confinement; processes declare required capabilities at startup
- **[SigmaOS-audit-log](SigmaOS-audit-log)** — cryptographically signed audit event journal; tamper-evident log ring with SHA-256 chaining
- **[SigmaOS-crypto-keys](SigmaOS-crypto-keys)** — PKI key management: generate, store, rotate Ed25519/RSA keys under `/etc/sigma/pki`
- **[SigmaOS-wayland-portal](SigmaOS-wayland-portal)** — Wayland XDG portal integration; enforces sandboxed file/screen access for desktop apps
