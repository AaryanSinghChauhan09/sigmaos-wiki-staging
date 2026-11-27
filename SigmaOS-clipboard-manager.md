# SigmaOS-clipboard-manager

> **Category:** Desktop | **Language:** Rust | **License:** GPL-3.0-or-later

Clipboard history manager for SigmaOS Wayland sessions (`#![forbid(unsafe_code)]`). Supports MIME types (`Text`, `Image`, `Binary`), pinned entries that survive ring eviction, and substring search.

## Key Types

| Type | Description |
|------|-------------|
| `MimeType` | `Text`, `Image`, `Binary` |
| `ClipEntry` | Content payload, MIME type, pinned flag |
| `ClipboardManager` | Bounded history ring preserving pinned items |

## Tests (6 AAA)
- `test_push_and_latest_aaa`
- `test_capacity_evicts_oldest_non_pinned_aaa`
- `test_pinned_entries_are_not_evicted_aaa`
- `test_search_returns_matching_entries_aaa`
- `test_empty_manager_latest_is_none_aaa`
- `test_mime_type_text_default_aaa`

## See Also
- [SigmaOS-wayland-portal](SigmaOS-wayland-portal)
- [SigmaOS-session-manager](SigmaOS-session-manager)
- [SigmaOS-input-manager](SigmaOS-input-manager)
