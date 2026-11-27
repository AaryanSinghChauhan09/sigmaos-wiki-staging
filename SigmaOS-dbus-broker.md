# SigmaOS-dbus-broker

**Category:** System | **Language:** Rust | **License:** GPL-3.0-or-later | **Status:** Stable

## Purpose

D-Bus message broker state tracker for SigmaOS. Maintains an in-process registry of system and session bus service entries — unique names, PIDs, and bus membership — without requiring a live D-Bus daemon for logic verification.

## Features

- **Dual-bus registry** — tracks `System` and `Session` bus services independently
- **Unique-name tracking** — maps well-known names to `:1.N` unique names and PIDs
- **Bus-scoped filtering** — `services_on_bus()` returns all registrations on a given bus
- **Safe registration** — rejects duplicate names with typed errors

## API

| Function | Description |
|---|---|
| `register(entry)` | Register a service entry |
| `unregister(name)` | Remove a service by well-known name |
| `lookup(name)` | Retrieve service entry by name |
| `services_on_bus(bus)` | List all services on a given bus |
| `service_count()` | Total registered services |

## Errors

| Error | Condition |
|---|---|
| `AlreadyRegistered(name)` | Duplicate name registration |
| `NotFound(name)` | Lookup/unregister of unknown service |

## Tests

6 AAA unit tests covering: register+lookup, duplicate rejection, bus filtering, unregister cleanup, unregister-nonexistent, service count.

## See Also

- [SigmaOS-session-manager](SigmaOS-session-manager) — user session lifecycle
- [SigmaOS-notification-daemon](SigmaOS-notification-daemon) — notification dispatch
- [SigmaOS-service-supervisor](SigmaOS-service-supervisor) — service lifecycle supervision
