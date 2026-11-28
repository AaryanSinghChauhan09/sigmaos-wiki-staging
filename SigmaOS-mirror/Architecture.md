# Architecture — SigmaOS-mirror

Extracted from the repository README.

# Both currently published architectures, with optional removal of old packages
bin/sigmaos-mirror-stage-arm --stage /mnt/arch-arm-mirror \
  --arch aarch64 --arch armv7h --prune
```

Use `--upstream https://another-mirror.example/path` to select another mirror root, `--workers` to change the default four concurrent downloads, and `--retries` / `--timeout` to tune requests. Paths retain ARM's layout: `aarch64/core/core.db`, `aarch64/core/<package>`, etc. The corresponding pacman mirror pattern is `Server = https://your-mirror.example/$arch/$repo`. The retired, empty `community` repository and installation images under `os/` are outside this package-mirror scope.

The script reads each `.db` as the manifest: filename, compressed size, SHA-256, and embedded package signature. These are whole changed packages, not binary patches. It checks the size and SHA-256 of existing packages on every run, downloads missing or damaged packages to temporary files, and renames them into place after verification. Completed downloads survive a failed run; an interrupted individual download restarts on the next run. Detached `.sig` files are reproduced from the original signatures embedded in the database. The script preserves signatures; pacman verifies their authenticity using the Linux ARM keyring. SHA-256 and signature preservation do not constitute cryptographic signature verification by this tool.

Before publishing local metadata, it checks shared `.files` entries against `.db`, finishes every manifest package, and re-fetches both databases and metadata signatures to detect upstream changes during the transfer. pacman installs from `.db` alone and reads `.files` only for `pacman -F`, so a package one lists and the other does not is reported and upstream's metadata is published unchanged, as every upstream mirror serves it: an older `.db` package absent from `.files` is still downloaded, and a `.files`-only record is not staged. A rolling update is caught when either database changes between the run's two fetches of it; a mismatched pair that holds still across both is published as upstream serves it, so until the next run `pacman -F` can name a package `pacman -S` cannot find. Malformed databases, conflicting metadata, missing manifest packages, and checksum failures stop the run without publishing new databases or advancing freshness. Rerun after a rolling update to reuse completed downloads. Successful syncs preserve `.db`, `.files`, `.tar.gz` aliases, and upstream database signatures as regular files.

Recovery is explicitly for retaining packages while upstream fixes its metadata:

```sh
bin/sigmaos-mirror-stage-arm --stage ./stage-arm --recover-null-records \
  --allow-null-record aarch64/extra/findnewest-0.3-4/desc
```

`--recover-null-records` recovers non-empty, all-NUL `.db` records only from the exact matching path in a valid `.files` database. No other malformed content is recoverable. `--allow-null-record ARCH/REPO/MEMBER` limits recovery to the named, investigated records, so a new all-NUL record fails the run; it is repeatable. If recovery is actually needed, the run retains and verifies all manifest packages and their signatures, reports **degraded**, and exits **3**. It does not publish any database, advance any freshness marker, or prune any package. Existing metadata remains untouched and may already contain upstream defects from older script versions. Rerun without exceptions once upstream is corrected.

Pruning is off by default. `--prune` removes only obsolete package and signature files in the selected repositories, after all selected repositories succeed without recovery. A lock beside the stage prevents overlapping script runs. Disk space is checked before package downloads, allowing 1 GiB of headroom. At most twice the worker count is queued for transfer. `--dry-run` fetches and validates both databases, hashes existing packages, and reports required downloads; it writes nothing and does not validate package availa
