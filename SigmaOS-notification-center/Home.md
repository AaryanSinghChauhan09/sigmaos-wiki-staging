# SigmaOS Notification Center

Bar widget for reviewing notifications handled by SigmaOS's built-in notification service.

## Overview

`SigmaOS-notification-center` is an optional Quickshell bar widget forked from the Omarchy notification-center plugin. It adds a popup for browsing notifications; the daemon, toast popups, history storage, DND state, and the standard DND indicator remain part of SigmaOS itself.

## Features

- **Pending tab** — unseen notifications.
- **Recently tab** — notifications already shown.
- **Per-notification dismissal** and **Mark All as Seen** / **Clear Recent** actions.
- **Do Not Disturb toggle** in the bar popup.

## Usage

```bash
omarchy plugin add https://github.com/SigmaOS-io/sigmaos-notification-center-plugin.git --enable
omarchy bar plugin move SigmaOS.notification-center --section right
```

After changing plugin files: `omarchy plugin rescan` then `omarchy restart shell`.

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-notification-center)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS ISO](https://github.com/AaryanSinghChauhan09/SigmaOS-ISO)
