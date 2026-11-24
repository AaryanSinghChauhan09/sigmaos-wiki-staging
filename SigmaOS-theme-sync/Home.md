# SigmaOS Theme Sync

Use your SigmaOS desktop colors on the web.

SigmaOS Theme Sync is a Chromium extension that shares your current theme with websites through CSS variables and a small JavaScript API. Change your desktop theme, and pages that use these colors update without a reload.

## Overview

It does not automatically restyle every website. Each site chooses how to use the colors.

## Install

You need a SigmaOS desktop and Chromium. There is no build step and no npm install. The installer runs as your normal user, without `sudo`.

1. Open Chromium at least once so its profile exists.
2. Clone the project and run the installer:

```bash
git clone https://github.com/AaryanSinghChauhan09/SigmaOS-theme-sync.git
cd SigmaOS-theme-sync
./install.sh
```

3. Fully quit and restart Chromium.
4. Open `chrome://extensions` and check for **SigmaOS Theme Sync**.

Keep the project folder in place. The browser loads the extension and its local helper directly from this folder.

## Use Colors in CSS

The extension adds CSS variables to the page's `<html>` element:

```css
.card {
  background: var(--sigmaos-background, #101913);
  color: var(--sigmaos-foreground, #a1af9c);
  border: 1px solid var(--sigmaos-accent, #4a9a68);
}
```

Always include a fallback color. Your site should still work when the extension is not installed.

Color names come from the theme's `colors.toml` file. Underscores become hyphens: `bright_green` becomes `--sigmaos-bright-green`.

The `<html>` element also gets `data-sigmaos-theme` and `data-sigmaos-mode` attributes for the theme name and light or dark mode.

## Use the JavaScript API

Check for `window.sigmaos` before using it:

```js
const api = window.sigmaos;

if (api) {
  console.log(api.theme);           // Theme name
  console.log(api.mode);            // "light" or "dark"
  console.log(api.color('accent')); // One color
  console.log(api.colors());        // All colors

  const stop = api.onChange((colors) => {
    console.log('Theme colors updated:', colors);
  });

  // Call stop() when your component or view is removed.
}
```

The palette arrives asynchronously. Initial reads can be empty; `onChange` also fires when the first palette arrives.

## Try the Demo

From the project folder, run:

```bash
python3 -m http.server 8080 --bind 127.0.0.1 --directory demo
```

Open [http://localhost:8080](http://localhost:8080). In another terminal, switch to a theme you have installed.

## Security and Privacy

Every page where the extension runs can read your theme name and palette. Custom colors can help identify you across sites. There is no per-site read opt-in yet.

An allowed write origin can change your theme without a confirmation prompt. Only add origins you trust.

## Development

The project uses plain JavaScript and Bash. No bundler or package installation is required.

| Path | Purpose |
| --- | --- |
| `extension/` | Chromium extension and page API |
| `bin/sigmaos-browser-theme-host` | Local helper that reads and applies themes |
| `demo/` | Live demo and example palettes |
| `install.sh` | Browser registration and removal |
| `tests/` | Security and behavior regression tests |

Run the tests from the project folder:

```bash
node --test tests/*.test.mjs
```

## Uninstall

Run this before deleting or moving the project folder:

```bash
./install.sh --uninstall
```

Restart the browser. This removes the browser registration, not themes you previously installed or the helper's rate-limit state.

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-theme-sync)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
