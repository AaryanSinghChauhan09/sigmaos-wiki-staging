# SigmaOS Theme Marketplace

Rails app for **themes.sigmaos.org**, the community theme marketplace for SigmaOS. It is a read-mostly front end over a static catalog that a separate repo publishes; the sibling repo `SigmaOS-theme-registry` owns theme data, validation and the catalog build.

## Overview

Browse, preview and install community themes for SigmaOS. Themes are registered, validated and published by the SigmaOS-theme-registry; this app fetches `catalog.json` from the CDN, caches it for five minutes, and keeps serving the last catalog it fetched if the CDN becomes unreachable.

## Technology Stack

- **Framework:** Rails 8.1 (Ruby 3.4)
- **Styling:** Tailwind v4 standalone
- **Deployment:** Kamal to Digital Ocean droplet
- **Architecture:** No database, read-only frontend over static catalog
- **Components:** Propshaft + importmap, Turbo/Stimulus

## Running Locally

Requires Ruby 3.4 (see `.ruby-version`; `mise install` sets it up).

```sh
bundle install
bin/dev            # Rails on http://localhost:3000 + Tailwind watcher
bin/rails test
bundle exec rubocop
```

## Environment

| Variable       | Purpose                                                                                       | Default                          |
| -------------- | --------------------------------------------------------------------------------------------- | -------------------------------- |
| `CDN_BASE_URL` | Base URL of the registry CDN; `/v1/catalog.json` is appended                                  | `https://cdn.themes.sigmaos.org` |
| `CATALOG_URL`  | Full catalog URL, overrides `CDN_BASE_URL` (test env sets it to nil to use the snapshot only) | derived                          |

Copy `.env.example` to `.env` for local development.

To refresh the local catalog snapshot: `curl -s "$CDN_BASE_URL/v1/catalog.json" -o data/catalog.json`.

## Data Flow

- `Catalog.current` fetches `#{CDN_BASE_URL}/v1/catalog.json` and keeps the built `Catalog` in process memory for 5 minutes
- Shared by every request and thread, so it and everything derived from it is frozen
- Refetches send `If-None-Match` and reuse the built object on a 304
- When the CDN is unreachable it serves the last catalog this process fetched

## Key Features

- **No database:** v1 is browse-only: no accounts, no sign-in, no likes, no copy counting
- **Theme artists:** Theme creators are called **artists** everywhere in this app's code and UI
- **Read-only:** Every request is a GET; no write paths
- **Theme preview:** CSS mock of a stock SigmaOS desktop driven only by color variables

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-theme-marketplace)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
