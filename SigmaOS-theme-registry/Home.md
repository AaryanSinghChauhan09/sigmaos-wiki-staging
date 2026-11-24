# SigmaOS Theme Registry

Source of truth for the community themes listed on **themes.sigmaos.org**. Every theme here is a public GitHub repository that the SigmaOS theme installer can clone; this repo only records which ones are listed, checks them automatically, and publishes the catalog that the website reads.

## Overview

One small JSON file per theme goes in (`themes/<slug>.json`), a validated catalog and processed preview images come out and are uploaded to Cloudflare R2. The website (`SigmaOS-theme-marketplace`, Rails) and later the SigmaOS CLI only ever read the published catalog; nothing here talks to the site's database.

## Technology Stack

- **Language:** TypeScript/Node.js (Node 24, pnpm 12)
- **Validation:** Zod schemas
- **Infrastructure:** Cloudflare R2 CDN
- **Automation:** GitHub workflows for submission, validation, and health monitoring

## Submit Your Theme

1. Make a theme. The SigmaOS manual has the full guide; the short version is a public GitHub repo named `sigmaos-<name>-theme` with `colors.toml`, a `backgrounds/` folder and a 16:9 `preview.png` at its root.
2. [**Submit a theme**](https://github.com/AaryanSinghChauhan09/SigmaOS-theme-registry/issues/new?template=submit-theme.yml).
3. Within a few minutes a bot comments a validation report on the issue.
   - **Passed:** a pull request is opened for you and a maintainer merges it. The bot tells you on the issue; your theme appears on the site at the next catalog build, which runs every six hours.
   - **Needs changes:** fix what the report lists in your repo, then comment `/recheck` on the issue. No need to open a new one.

Once listed, the marketplace follows your repository's default branch: push changes and the listing updates on the next refresh (every six hours).

## Browse and Install

Browse at [themes.sigmaos.org](https://themes.sigmaos.org), or in SigmaOS with the theme browser. Each theme page has the one-line install command:

```sh
sigmaos theme install <name>
```

Installing by name checks out the commit the registry validated, and only the files SigmaOS reads; `sigmaos theme update` moves it to the next validated commit.

## What Gets Checked

The validator enforces what the SigmaOS theme installer enforces, plus a few things that make a good listing.

**Errors** — repository missing or private; theme not at the repo root; symlinks; no palette (`colors.toml`) or one missing required keys; no `preview.png` at the root, or narrower than 1000 px; images over 50 MB / 40 MP; repository over 400 MB; an install name SigmaOS refuses.

**Warnings** — archived repo; files SigmaOS drops on install; undeclared or conflicting `mode`; heavy or oddly named backgrounds; no README or LICENSE; no `sigmaos-theme` topic; unconventional repo name; scripts or binaries in the repo.

## Architecture

- `packages/schema` — Zod schemas and constants: `RegistryEntry`, `Overrides`, `CatalogTheme`/`Catalog`, `ValidationReport`
- `packages/validator` — `validateTheme` (errors block, warnings publish), `installedFiles`, `deriveSlug`/`assignSlug`, palette parsing and hue bucketing, repo inspection, `GithubClient`
- `scripts/` — `validate.ts`, `submit.ts`, `build-catalog.ts`, `upload.ts`, `lib.ts`
- `themes/*.json` entries, each pinned to its GitHub `repo_id`
- `overrides/featured.json` + `hidden.json` (curator-only)

## Automation (`.github/workflows`)

- `submit.yml` — issues from the "Submit a theme" form and `/recheck` comments
- `published.yml` — when a submission PR merges: notify and close the issue
- `validate-pr.yml` — PRs touching `overrides/` only
- `build.yml` — on push to master, every 6 h, and on dispatch: build and upload to R2
- `ci.yml` — lint, type-check, tests

## Working Locally

Node 24, pnpm 12, `just`:

```sh
just install
just check                    # lint, type-check, tests
just validate <url|slug>      # one repo, same rules as the build
just submit <repo> <login>    # dry-run a submission (--write creates the entry)
just build                    # full catalog into dist/v1
just upload-dry               # what would go to R2
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-theme-registry)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
