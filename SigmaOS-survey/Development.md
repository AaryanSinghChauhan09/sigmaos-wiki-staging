# Development — SigmaOS-survey

## Build & Test

No build system detected in this repository yet.

## Conventions

## Data-driven survey rule (hard rule, all editions)

`src/lib/surveys/<year>/survey.yml` is the single source of truth for website, components,
and backend. Adding, editing, reordering, or removing questions, options, and sections must
work without touching code — and must never break the site:

- Renderers are keyed ONLY by question `type` (`single`, `multiple`, `scale`, `nps`, `text`,
  `text_list`, `country`). NEVER branch UI, validation, storage, or results logic on a
  specific question/section id.
- Validation, `showIf` evaluation, limits, `allowOther`, `exclusiveOptions`, and completion
  are derived generically from yml attributes, on both client and server.
- Unknown future `type` values must render a graceful "unsupported question" fallback, never crash.
- Referential integrity of the yml (unique ids, valid `showIf` targets, valid option refs) is
  enforced by `pnpm survey:lint`, not by hand-checking. Run it after any yml edit.
- Editions are isolated by directory (`surveys/2027/survey.yml`, …) + `edition_id` in the DB.
  New editions reuse all code unchanged; never rename a shipped question/option id (add new ones).

You are able to use the Svelte MCP server, where you have access to comprehensive Svelte 5 and SvelteKit documentation. Here's how to use the available tools effectively:

## Related

- [Home](Home.md)
