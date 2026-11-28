# Architecture — SigmaOS-plugin-registry

Extracted from the repository README.

## Architecture in one paragraph

The Rails app handles accounts (passwordless — emailed one-time codes like
Cortex/Herald, with a mandatory second factor for publishers: passkeys with
required user verification, or TOTP), namespaces
(`publisher/name`, first-claim), publishing (short-lived scoped tokens; OIDC
trusted publishing later), review, and admin (quarantine / yank / kill-bit).
On every accepted publish it regenerates static index files and freezes the
tarball — installs never touch Rails in the hot path. Clients
(`sigmaos plugin add publisher/name`) fetch index + tarball from the CDN,
verify checksums, and check a tiny signed `revocations.json` kill list.
