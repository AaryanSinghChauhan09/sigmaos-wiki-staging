# Development — SigmaOS-plugin-marketplace-tools

## Build & Test

```sh
rg -n '\?v=' site/*.html site/assets/js/*.js
```

## Conventions

## Frontend and design rules

Use the existing HTML, CSS, and JavaScript patterns. Reuse design tokens and existing components before adding new ones.

Preserve the visual language:

- Monospace typography for navigation, commands, identifiers, and technical metadata
- Black and neutral surfaces with restrained orange accents
- Thin borders, square controls, clear spacing, and no decorative clutter
- Strong information hierarchy without oversized promotional elements
- Existing dark and light themes

Keep interface copy short and functional. Match nearby capitalization and terminology. Do not translate the English interface unless the maintainer requests it.

The Ko-fi support action uses `https://ko-fi.com/hancore`. Keep it directly before **Browse plugins** in the desktop header. It uses the same dimensions and typography as the other navigation links, an orange status dot, and the established orange hover treatment. Keep **Browse plugins** visually primary; utility links may use the muted text color. Support is a desktop-header action; do not add it to the mobile bottom navigation unless the maintainer requests it.

External links that open a new tab must use `target="_blank"` and `rel="noreferrer"`. Add an accessible name when the visible label does not fully describe the destination.

## Related

- [Home](Home.md)
