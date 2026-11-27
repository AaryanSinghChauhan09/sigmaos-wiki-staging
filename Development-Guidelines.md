# SigmaOS Development Guidelines

Comprehensive engineering, architectural, systems, testing, security, and identity rules for all SigmaOS contributors and AI agents. Every principle below includes a concise definition, applicability boundaries, a SigmaOS-specific example, and a Rust (or configuration) snippet where applicable.

## Table of Contents

1. [Software Engineering](#1-software-engineering)
2. [Architecture](#2-architecture)
3. [OS / Systems](#3-os-systems)
4. [Testing](#4-testing)
5. [Development Practices](#5-development-practices)
6. [SigmaOS-Specific](#6-sigmaos-specific)
7. [Security](#7-security)
8. [Code Reuse](#8-code-reuse)
9. [Identity](#9-identity)

---

## 1. Software Engineering

### 1.1 SOLID: Single Responsibility Principle (SRP)
- **Definition**: Every module, struct, or function should have one—and only one—reason to change.
- **When to apply**: When designing crates, services, structs, or functions that might otherwise mix I/O, business logic, and formatting.
- **When NOT to apply**: Do not fracture a trivial 10-line helper into multiple files or types just to satisfy an abstract rule.
- **SigmaOS-specific example**: In `sigma-system`, keep `COMPONENT.toml` manifest parsing separate from repository network synchronization.
- **Code snippet**:
```rust
pub struct ManifestParser;
impl ManifestParser {
    pub fn parse(raw: &str) -> Result<ComponentManifest, ParseError> { /* ... */ todo!() }
}

pub struct ComponentSync;
impl ComponentSync {
    pub fn sync(manifest: &ComponentManifest) -> Result<(), SyncError> { /* ... */ todo!() }
}
```

### 1.2 SOLID: Open/Closed Principle (OCP)
- **Definition**: Software entities should be open for extension but closed for modification.
- **When to apply**: When adding new formats, drivers, backends, or theme providers without editing core dispatch logic.
- **When NOT to apply**: When there is only one implementation and no foreseeable need for plugins or variants (YAGNI).
- **SigmaOS-specific example**: `SigmaOS-theme-registry` defines a `ThemeExporter` trait so new desktop targets can be added without modifying the core registry engine.
- **Code snippet**:
```rust
pub trait ThemeExporter {
    fn export(&self, theme: &ThemeSpec) -> Result<String, ExportError>;
}

pub fn run_export(exporter: &dyn ThemeExporter, theme: &ThemeSpec) -> Result<String, ExportError> {
    exporter.export(theme)
}
```

### 1.3 SOLID: Liskov Substitution Principle (LSP)
- **Definition**: Any subtype or trait implementation must be substitutable for its base type without altering correctness or violating invariants.
- **When to apply**: Whenever implementing shared Rust traits across multiple drivers, storage backends, or package providers.
- **When NOT to apply**: When two types share superficial method names but have incompatible semantic contracts—use separate traits instead.
- **SigmaOS-specific example**: Every `PackageBackend` implementation in `SigmaOS-update-system` must honor idempotent `install()` semantics so callers never need backend-specific workarounds.
- **Code snippet**:
```rust
pub trait PackageBackend {
    /// Must be idempotent: installing an already-present package succeeds with Ok(false).
    fn install(&self, pkg: &str) -> Result<bool, PkgError>;
}
```

### 1.4 SOLID: Interface Segregation Principle (ISP)
- **Definition**: Clients should not be forced to depend on methods or interfaces they do not use.
- **When to apply**: When a large trait forces read-only consumers or lightweight tools to stub out write or lifecycle methods.
- **When NOT to apply**: When a trait has 2–3 tightly cohesive methods that every implementer genuinely needs together.
- **SigmaOS-specific example**: Split `ComponentStore` into `ComponentReader` (used by `sigma-sh` status queries) and `ComponentWriter` (used by `SigmaOS-update-system`).
- **Code snippet**:
```rust
pub trait ComponentReader {
    fn get_status(&self, name: &str) -> Result<ComponentState, StoreError>;
}

pub trait ComponentWriter {
    fn set_status(&mut self, name: &str, state: ComponentState) -> Result<(), StoreError>;
}
```

### 1.5 SOLID: Dependency Inversion Principle (DIP)
- **Definition**: High-level policy modules should not depend on low-level implementation details; both should depend on abstractions.
- **When to apply**: When core SigmaOS orchestrators interact with filesystems, databases, or network transports.
- **When NOT to apply**: In small leaf utilities where abstracting `std::fs` adds boilerplate with zero testability or portability gain.
- **SigmaOS-specific example**: `SigmaOS-xtask` depends on a `RepoRunner` trait rather than hardcoding shell subprocess calls directly into orchestration logic.
- **Code snippet**:
```rust
pub trait RepoRunner {
    fn run_checks(&self, repo_path: &str) -> Result<(), CheckError>;
}

pub fn audit_all(runner: &dyn RepoRunner, repos: &[&str]) -> Result<(), CheckError> {
    for r in repos { runner.run_checks(r)?; }
    Ok(())
}
```

### 1.6 DRY (Don't Repeat Yourself)
- **Definition**: Every piece of knowledge or business logic must have a single, unambiguous, authoritative representation in the system.
- **When to apply**: When the same validation, serialization, or domain rule is duplicated across two or more modules or repos.
- **When NOT to apply**: When two blocks look syntactically similar by coincidence but represent independent domain concepts that will evolve differently.
- **SigmaOS-specific example**: Centralize `COMPONENT.toml` schema validation in `sigma-system` instead of copying parsing code into every SigmaOS repository.
- **Code snippet**:
```rust
pub fn validate_component_name(name: &str) -> Result<(), ValidationError> {
    if name.starts_with("SigmaOS-") && name.len() > 8 { Ok(()) } else { Err(ValidationError::InvalidName) }
}
```

### 1.7 KISS (Keep It Simple, Stupid)
- **Definition**: Prefer the simplest design that satisfies the requirements cleanly without unnecessary indirection or cleverness.
- **When to apply**: Always—especially in system boot paths, CLI parsers, and configuration loaders.
- **When NOT to apply**: Never use KISS as an excuse to omit error handling, security checks, or required thread safety.
- **SigmaOS-specific example**: `sigma-bootloader` reads a flat declarative boot entry list rather than embedding a scripting interpreter.
- **Code snippet**:
```rust
pub fn select_default_entry<'a>(entries: &'a [BootEntry], preferred: &str) -> Option<&'a BootEntry> {
    entries.iter().find(|e| e.id == preferred).or_else(|| entries.first())
}
```

### 1.8 YAGNI (You Aren't Gonna Need It)
- **Definition**: Do not implement speculative features, abstractions, or extension points until there is a concrete, current requirement.
- **When to apply**: When tempted to build generic plugin frameworks, unused config flags, or future-proofed wrappers before a second use case exists.
- **When NOT to apply**: For foundational invariants that are costly to retrofit later, such as memory safety, security boundaries, and public wire formats.
- **SigmaOS-specific example**: Build only the CLI flags specified in the current `sigma-sh` spec rather than pre-implementing speculative subcommands.

### 1.9 GRASP (General Responsibility Assignment Software Patterns)
- **Definition**: A set of principles (Information Expert, Creator, Controller, Low Coupling, High Cohesion, Polymorphism, Pure Fabrication, Indirection, Protected Variations) guiding where responsibilities live.
- **When to apply**: During initial module design when deciding which struct owns state transitions, object creation, or external coordination.
- **When NOT to apply**: Do not over-engineer simple procedural scripts with artificial "Controller" or "Fabrication" classes.
- **SigmaOS-specific example**: In `sigma-system`, `SystemProfile` acts as the Information Expert for validating profile dependencies because it already owns the package graph.

### 1.10 Gall's Law
- **Definition**: A complex system that works is invariably found to have evolved from a simple system that worked.
- **When to apply**: When bootstrapping new SigmaOS subsystems (e.g., `sigma-kernel`, `SigmaOS-deskland`, distributed managers).
- **When NOT to apply**: Never use it to justify shipping broken stubs—the simple initial system must actually work end-to-end.
- **SigmaOS-specific example**: Start `SigmaOS-update-system` with atomic single-package verification and rollback before adding distributed fleet orchestration.

### 1.11 Zen of Python
- **Definition**: A collection of guiding aphorisms emphasizing readability, explicitness, simplicity, and flat structure over implicit magic.
- **When to apply**: In all SigmaOS Python tooling (e.g., data science/ML integrations, build helpers) and as general clarity guidance in Rust.
- **When NOT to apply**: When extreme low-level bit manipulation or zero-copy kernel interfaces require dense hardware-specific code (document thoroughly instead).
- **SigmaOS-specific example**: Explicit error propagation and flat `match` arms in `sigma-system` rather than deeply nested callbacks.

### 1.12 Ninety-Ninety Rule
- **Definition**: The first 90 percent of the code accounts for the first 90 percent of the development time; the remaining 10 percent (edge cases, polish, integration) accounts for the other 90 percent.
- **When to apply**: When estimating schedules and reviewing "nearly done" PRs in SigmaOS—always budget for edge cases, error paths, tests, and wiki docs.
- **When NOT to apply**: Not a reason to delay merging small, complete, tested increments.
- **SigmaOS-specific example**: Finishing the happy path of `SigmaOS-bootloader` is only half the work; handling corrupt partitions, fallback entries, and cross-arch tests completes it.

### 1.13 Rule of Three
- **Definition**: Wait until logic is duplicated three times before extracting a shared abstraction, avoiding premature generalization.
- **When to apply**: When deciding whether two similar functions warrant a generic trait or shared crate.
- **When NOT to apply**: Security-critical logic (auth, crypto, secret loading) and identity rules must be centralized immediately on first use.
- **SigmaOS-specific example**: After three SigmaOS CLI tools needed identical `COMPONENT.toml` discovery, that logic was promoted into `sigma-system`.

### 1.14 Boy Scout Rule
- **Definition**: Always leave every file or module you touch slightly cleaner than you found it.
- **When to apply**: When fixing bugs or adding features—clean up dead imports, unclear variable names, or missing doc comments in the touched area.
- **When NOT to apply**: Never mix massive unrelated refactors into a targeted bug-fix PR; keep unrelated cleanups in a separate commit/PR.
- **SigmaOS-specific example**: While fixing a path bug in `sigma-sh`, also replace an `.unwrap()` with proper `?` error propagation in that function.

### 1.15 Deutsch Limit
- **Definition**: Avoid overloading visual or textual interfaces with excessive simultaneous elements (roughly no more than ~50 primitives/controls at once).
- **When to apply**: When designing SigmaOS GUI dashboards (`SigmaOS-ui`, `SigmaOS-deskland`) and CLI help outputs.
- **When NOT to apply**: When rendering dense scientific datasets or logs where pagination/filtering is handled by the viewer.
- **SigmaOS-specific example**: Group `sigma-sh` subcommands into logical namespaces (`pkg`, `sys`, `theme`, `net`) rather than dumping 80 top-level flags.

### 1.16 Zero-One-Infinity
- **Definition**: Allow either zero instances, one instance, or an arbitrary number of instances—never an arbitrary hardcoded limit like 3 or 16.
- **When to apply**: When designing collections, worker pools, config lists, or repository registries.
- **When NOT to apply**: Hardware-imposed limits (e.g., fixed CPU register counts, kernel page table levels, bounded ring buffers for real-time safety).
- **SigmaOS-specific example**: `SigmaOS-wiki-hub` supports arbitrary numbers of component directories discovered dynamically rather than a fixed array of categories.
- **Code snippet**:
```rust
pub struct ComponentRegistry {
    components: Vec<ComponentManifest>, // Arbitrary number, no magic cap
}
```

### 1.17 Worse is Better
- **Definition**: Simplicity of both implementation and interface can be more valuable than completeness or theoretical perfection when shipping real systems.
- **When to apply**: When choosing a clean, debuggable IPC or config format over a complex distributed protocol that delays usability.
- **When NOT to apply**: Never compromise security, memory safety, or data integrity in the name of simplicity.
- **SigmaOS-specific example**: Using plain TOML + Unix domain sockets for local SigmaOS service coordination instead of a heavy broker.

### 1.18 Principle of Least Astonishment
- **Definition**: A component, API, or CLI command should behave the way users and developers naturally expect without hidden side effects.
- **When to apply**: In all CLI flags, exit codes, API return values, and default configurations.
- **When NOT to apply**: When backward-incompatible security hardening intentionally rejects insecure legacy behavior (document clearly).
- **SigmaOS-specific example**: `sigma pkg list` only reads state and never mutates the filesystem or triggers network downloads.

### 1.19 If It Ain't Broke, Don't Fix It
- **Definition**: Do not rewrite or churn stable, tested, working code without a concrete bug, security issue, or new requirement.
- **When to apply**: When tempted to rewrite a working SigmaOS module just to match a passing stylistic preference.
- **When NOT to apply**: When code violates security, memory safety (`unsafe`), or SigmaOS identity rules—those must always be fixed.
- **SigmaOS-specific example**: Leave stable `sigma-system` hash utilities untouched unless a vulnerability or performance bottleneck is proven.

### 1.20 Defensive Programming
- **Definition**: Validate all inputs, preconditions, and external boundaries so the component degrades safely or rejects invalid data cleanly.
- **When to apply**: At all trust boundaries: CLI arguments, config files, IPC messages, network payloads, and kernel syscalls.
- **When NOT to apply**: Inside tight, already-validated inner loops where redundant checks measurably hurt hot-path performance.
- **SigmaOS-specific example**: `SigmaOS-update-system` verifies archive checksums and canonicalizes target paths before extracting any package.
- **Code snippet**:
```rust
pub fn safe_join(base: &std::path::Path, rel: &std::path::Path) -> Result<std::path::PathBuf, PathError> {
    if rel.is_absolute() || rel.components().any(|c| matches!(c, std::path::Component::ParentDir)) {
        return Err(PathError::TraversalRejected);
    }
    Ok(base.join(rel))
}
```

### 1.21 Offensive Programming
- **Definition**: Fail loudly and immediately on internal invariant violations or impossible states rather than masking bugs with silent fallbacks.
- **When to apply**: Inside internal invariants, state machines, and debug/test assertions where continuing would corrupt data.
- **When NOT to apply**: On untrusted user input—use Defensive Programming to return structured `Result::Err` rather than panicking the process.
- **SigmaOS-specific example**: `sigma-kernel` panics/halts immediately on corrupted internal page-table invariants rather than continuing with undefined memory state.
- **Code snippet**:
```rust
pub fn advance_state(state: BootPhase) -> BootPhase {
    match state {
        BootPhase::Init => BootPhase::HardwareReady,
        BootPhase::HardwareReady => BootPhase::KernelLoaded,
        BootPhase::KernelLoaded => unreachable!("KernelLoaded is terminal"),
    }
}
```

### 1.22 Information Hiding
- **Definition**: Conceal internal data representations and implementation details behind stable public interfaces.
- **When to apply**: Across all library crates (`sigma-system`) and inter-repo APIs so internal refactors never break downstream consumers.
- **When NOT to apply**: Plain data-transfer structs (DTOs) whose entire purpose is transparent field access.
- **SigmaOS-specific example**: Keep internal `HashMap` indexing private inside `ThemeRegistry` and expose only lookup methods.
- **Code snippet**:
```rust
pub struct ThemeRegistry {
    entries: std::collections::HashMap<String, ThemeMeta>,
}
impl ThemeRegistry {
    pub fn find(&self, name: &str) -> Option<&ThemeMeta> { self.entries.get(name) }
}
```

### 1.23 Encapsulation
- **Definition**: Bundle data together with the methods that maintain its invariants, restricting direct external mutation.
- **When to apply**: Whenever a struct has invariants across multiple fields (e.g., capacity, state transitions, validated tokens).
- **When NOT to apply**: Simple configuration records with no cross-field invariants.
- **SigmaOS-specific example**: `BoundedQueue` in `sigma-system` keeps its buffer and head/tail indices private so callers cannot desynchronize them.

### 1.24 Abstraction
- **Definition**: Expose essential behavioral concepts while hiding incidental low-level mechanics.
- **When to apply**: When unifying multiple OS targets, storage drivers, or UI backends under a clean SigmaOS interface.
- **When NOT to apply**: When leaky or over-generalized abstractions obscure critical hardware semantics (e.g., DMA alignment or lock ordering).
- **SigmaOS-specific example**: `SigmaOS-zfs-integration` exposes `SnapshotManager` operations (`create`, `rollback`, `list`) without leaking raw ioctl flags to callers.

### 1.25 Composition over Inheritance
- **Definition**: Build complex behavior by combining small, focused components and traits rather than deep class hierarchies.
- **When to apply**: Always in Rust (which enforces trait/struct composition) and in all SigmaOS Python/C++ modules.
- **When NOT to apply**: Only when an external framework explicitly requires subclassing a base class.
- **SigmaOS-specific example**: A `SigmaService` composes a `Logger`, `ConfigStore`, and `HealthCheck` rather than inheriting from a monolithic `BaseDaemon`.
- **Code snippet**:
```rust
pub struct SigmaService<S: ConfigStore, H: HealthCheck> {
    store: S,
    health: H,
}
```

### 1.26 Composition over Configuration
- **Definition**: Prefer assembling small, well-defined code components or declarative profiles rather than building monolithic, flag-heavy configuration engines.
- **When to apply**: When a component accumulates dozens of mutually interacting boolean flags.
- **When NOT to apply**: When end users need runtime declarative tuning (e.g., `SigmaOS` system profiles) without recompiling.
- **SigmaOS-specific example**: Compose `SigmaOS-ui` panels from reusable widget traits instead of a 200-key JSON layout monolith.

### 1.27 Polymorphism
- **Definition**: Allow a single interface to operate uniformly over multiple concrete types (via static generics or dynamic trait objects).
- **When to apply**: Use static dispatch (`impl Trait` / generics) on hot paths and dynamic dispatch (`&dyn Trait`) for runtime plugins.
- **When NOT to apply**: When only one concrete type exists—avoid unnecessary trait indirection.
- **SigmaOS-specific example**: `sigma-system` uses generic `StorageBackend` traits for unit testing with in-memory mocks and production disk backends.
- **Code snippet**:
```rust
pub fn persist<B: StorageBackend>(backend: &B, key: &str, data: &[u8]) -> Result<(), IoError> {
    backend.write(key, data)
}
```

### 1.28 Inheritance (When to Use)
- **Definition**: Deriving a specialized type from a base type; use strictly for true "is-a" behavioral subtyping or trait super-bounds, never merely for code reuse.
- **When to apply**: In Rust, via trait super-bounds (`trait SecureTransport: Transport`) where every implementer genuinely is a specialized form of the base contract.
- **When NOT to apply**: Never use inheritance solely to share helper fields or methods—use composition instead.
- **SigmaOS-specific example**: `trait EncryptedChannel: ByteChannel` requires every `EncryptedChannel` to also satisfy `ByteChannel`.

### 1.29 Uniform Access
- **Definition**: All services or properties offered by a module should be accessed through a consistent notation, whether computed or stored.
- **When to apply**: In public Rust APIs where callers shouldn't care whether a value is cached or computed on demand (expose methods, not public fields).
- **When NOT to apply**: Plain POD/config structs where direct field access is idiomatic and cheaper.
- **SigmaOS-specific example**: `SystemMetrics::cpu_load(&self)` hides whether load is read from `/proc` or a cached sampler.

### 1.30 Open Standard and Interoperability
- **Definition**: Prefer documented, open, vendor-neutral standards and protocols so SigmaOS components interoperate seamlessly across tools and platforms.
- **When to apply**: For file formats, IPC, authentication, graphics, and package metadata (e.g., TOML, JSON, OCI, Wayland, POSIX, SQL).
- **When NOT to apply**: Internal-only, ephemeral in-memory representations where standard serialization overhead is unwarranted.
- **SigmaOS-specific example**: `COMPONENT.toml` uses standard TOML and `SigmaOS` containers support standard OCI images.

---

## 2. Architecture

### 2.1 Separation of Concerns
- **Definition**: Divide a system into distinct sections where each section addresses a separate, non-overlapping concern.
- **When to apply**: Across all SigmaOS layers—separating presentation (GUI/CLI), domain logic, and persistence/hardware access.
- **When NOT to apply**: Never split a cohesive 20-line function into artificial layers that only pass arguments through.
- **SigmaOS-specific example**: `SigmaOS-ui` handles rendering while `sigma-system` handles system state queries.
- **Code snippet**:
```rust
// Domain logic (sigma-system) has zero terminal/UI formatting dependencies
pub fn compute_disk_usage(used: u64, total: u64) -> f64 {
    if total == 0 { 0.0 } else { (used as f64 / total as f64) * 100.0 }
}
```

### 2.2 Layered Design
- **Definition**: Organize the system into hierarchical layers where each layer depends only on the layer directly beneath it.
- **When to apply**: Across the SigmaOS stack: Hardware/Kernel (`sigma-kernel`) -> System Foundation (`sigma-system`) -> Services/Daemons -> CLI & GUI (`sigma-sh`, `SigmaOS-ui`).
- **When NOT to apply**: Never force high-throughput zero-copy data paths through unnecessary pass-through layers; allow controlled bypasses when latency demands it.
- **SigmaOS-specific example**: `sigma-sh` calls `sigma-system` APIs, which in turn invoke `sigma-kernel` syscalls—`SigmaOS-ui` never issues raw kernel ioctls directly.

### 2.3 Modularity
- **Definition**: Decompose the system into discrete, self-contained modules with explicit boundaries and minimal dependencies.
- **When to apply**: Always—both within Rust crates (modules) and across SigmaOS's multi-repo architecture.
- **When NOT to apply**: Avoid over-modularizing tightly coupled state machines where splitting files creates circular dependencies.
- **SigmaOS-specific example**: Each tool (e.g., `SigmaOS-speedtest`, `SigmaOS-notifications`, `SigmaOS-theme-registry`) lives in its own repository with a `COMPONENT.toml`.

### 2.4 Blackbox
- **Definition**: Design components so consumers rely strictly on documented inputs, outputs, and contracts without knowing internal mechanics.
- **When to apply**: At crate boundaries, daemon IPC boundaries, and plugin interfaces.
- **When NOT to apply**: Performance-critical kernel internals where callers must reason about lock ordering or memory layout.
- **SigmaOS-specific example**: `SigmaOS-state-archive` exposes `snapshot()` and `restore()` without exposing its internal compression or chunking format.

### 2.5 Booch Method
- **Definition**: An object-oriented analysis and design methodology emphasizing clear class/module abstractions, explicit boundaries, and iterative macro/micro architecture.
- **When to apply**: When modeling complex stateful SigmaOS subsystems (desktop compositors, virtual machine managers, distributed schedulers).
- **When NOT to apply**: Simple stateless CLI filters or single-purpose scripts.
- **SigmaOS-specific example**: Modeling `SigmaOS-deskland` windows, workspaces, and outputs as distinct collaborating abstractions with explicit lifecycle states.

### 2.6 Command-Query Separation (CQS)
- **Definition**: Every method should either be a command that mutates state (returning `()` or status) or a query that returns data without observable side effects.
- **When to apply**: In all Rust APIs, state managers, and CLI subcommands.
- **When NOT to apply**: Atomic operations like `stack.pop()`, `AtomicUsize::fetch_add()`, or `map.insert()` where combining mutation and return is required for atomicity or ergonomics.
- **SigmaOS-specific example**: `Registry::get_theme(&self, id)` is a pure `&self` query; `Registry::register_theme(&mut self, theme)` is a `&mut self` command.
- **Code snippet**:
```rust
impl Registry {
    pub fn get_theme(&self, id: &str) -> Option<&Theme> { self.map.get(id) }
    pub fn register_theme(&mut self, theme: Theme) { self.map.insert(theme.id.clone(), theme); }
}
```

### 2.7 CQRS (Command Query Responsibility Segregation)
- **Definition**: Separate the write/mutation model (commands) from the read/projection model (queries) at the architectural level.
- **When to apply**: In distributed SigmaOS telemetry, audit logs, and package indexers where read patterns differ drastically from write patterns.
- **When NOT to apply**: Standard CRUD tools and local config managers where a single model is simpler and sufficient.
- **SigmaOS-specific example**: `SigmaOS-update-system` writes signed transaction logs to an append-only journal while serving fast pre-indexed read views to `sigma pkg search`.

### 2.8 Inversion of Control (IoC)
- **Definition**: Transfer control of execution flow or dependency wiring from custom application code to a framework, runtime, or caller-supplied callbacks.
- **When to apply**: In async event loops (`tokio`), plugin hosts, and dependency injection for testable SigmaOS services.
- **When NOT to apply**: Linear startup scripts (`sigma-bootloader`) where explicit step-by-step control flow is clearer and easier to audit.
- **SigmaOS-specific example**: `SigmaOS-ui` registers event handlers with the compositor event loop rather than polling hardware input manually.

### 2.9 Interface Segregation
- **Definition**: Prefer many small, role-specific interfaces/traits over one monolithic interface.
- **When to apply**: Whenever traits are shared across multiple SigmaOS crates or drivers.
- **When NOT to apply**: When a single trait has only a few inseparable methods.
- **SigmaOS-specific example**: Separate `HealthCheckable` from `Configurable` so read-only daemons don't implement dummy configuration setters.

### 2.10 Loose Coupling
- **Definition**: Minimize direct knowledge and compile-time/runtime assumptions between modules so one can change without breaking others.
- **When to apply**: Between independent SigmaOS repositories and services.
- **When NOT to apply**: Within a single cohesive algorithm or data structure where tight collaboration is natural.
- **SigmaOS-specific example**: SigmaOS services communicate over versioned IPC schemas or `COMPONENT.toml` contracts rather than sharing internal struct layouts.

### 2.11 Cohesion Maximize
- **Definition**: Keep closely related data and functions together inside the same module or struct so each unit has a clear, unified purpose.
- **When to apply**: Always when organizing modules in `sigma-system` and component crates.
- **When NOT to apply**: Never dump unrelated utilities into a `utils.rs` or `misc.rs` grab-bag.
- **SigmaOS-specific example**: Group all cryptographic signature verification helpers into `sigma_system::security::verify` rather than scattering them across callers.

### 2.12 Coupling Minimization
- **Definition**: Reduce the number and strength of dependencies between modules, crates, and repositories.
- **When to apply**: When reviewing `Cargo.toml` dependencies and inter-repo calls.
- **When NOT to apply**: Do not duplicate core `sigma-system` primitives just to avoid a single well-defined dependency on the shared foundation crate.
- **SigmaOS-specific example**: `SigmaOS-speedtest` depends only on `sigma-system` core networking, not on GUI or theme crates.

### 2.13 Plug-In Driver Model
- **Definition**: Define a stable core host interface that discovers and loads specialized driver implementations externally.
- **When to apply**: For filesystems, audio/video backends, theme engines, and device drivers.
- **When NOT to apply**: Core kernel boot primitives that must be statically linked for reliability.
- **SigmaOS-specific example**: `SigmaOS-deskland` supports pluggable output/renderer drivers behind a unified `DisplayDriver` trait.

### 2.14 Plug & Play Driver Model
- **Definition**: Automatically detect, bind, and configure hardware or virtual devices at runtime without manual user intervention.
- **When to apply**: In SigmaOS device managers for USB, displays, audio, and network interfaces.
- **When NOT to apply**: Security-sensitive enterprise environments where explicit device allowlisting is mandated.
- **SigmaOS-specific example**: `sigma-kernel` emits hotplug events that `sigma-system` binds automatically to the matching device driver.

### 2.15 Dynamically Loadable Modules
- **Definition**: Support loading and unloading compiled modules or extensions at runtime without restarting the core system.
- **When to apply**: For optional kernel drivers, codec packs, and desktop applets.
- **When NOT to apply**: Security-critical TCB (Trusted Computing Base) components that should remain statically verified.
- **SigmaOS-specific example**: `sigma-kernel` loads hardware-specific driver modules on demand via signed module manifests.

### 2.16 Separation of Mechanism & Policy
- **Definition**: Separate *how* a capability works (mechanism) from *when/who/what* rules govern its use (policy).
- **When to apply**: In schedulers, security enforcement, package managers, and window managers.
- **When NOT to apply**: Tiny single-purpose tools where policy and mechanism are fixed and inseparable.
- **SigmaOS-specific example**: `sigma-kernel` provides process isolation mechanisms (namespaces/cgroups), while `SigmaOS-system-profile` defines the policy rules.

### 2.17 Normalization
- **Definition**: Structure schemas, configurations, and identifiers into a canonical, non-redundant form.
- **When to apply**: In package databases, `COMPONENT.toml` manifests, configuration files, and SigmaOS naming conventions.
- **When NOT to apply**: Denormalized read caches where measured query latency requires pre-joined views.
- **SigmaOS-specific example**: Normalize all component paths, package IDs, and metadata keys to lowercase `SigmaOS-*` / `sigma-*` canonical forms.

### 2.18 Component Isolation
- **Definition**: Run and package components so failures, crashes, or compromises in one component cannot cascade into others.
- **When to apply**: Across daemons, browser tabs, virtual environments, and third-party app environments (`SigmaOS-wine`, `SigmaOS-virtualbox`).
- **When NOT to apply**: Tightly coupled library calls inside the same trusted process where IPC overhead is prohibitive.
- **SigmaOS-specific example**: Run `SigmaOS-theme-marketplace` downloads in an isolated sandboxed worker before applying themes to the compositor.

---

## 3. OS / Systems

### 3.1 Memory Safety
- **Definition**: Guarantee that all memory accesses are valid, bounded, and free of use-after-free, double-free, and buffer overflows.
- **When to apply**: Always—every standard SigmaOS Rust crate must enforce `#![forbid(unsafe_code)]`.
- **When NOT to apply**: Never compromise memory safety; where hardware/FFI forces `unsafe`, isolate it into tiny audited modules with safety comments.
- **SigmaOS-specific example**: `sigma-system` enforces `#![forbid(unsafe_code)]` at crate root.
- **Code snippet**:
```rust
#![forbid(unsafe_code)]

pub fn safe_slice(buf: &[u8], len: usize) -> Option<&[u8]> {
    buf.get(..len)
}
```

### 3.2 Manual Memory Control
- **Definition**: Explicitly manage allocation lifetimes, arenas, or slab pools when deterministic latency or zero-GC behavior is required.
- **When to apply**: In `sigma-kernel`, device drivers, real-time audio (`SigmaOS-sound`), and high-throughput packet buffers.
- **When NOT to apply**: Standard CLI tools and high-level services where Rust ownership and standard `Vec`/`Box` suffice.
- **SigmaOS-specific example**: `sigma-kernel` uses fixed-size slab allocators for interrupt-safe descriptor allocation.

### 3.3 Memory Barriers
- **Definition**: Hardware or compiler fences that enforce strict ordering of memory reads and writes across CPU cores and DMA devices.
- **When to apply**: When implementing lock-free ring buffers, atomic state machines, or MMIO device registers.
- **When NOT to apply**: Standard mutex-protected code where locks already provide acquire/release memory ordering.
- **SigmaOS-specific example**: `sigma-kernel` uses `Ordering::Release` / `Ordering::Acquire` when publishing DMA descriptor ring indices.
- **Code snippet**:
```rust
use std::sync::atomic::{AtomicUsize, Ordering};

pub fn publish_tail(tail: &AtomicUsize, next: usize) {
    tail.store(next, Ordering::Release);
}
```

### 3.4 Memory Discipline
- **Definition**: Enforce strict ownership, bounded allocations, zero leaks, and explicit limits on every memory-consuming path.
- **When to apply**: In long-running SigmaOS daemons, kernel subsystems, and embedded/resource-constrained targets.
- **When NOT to apply**: Short-lived one-shot CLI invocations where the OS reclaims process memory on exit (still avoid unbounded leaks).
- **SigmaOS-specific example**: `SigmaOS-notifications` caps its in-memory history ring buffer to a bounded capacity so memory never grows unbounded.

### 3.5 Virtual Memory Abstraction
- **Definition**: Map process-isolated virtual address spaces to physical frames via page tables, providing protection, paging, and shared memory.
- **When to apply**: In `sigma-kernel` process management, memory-mapped I/O, and copy-on-write IPC.
- **When NOT to apply**: Early pre-MMU bootloader stages (`sigma-bootloader`) operating on physical addresses.
- **SigmaOS-specific example**: `sigma-kernel` maps each user-space SigmaOS service into an isolated virtual address space with W^X (Write XOR Execute) page permissions.

### 3.6 Zero-Copy
- **Definition**: Transfer data between buffers, sockets, or processes without redundant CPU memory copies.
- **When to apply**: In `SigmaOS-ui` compositor framebuffers, `sigma-sh` stream pipelines, and `SigmaOS-zfs-integration` I/O paths.
- **When NOT to apply**: Small control messages (< 4 KiB) where copying is faster than page-remapping or lifetime synchronization.
- **SigmaOS-specific example**: Pass `&[u8]` slices or shared DMA-BUF handles between `SigmaOS-deskland` and clients instead of copying pixel buffers.

### 3.7 Translation Lookaside Buffer (TLB) Consistency
- **Definition**: Keep per-CPU TLB caches synchronized with page-table modifications via targeted invalidations and shootdowns.
- **When to apply**: Whenever `sigma-kernel` unmaps pages, changes page permissions, or migrates address spaces across cores.
- **When NOT to apply**: User-space applications that do not manage page tables directly.
- **SigmaOS-specific example**: `sigma-kernel` issues `invlpg` / ASID-tagged TLB shootdowns whenever a shared IPC page is unmapped.

### 3.8 Locality of Reference
- **Definition**: Organize data and execution paths so temporally and spatially adjacent accesses hit CPU caches rather than main memory.
- **When to apply**: In hot loops, ECS/scene graphs (`SigmaOS-deskland`), and kernel scheduling queues.
- **When NOT to apply**: Cold configuration parsing or one-time startup paths.
- **SigmaOS-specific example**: Store active task descriptors in contiguous `Vec<TaskEntry>` arrays rather than pointer-chasing linked lists.

### 3.9 Cache Conscious Design
- **Definition**: Align hot data structures to cache lines (typically 64 bytes) and avoid false sharing between CPU cores.
- **When to apply**: In multi-core counters, lock-free queues, and kernel per-CPU structures.
- **When NOT to apply**: Single-threaded or cold-path structs where padding wastes memory without contention benefit.
- **SigmaOS-specific example**: Pad per-core scheduler statistics in `sigma-kernel` to 64-byte cache-line boundaries to prevent false sharing.
- **Code snippet**:
```rust
#[repr(align(64))]
pub struct CacheAlignedCounter {
    pub count: std::sync::atomic::AtomicU64,
}
```

### 3.10 Mechanical Sympathy
- **Definition**: Design software data structures and algorithms to harmonize with how underlying CPU caches, branch predictors, and NVMe/NIC hardware actually work.
- **When to apply**: In systems libraries, databases, filesystems, and kernel schedulers.
- **When NOT to apply**: High-level glue scripts where developer clarity far outweighs microsecond hardware tuning.
- **SigmaOS-specific example**: Batch filesystem metadata writes in `SigmaOS-zfs-integration` to match underlying NVMe block sizes.

### 3.11 Low Level Control
- **Definition**: Retain direct, predictable control over memory layout, syscalls, I/O, and CPU scheduling without hidden runtime pauses.
- **When to apply**: In `sigma-kernel`, `sigma-bootloader`, and system daemons.
- **When NOT to apply**: High-level data science notebooks or UI scripting layers where managed runtimes are appropriate.
- **SigmaOS-specific example**: `sigma-bootloader` controls UEFI/BIOS handoff and memory maps directly without garbage collection.

### 3.12 Low Level Languages
- **Definition**: Use systems languages (primarily Rust, with C/assembly only where hardware mandates) for OS, kernel, and core infrastructure.
- **When to apply**: All core SigmaOS infrastructure, daemons, CLI tools, and performance-critical libraries.
- **When NOT to apply**: Exploratory data analysis or ML orchestration where Python/Julia ecosystems are explicitly targeted.
- **SigmaOS-specific example**: `sigma-system`, `sigma-sh`, and `sigma-kernel` are implemented in Rust.

### 3.13 Process Isolation
- **Definition**: Confine each process to its own address space, file descriptors, and capability set so faults or exploits cannot cross boundaries.
- **When to apply**: Across all SigmaOS system daemons, user applications, and sandboxed environments.
- **When NOT to apply**: Cooperative internal threads within a single trusted service.
- **SigmaOS-specific example**: `SigmaOS-wine` and `SigmaOS-browser` profiles run with strict namespace and capability isolation.

### 3.14 Race-Free Design
- **Definition**: Eliminate data races at compile time or through strict synchronization invariants so concurrent accesses are always well-defined.
- **When to apply**: Always in multi-threaded and async SigmaOS code.
- **When NOT to apply**: Never—data races are undefined behavior and strictly forbidden.
- **SigmaOS-specific example**: Rely on Rust's `Send` and `Sync` traits plus `Mutex`/`RwLock` or message passing instead of shared mutable globals.

### 3.15 Safe Concurrency
- **Definition**: Coordinate concurrent tasks using Rust's ownership model, channels, and scoped threads rather than error-prone raw locks.
- **When to apply**: Whenever parallelizing I/O, repo audits, or background daemon tasks.
- **When NOT to apply**: Sequential tasks where spawning threads adds synchronization overhead without speedup.
- **SigmaOS-specific example**: `SigmaOS-xtask` uses bounded `tokio::sync::mpsc` channels to collect audit results from worker tasks.
- **Code snippet**:
```rust
pub async fn collect_results(mut rx: tokio::sync::mpsc::Receiver<String>) -> Vec<String> {
    let mut out = Vec::new();
    while let Some(item) = rx.recv().await { out.push(item); }
    out
}
```

### 3.16 Deadlock Avoidance
- **Definition**: Prevent circular lock dependencies using strict lock ordering, lock-free structures, or message-passing actors.
- **When to apply**: Any module acquiring multiple locks or awaiting resources across tasks.
- **When NOT to apply**: Single-lock critical sections that never call out to external callbacks while holding the lock.
- **SigmaOS-specific example**: Document and enforce a strict global lock hierarchy in `sigma-system`, and never hold a `MutexGuard` across an `.await` point.

### 3.17 Priority Inversion Avoidance
- **Definition**: Prevent low-priority tasks from blocking high-priority tasks on shared locks via priority inheritance or lock-free designs.
- **When to apply**: In `sigma-kernel` schedulers, real-time audio (`SigmaOS-sound`), and compositor input threads (`SigmaOS-deskland`).
- **When NOT to apply**: Uniform-priority batch worker pools.
- **SigmaOS-specific example**: Input-handling threads in `SigmaOS-deskland` communicate with background workers via lock-free ring buffers rather than shared mutexes.

### 3.18 Atomic Operations
- **Definition**: Use CPU-guaranteed indivisible read-modify-write primitives (`AtomicBool`, `AtomicU64`) for lock-free flags and counters.
- **When to apply**: For shutdown flags, reference counts, metrics counters, and single-word state transitions.
- **When NOT to apply**: Multi-field invariants that must update together—use a `Mutex` instead of fragile multi-atomic schemes.
- **SigmaOS-specific example**: Graceful daemon shutdown uses an `Arc<AtomicBool>` signal flag.
- **Code snippet**:
```rust
use std::sync::atomic::{AtomicBool, Ordering};

pub fn should_stop(flag: &AtomicBool) -> bool {
    flag.load(Ordering::Acquire)
}
```

### 3.19 Interrupt Handling Discipline
- **Definition**: Keep hardware interrupt handlers (top-halves) minimal, non-blocking, and allocation-free, deferring heavy work to bottom-halves/workers.
- **When to apply**: In `sigma-kernel` IRQ handlers and signal handlers.
- **When NOT to apply**: Normal user-space async tasks.
- **SigmaOS-specific example**: `sigma-kernel` IRQ handler acknowledges the APIC, enqueues the event into a pre-allocated ring, and wakes the driver thread.

### 3.20 Efficient Scheduling
- **Definition**: Allocate CPU time fairly and predictably with low context-switch overhead, prioritizing interactive responsiveness alongside throughput.
- **When to apply**: In `sigma-kernel` task scheduler and async task executors.
- **When NOT to apply**: Single-threaded synchronous CLI utilities.
- **SigmaOS-specific example**: `sigma-kernel` prioritizes interactive `SigmaOS-deskland` compositor frames over background indexing jobs.

### 3.21 Direct Device Control
- **Definition**: Interface cleanly with hardware registers, DMA, or kernel device nodes without unnecessary intermediate abstraction layers.
- **When to apply**: In `sigma-kernel` drivers and hardware utilities.
- **When NOT to apply**: Portable user-space applications that should use standard `sigma-system` abstractions.
- **SigmaOS-specific example**: `SigmaOS-sigma-kernel` GPU/display driver programs KMS/DRM buffers directly for low-latency frame presentation.

### 3.22 Asynchronous I/O & Event Loops
- **Definition**: Multiplex non-blocking I/O readiness events on an event loop (`tokio` / `epoll` / `io_uring`) so threads never block idly waiting on I/O.
- **When to apply**: In network services, IPC daemons, and multi-repo orchestration tools.
- **When NOT to apply**: CPU-bound number crunching (use thread pools like `rayon` instead of async tasks).
- **SigmaOS-specific example**: `SigmaOS-theme-sync` uses `tokio` async I/O to concurrently fetch and verify theme metadata.

### 3.23 Concurrency
- **Definition**: Structure computations into independent tasks that can make progress simultaneously without corrupting shared state.
- **When to apply**: When overlapping I/O, servicing multiple clients, or utilizing multi-core CPUs.
- **When NOT to apply**: Trivial sequential scripts where concurrency adds complexity and debugging cost without measurable benefit.
- **SigmaOS-specific example**: `SigmaOS-wiki-hub` validates repository manifests concurrently across worker tasks.

---

## 4. Testing

### 4.1 FIRST (Fast-Isolated-Repeatable-Self-validating-Timely)
- **Definition**: Every test must be Fast, Isolated from external state, Repeatable across runs, Self-validating (pass/fail without manual inspection), and Timely (written with the code).
- **When to apply**: All unit and integration tests across every SigmaOS repository.
- **When NOT to apply**: Dedicated end-to-end hardware/QEMU boot tests (which are slower and run in dedicated CI stages, still kept isolated and self-validating).
- **SigmaOS-specific example**: `sigma-system` unit tests use `tempfile::tempdir()` so tests never collide on shared filesystem paths.

### 4.2 Arrange-Act-Assert (AAA)
- **Definition**: Structure every test cleanly into three distinct phases: Arrange preconditions, Act on the unit under test, and Assert the expected outcome.
- **When to apply**: Every unit and integration test in SigmaOS.
- **When NOT to apply**: Property-based fuzz tests where input generation and invariant checking are driven by a framework loop.
- **SigmaOS-specific example**: All `sigma-sh` command parser tests explicitly separate input construction, parser invocation, and assertion.
- **Code snippet**:
```rust
#[test]
fn rejects_empty_component_name() {
    // Arrange
    let input = "";
    // Act
    let res = validate_component_name(input);
    // Assert
    assert!(res.is_err());
}
```

### 4.3 Deterministic Testing
- **Definition**: Tests must produce identical results on every execution regardless of CPU speed, clock time, OS scheduling, or network conditions.
- **When to apply**: Always—no `thread::sleep` synchronization, unseeded RNGs, or live internet fetches in unit tests.
- **When NOT to apply**: Never—even chaos/stress tests should log and accept a deterministic PRNG seed.
- **SigmaOS-specific example**: Inject a `Clock` trait or fixed timestamp in `SigmaOS-state-archive` tests instead of calling `SystemTime::now()`.

### 4.4 Test Failure on Purpose
- **Definition**: Explicitly write negative tests that verify error paths, invalid inputs, permission denials, and boundary failures behave as specified.
- **When to apply**: For every parser, validator, auth check, and state transition.
- **When NOT to apply**: Never skip negative tests; failure paths are where security bugs hide.
- **SigmaOS-specific example**: `SigmaOS-update-system` tests intentionally feed tampered SHA-256 checksums to prove installation aborts cleanly.

### 4.5 Fail-Fast System
- **Definition**: Detect invalid state, missing configuration, or invariant violations as early as possible and abort the operation immediately with a clear diagnostic.
- **When to apply**: Startup config loading, CLI argument validation, CI pipelines, and security checks.
- **When NOT to apply**: Fault-tolerant background sync loops where transient network retries with backoff are expected.
- **SigmaOS-specific example**: `sigma-system` aborts immediately on startup if required environment secrets or `COMPONENT.toml` fields are missing.

### 4.6 CI/CD
- **Definition**: Automatically run formatting, linting, builds, tests, and security checks on every push and pull request before merging to `main`.
- **When to apply**: Every SigmaOS repository via `.github/workflows/`.
- **When NOT to apply**: Never bypass CI checks to force-push unverified code into `main`.
- **SigmaOS-specific example**: Every repo's CI workflow runs `cargo fmt --check`, `cargo clippy -- -D warnings`, and `cargo test`.

### 4.7 Reproducible Builds
- **Definition**: Compiling the same source commit with the same toolchain and locked dependencies must produce bit-for-bit identical build artifacts.
- **When to apply**: All SigmaOS releases, kernel images, bootloaders, and system packages.
- **When NOT to apply**: Local incremental debug builds where fast iteration is prioritized over determinism.
- **SigmaOS-specific example**: Commit `Cargo.lock` in every binary/application repo, pin toolchains, and strip non-deterministic timestamps.

### 4.8 Power of Ten
- **Definition**: Ten safety-critical coding rules (simple control flow, no unbounded loops, no post-init dynamic allocation in critical paths, small functions, high assertion density, minimal scope, check all return values, limited preprocessor/macro magic, restricted pointer indirection, zero-warning compilation).
- **When to apply**: In `sigma-kernel`, `sigma-bootloader`, and safety-critical system daemons (`cargo clippy -- -D warnings`).
- **When NOT to apply**: High-level user-space apps where standard heap allocation (`Vec`, `String`) is safe and idiomatic.
- **SigmaOS-specific example**: `sigma-bootloader` bounds all partition-table loops to a fixed maximum iteration count and compiles with zero warnings.

---

## 5. Development Practices

### 5.1 Spec-Driven Development
- **Definition**: Define the requirements, interfaces, edge cases, and acceptance criteria in a clear specification before writing implementation code.
- **When to apply**: Before building any new SigmaOS component, protocol, or cross-repo feature.
- **When NOT to apply**: Quick one-line bug fixes where the issue report itself is already a complete spec.
- **SigmaOS-specific example**: Author `COMPONENT.toml` and the component's wiki spec before implementing `SigmaOS-survey` or `SigmaOS-video`.

### 5.2 Refactoring
- **Definition**: Improve the internal structure, readability, and modularity of existing code without changing its observable external behavior.
- **When to apply**: When code becomes hard to test, duplicates logic (Rule of Three), or accumulates technical debt—always backed by passing tests.
- **When NOT to apply**: Never refactor without test coverage, and never mix large refactors with unrelated feature changes.
- **SigmaOS-specific example**: Extracting shared manifest parsing from three CLI crates into `sigma-system` while keeping all CLI outputs identical.

### 5.3 Optimize for Deletion
- **Definition**: Structure code into self-contained, loosely coupled modules so obsolete features or backends can be deleted cleanly without untangling the whole codebase.
- **When to apply**: When adding experimental backends, feature adapters, or temporary migration shims.
- **When NOT to apply**: Core foundational primitives that every module depends on.
- **SigmaOS-specific example**: Keep each `SigmaOS-theme-registry` exporter in its own file so deprecated themes/targets can be removed with a single `git rm`.

### 5.4 Optimize for Performance
- **Definition**: Profile and optimize bottlenecks using real benchmarks (`criterion`, `perf`) rather than guesswork.
- **When to apply**: When a measured latency, memory, or throughput target is missed (e.g., boot time, compositor frame time, package resolution).
- **When NOT to apply**: Premature micro-optimization of cold paths that sacrifices clarity for negligible gain.
- **SigmaOS-specific example**: Benchmarking `sigma-sh` startup latency to keep shell prompt initialization under 10 ms.

### 5.5 Avoid Fragmentation
- **Definition**: Prevent unnecessary forks, divergent copies, or incompatible variants of tools, configs, or APIs within the SigmaOS ecosystem.
- **When to apply**: Whenever tempted to copy-paste a crate or invent a custom config format instead of reusing `sigma-system`.
- **When NOT to apply**: Intentional multi-repo separation of distinct domain components.
- **SigmaOS-specific example**: All SigmaOS tools share one `COMPONENT.toml` format and one `sigma-system` core library.

### 5.6 Pristine Sources
- **Definition**: Keep repository working trees and source commits clean—free of build artifacts, temporary files, generated binaries, or ad-hoc patches.
- **When to apply**: Always in every SigmaOS repository (`.gitignore` `target/`, `*.log`, local env files).
- **When NOT to apply**: Committed `Cargo.lock` for binaries (which is required for reproducibility, not a build artifact).
- **SigmaOS-specific example**: Never commit `target/` or untracked `.tmp` files into `Sigma` or component repos.

### 5.7 Upstream First Policy
- **Definition**: Contribute fixes and improvements to the canonical shared library or core repository first rather than maintaining private downstream patches.
- **When to apply**: Whenever a bug is found in `sigma-system` or a shared SigmaOS component while building a downstream tool.
- **When NOT to apply**: Emergency local hotfixes that are immediately followed by an upstream PR.
- **SigmaOS-specific example**: Fix a `COMPONENT.toml` parsing edge case in `sigma-system` directly instead of patching around it in `SigmaOS-xtask`.

### 5.8 Practical Licensing Awareness
- **Definition**: Understand and respect open-source license compatibility—SigmaOS is **GPL-3.0-or-later**, so all dependencies and contributions must be GPL-3.0-compatible.
- **When to apply**: Before adding any new crate to `Cargo.toml` or importing external assets.
- **When NOT to apply**: Never ignore license incompatibility; reject proprietary or GPL-incompatible dependencies.
- **SigmaOS-specific example**: Verify every crate in `Cargo.toml` uses MIT, Apache-2.0, BSD, or GPL-3.0-compatible licenses.

### 5.9 Semantic Versioning
- **Definition**: Use `MAJOR.MINOR.PATCH` versioning for internal library crates (`sigma-system`) to communicate breaking changes, new features, and bug fixes clearly.
- **When to apply**: In `Cargo.toml` crate metadata for shared libraries.
- **When NOT to apply**: Do **not** create Git release tags for SigmaOS OS/component rolling releases (see Rolling Release Model).
- **SigmaOS-specific example**: `sigma-system` bumps `MINOR` in `Cargo.toml` when adding new public traits without breaking existing callers.

### 5.10 Version Control Practices
- **Definition**: Maintain clean, atomic, descriptive commits on short-lived `feature/<name>` branches with Conventional Commit messages.
- **When to apply**: Every commit in every SigmaOS repository.
- **When NOT to apply**: Never force-push `main` or bundle unrelated changes into one giant commit.
- **SigmaOS-specific example**: Commit `feat(bootloader): add fallback kernel entry selection` with tests and wiki update together.

### 5.11 Stable APIs
- **Definition**: Keep public library traits, CLI flags, and IPC schemas backward-compatible once published, deprecating gracefully before removal.
- **When to apply**: Public interfaces in `sigma-system`, `sigma-sh`, and `COMPONENT.toml`.
- **When NOT to apply**: Private `pub(crate)` internals, which can be refactored freely.
- **SigmaOS-specific example**: Mark old `sigma-system` config keys `#[deprecated]` for a migration cycle rather than breaking all 100+ repos overnight.

### 5.12 Rolling Release Model
- **Definition**: Continuously integrate and ship tested changes on `main` without freezing versioned release branches or creating release tags.
- **When to apply**: Across all SigmaOS repositories.
- **When NOT to apply**: Never create `vX.Y.Z` Git tags or long-lived release branches.
- **SigmaOS-specific example**: `main` in `Sigma` and `SigmaOS-update-system` is always green and deployable.

### 5.13 No Demo & No Stub
- **Definition**: Never commit placeholder implementations, `unimplemented!()`, mock-only demos, or half-finished stubs to `main`.
- **When to apply**: Every PR and commit across SigmaOS.
- **When NOT to apply**: Pure trait definitions or test doubles inside `#[cfg(test)]` modules.
- **SigmaOS-specific example**: Every subcommand in `sigma-sh` must execute real logic and have real tests before merging.

### 5.14 Talk Is Cheap, Show Me The Code
- **Definition**: Ground technical debates and proposals in working prototypes, benchmarks, or concrete patches rather than endless abstract discussion.
- **When to apply**: When resolving architectural disagreements or proposing new SigmaOS subsystems.
- **When NOT to apply**: Security/architecture reviews where a brief written threat model prevents wasted implementation effort.
- **SigmaOS-specific example**: Submit a working benchmarked PR for a faster `sigma-kernel` allocator rather than debating theory in issues.

### 5.15 Create Components Which Are Necessary
- **Definition**: Every repository, crate, or service in SigmaOS must serve a concrete, documented purpose in the ecosystem.
- **When to apply**: Before creating a new repository or microservice.
- **When NOT to apply**: Never create empty placeholder repos with no real functionality.
- **SigmaOS-specific example**: Create `SigmaOS-airbyte` or `SigmaOS-duckdb` only with real integration config, `COMPONENT.toml`, tests, and wiki docs.

### 5.16 If It Is Not Required, Then Don't Do It
- **Definition**: Aggressively eliminate unnecessary complexity, unused dependencies, and over-engineered features.
- **When to apply**: During spec review, dependency selection, and PR review.
- **When NOT to apply**: Never strip required security, error handling, tests, or documentation.
- **SigmaOS-specific example**: Omit heavy web frameworks when a lightweight Rust CLI + local socket satisfies the requirement.

### 5.17 Fix & Solve Edge Cases
- **Definition**: Proactively handle boundary conditions (empty inputs, zero capacity, Unicode paths, network timeouts, disk full, permission denied).
- **When to apply**: Every parser, filesystem operation, allocator, and network handler.
- **When NOT to apply**: Never defer known crash-inducing edge cases as "rare".
- **SigmaOS-specific example**: `sigma-system` handles zero-byte files, symlinks, and non-UTF-8 OS paths without panicking.

### 5.18 Uphold Intellectual Property
- **Definition**: Respect copyrights, patents, and open-source licenses; never copy proprietary code or strip license headers from permitted third-party code.
- **When to apply**: Whenever incorporating algorithms, assets, or dependencies.
- **When NOT to apply**: Never—IP compliance is mandatory.
- **SigmaOS-specific example**: All SigmaOS repositories carry `GPL-3.0-or-later` `LICENSE` files and original SigmaOS-authored implementations.

### 5.19 Meritocracy and Inclusivity
- **Definition**: Evaluate contributions strictly on technical quality and adherence to SigmaOS principles while welcoming contributors of all backgrounds.
- **When to apply**: Code reviews, maintainer promotions, and community discussions.
- **When NOT to apply**: Never lower technical or security standards, and never exclude contributors based on identity.
- **SigmaOS-specific example**: Any contributor whose PRs consistently pass CI, tests, and reviews can become a component maintainer.

### 5.20 Governance and Do-cracy
- **Definition**: Those who do the work make the decisions, within the shared guardrails of SigmaOS architecture and `GOVERNANCE.md`.
- **When to apply**: Day-to-day maintenance, prioritization, and component ownership.
- **When NOT to apply**: Cross-repo breaking changes or identity/security policies, which require core consensus.
- **SigmaOS-specific example**: The active maintainer of `SigmaOS-theme-registry` decides its internal module layout as long as it honors `COMPONENT.toml` and CI.

### 5.21 Community-Oriented Development
- **Definition**: Develop openly in public repositories with clear issues, accessible documentation, and responsive code reviews.
- **When to apply**: All SigmaOS planning, issue triage, and wiki updates.
- **When NOT to apply**: Private security vulnerability disclosures (handled confidentially until patched).
- **SigmaOS-specific example**: Keep roadmaps, parity matrices, and component guides up to date in `SigmaOS-wiki-hub`.

### 5.22 Respect & Ethical Participation
- **Definition**: Engage constructively, critique code rather than individuals, and never introduce malicious, deceptive, or harmful behavior.
- **When to apply**: All human and AI agent interactions, commit messages, and code reviews.
- **When NOT to apply**: Never tolerate harassment, backdoors, or fabricated test results.
- **SigmaOS-specific example**: Review comments focus on concrete improvements (e.g., "use `checked_add` here to prevent overflow").

### 5.23 Free and Open Source Software
- **Definition**: Ensure SigmaOS remains 100% free and open source under `GPL-3.0-or-later`, empowering users to inspect, modify, and redistribute the entire OS.
- **When to apply**: Every component, tool, build script, and configuration system in SigmaOS.
- **When NOT to apply**: Never introduce proprietary blobs or closed-source runtime dependencies into core SigmaOS.
- **SigmaOS-specific example**: All SigmaOS system tools and libraries ship full buildable source under `GPL-3.0-or-later`.

---

## 6. SigmaOS-Specific

### 6.1 Goal-Based OS
- **Definition**: Design SigmaOS around user outcomes and workflow goals (e.g., Data Science, Craft, Development, Office, Gaming) rather than forcing users to assemble raw packages manually.
- **When to apply**: When organizing `SigmaOS-system-profile` bundles, desktop presets, and onboarding flows.
- **When NOT to apply**: Never restrict power users from customizing or overriding individual packages when needed.
- **SigmaOS-specific example**: Selecting the "Data Science" goal profile automatically provisions `SigmaOS-python`, `SigmaOS-duckdb`, `SigmaOS-polars`, and `SigmaOS-jupyter` in one declarative step.

### 6.2 Multi-Repo Modularity
- **Definition**: Keep each SigmaOS domain or tool in its own dedicated, focused repository connected via `COMPONENT.toml` and `tools-sigmaos.sh`.
- **When to apply**: When creating or maintaining distinct SigmaOS components (e.g., `SigmaOS-deskland`, `SigmaOS-bootloader`, `SigmaOS-theme-registry`).
- **When NOT to apply**: Tightly coupled sub-crates that belong in one Cargo workspace (like `Sigma` + `Sigma/cli`).
- **SigmaOS-specific example**: Each of the 117+ SigmaOS repositories owns one clear capability and declares its metadata in `COMPONENT.toml`.

### 6.3 Single Branch Per Single Repository
- **Definition**: Every SigmaOS repository maintains `main` as its sole permanent branch; no parallel `develop`, `staging`, or `release/*` branches.
- **When to apply**: All SigmaOS repositories at all times.
- **When NOT to apply**: Never—temporary `feature/<name>` branches are deleted immediately after merging into `main`.
- **SigmaOS-specific example**: `Sigma`, `SigmaOS-wiki-hub`, and all component repos keep only `main` permanently.

### 6.4 Make a Branch Only in Case of New Feature
- **Definition**: Create a short-lived `feature/<name>` branch strictly when implementing a new feature or fix, and never commit directly to `main`.
- **When to apply**: Every code or documentation change.
- **When NOT to apply**: Automated CI mirror syncs explicitly authorized to fast-forward `main`.
- **SigmaOS-specific example**: `git checkout -b feature/add-tlb-shootdown-tests` before editing `sigma-kernel`.

### 6.5 Merge All Branches & Pull Requests Into Main
- **Definition**: Every approved feature branch and pull request must merge cleanly into `main` so `main` always reflects the complete, integrated state of the component.
- **When to apply**: Upon completing CI checks, tests, and wiki updates for any branch.
- **When NOT to apply**: Unfinished, failing, or unreviewed work—keep it on the feature branch until green.
- **SigmaOS-specific example**: After `cargo test` and `cargo clippy -- -D warnings` pass, merge `feature/<name>` into `main` and delete the branch.

### 6.6 Software Support Program
- **Definition**: Provide structured diagnostics, compatibility verification, and automated troubleshooting tools for all supported SigmaOS components and hardware.
- **When to apply**: Across `SigmaOS-system-profile`, `SigmaOS-survey`, and user-facing diagnostic commands.
- **When NOT to apply**: Experimental, unmerged feature branches.
- **SigmaOS-specific example**: `sigma sys doctor` validates `COMPONENT.toml` integrity, kernel modules, and service health in one command.

### 6.7 Software Updating Program
- **Definition**: Deliver atomic, verified, rollback-capable continuous updates across all SigmaOS system components and applications.
- **When to apply**: In `SigmaOS-update-system` and `SigmaOS-zfs-integration` snapshot hooks.
- **When NOT to apply**: Never perform partial, unverified in-place overwrites of critical boot or kernel files.
- **SigmaOS-specific example**: `SigmaOS-update-system` creates a pre-update ZFS/state snapshot before applying verified rolling updates.

### 6.8 Linux NixOS-Like Configuration System
- **Definition**: Manage the entire SigmaOS system state—packages, services, users, themes, and kernel parameters—through a single declarative, reproducible configuration model.
- **When to apply**: For system provisioning, profile switching, and reproducible machine setups.
- **When NOT to apply**: Ephemeral per-session runtime state (e.g., open window positions or temporary caches).
- **SigmaOS-specific example**: `sigma.toml` declaratively specifies enabled SigmaOS goal profiles, services, and theme settings, compiled atomically into a bootable generation.
- **Code snippet**:
```toml
[system]
hostname = "sigma-workstation"
profile = "developer"

[packages]
enabled = ["sigma-sh", "SigmaOS-vscode", "SigmaOS-docker"]
```

### 6.9 Bootloader Integration
- **Definition**: Seamlessly integrate system generations, kernel images, and fallback recovery entries into `SigmaOS-sigma-bootloader`.
- **When to apply**: Whenever kernel updates, system profile rebuilds, or disk layout changes occur.
- **When NOT to apply**: Purely user-space application updates that do not affect boot targets.
- **SigmaOS-specific example**: `SigmaOS-update-system` automatically registers each new `sigma-kernel` generation with `SigmaOS-sigma-bootloader` and retains the previous working entry for fallback.

### 6.10 Cross Compilation
- **Definition**: Support building SigmaOS binaries and images from a host architecture for target architectures (`x86_64`, `aarch64`, `riscv64`) without requiring native target hardware.
- **When to apply**: In `SigmaOS-xtask` build pipelines, `sigma-kernel`, and `sigma-system`.
- **When NOT to apply**: Host-only developer convenience scripts that never ship to target devices.
- **SigmaOS-specific example**: Build `sigma-system` for `aarch64-unknown-linux-gnu` via `cargo build --target aarch64-unknown-linux-gnu`.

### 6.11 Cross Platform Compatibility
- **Definition**: Write portable Rust abstractions so SigmaOS tooling and user-space utilities operate consistently across supported OS targets and environments.
- **When to apply**: In `sigma-system`, `SigmaOS-cli`, and cross-environment sync tools (`SigmaOS-syncthing`, `SigmaOS-localsend`).
- **When NOT to apply**: Explicitly hardware-bound kernel drivers inside `sigma-kernel`.
- **SigmaOS-specific example**: Use `std::path::PathBuf` and `cfg(target_os = ...)` abstractions rather than hardcoding `/usr/local/bin` everywhere.

### 6.12 Cross Device Compatibility
- **Definition**: Ensure SigmaOS interfaces, themes, and services scale cleanly across desktops, laptops, workstations, VMs, and mobile/touch form factors.
- **When to apply**: In `SigmaOS-ui`, `SigmaOS-deskland`, `SigmaOS-kde-connect`, and power/display profiles.
- **When NOT to apply**: Server-only headless daemons with no UI or battery/display interaction.
- **SigmaOS-specific example**: `SigmaOS-deskland` adapts DPI scaling and input handling automatically between high-DPI laptops and external monitors.

### 6.13 Portability
- **Definition**: Avoid host-specific assumptions, non-standard compiler extensions, or hardcoded absolute paths so SigmaOS builds and runs cleanly anywhere.
- **When to apply**: All Rust crates, shell scripts (`#!/usr/bin/env bash`), and `COMPONENT.toml` manifests.
- **When NOT to apply**: Architecture-specific assembly boot stubs where target-specific `#[cfg(target_arch = ...)]` is explicitly required.
- **SigmaOS-specific example**: Use `dirs` / XDG base directories instead of hardcoding `/home/user/`.

### 6.14 Declarative Package Configuration
- **Definition**: Declare desired packages, versions/channels, and feature flags in version-controlled manifests rather than imperative `install` scripts.
- **When to apply**: In `SigmaOS-system-profile` and component `COMPONENT.toml` files.
- **When NOT to apply**: One-off interactive `sigma pkg` inspection queries.
- **SigmaOS-specific example**: `COMPONENT.toml` declares dependencies and capabilities declaratively so any machine can reproduce the exact environment.

### 6.15 Easy to Download
- **Definition**: Provide clean, fast, single-command or single-click ISO/installer and repository bootstrap mechanisms with clear checksum verification.
- **When to apply**: In `SigmaOS-site`, `BOOTSTRAP.md`, and `INSTALL.md` workflows.
- **When NOT to apply**: Never sacrifice checksum/signature verification for download convenience.
- **SigmaOS-specific example**: Bootstrapping SigmaOS tools requires a single verified command with SHA-256 verification.

### 6.16 Ready to Use
- **Definition**: Ship SigmaOS with sensible, working out-of-the-box defaults—desktop, shell, networking, themes, and core tools configured on first boot.
- **When to apply**: Default system profiles, `SigmaOS-deskland`, `sigma-sh`, and `SigmaOS-ui`.
- **When NOT to apply**: Never enable insecure debug flags or default passwords in the name of "ready to use".
- **SigmaOS-specific example**: First boot launches `SigmaOS-deskland` with pre-configured keybindings, `sigma-sh`, and default `SigmaOS-theme-registry` styling.

### 6.17 Distributed System Management
- **Definition**: Manage fleets of SigmaOS nodes declaratively—pushing profiles, collecting health telemetry, and coordinating updates securely.
- **When to apply**: In enterprise/lab clusters using `SigmaOS-system-profile` and `SigmaOS-rustdesk` / remote management daemons.
- **When NOT to apply**: Single-user offline workstations where no remote control plane is enabled (keep remote listeners off by default).
- **SigmaOS-specific example**: Apply signed declarative `sigma.toml` profiles across multiple SigmaOS nodes via `sigma fleet apply`.

### 6.18 Virtual Environment in a Specific Folder
- **Definition**: Isolate language runtimes, dependencies, and app environments (`SigmaOS-python`, `SigmaOS-wine`, `SigmaOS-bottles`) inside dedicated, deterministic directories rather than polluting global system paths.
- **When to apply**: Whenever managing Python virtualenvs, container roots, or compatibility layers.
- **When NOT to apply**: Core system binaries managed declaratively by `SigmaOS-update-system`.
- **SigmaOS-specific example**: Store per-project Python environments in `.venv/` or `$SIGMA_ENV_DIR/<project>` without modifying `/usr/lib`.

### 6.19 GUI & CLI for All Tools
- **Definition**: Every user-facing SigmaOS tool must provide both a scriptable, automatable CLI and an intuitive GUI backed by the same shared core library.
- **When to apply**: All SigmaOS utilities (package manager, theme switcher, system monitor, updater, network tools).
- **When NOT to apply**: Pure low-level kernel/daemon internals with no direct user interaction (expose CLI diagnostics instead).
- **SigmaOS-specific example**: `SigmaOS-theme-registry` shares one Rust core crate between `sigma theme set` (CLI) and `SigmaOS-ui` Theme Picker (GUI).

---

## 7. Security

### 7.1 Least Privilege
- **Definition**: Grant every process, user, AI agent, and service only the minimum permissions, capabilities, and filesystem access strictly required for its task.
- **When to apply**: Always—across daemons, `systemd`/service units, sandboxes, and API tokens.
- **When NOT to apply**: Never run routine user-space tools as `root` for convenience.
- **SigmaOS-specific example**: `SigmaOS-theme-sync` runs as an unprivileged user with write access restricted solely to the user's theme cache directory.

### 7.2 Secure Defaults
- **Definition**: Ship every SigmaOS component in a locked-down, safe configuration out of the box—TLS enabled, debug modes off, authentication required, and minimal exposed ports.
- **When to apply**: All default configs, `COMPONENT.toml` templates, and daemon startup flags.
- **When NOT to apply**: Never weaken production defaults for local testing convenience; use explicit local dev overrides via env vars.
- **SigmaOS-specific example**: `SigmaOS-rustdesk` and remote services bind to `127.0.0.1` with authentication enabled by default.

### 7.3 Security Audit (API Keys, Passwords, Tokens, Debug Mode, Database Access)
- **Definition**: Continuously audit codebases and diffs to ensure zero hardcoded secrets, disabled debug bypasses, parameterized DB queries, and environment-based credential loading.
- **When to apply**: Before every commit, in CI pipelines, and during periodic swarm audits.
- **When NOT to apply**: Never skip secret scanning—even in test fixtures (use clearly fake dummy constants or env vars).
- **SigmaOS-specific example**: Load all API keys and DB URLs via `std::env::var(...)` and fail fast if missing.
- **Code snippet**:
```rust
pub fn load_api_token() -> Result<String, ConfigError> {
    std::env::var("SIGMAOS_API_TOKEN").map_err(|_| ConfigError::MissingSecret("SIGMAOS_API_TOKEN"))
}
```

### 7.4 Fail-Fast Security Validation
- **Definition**: Reject malformed tokens, invalid signatures, expired certificates, or missing security configs immediately at the boundary without fallback to insecure modes.
- **When to apply**: Authentication, package signature verification, TLS handshakes, and privilege checks.
- **When NOT to apply**: Never fall back to unencrypted HTTP or unverified packages on error.
- **SigmaOS-specific example**: `SigmaOS-update-system` aborts immediately if a package signature fails verification.

---

## 8. Code Reuse

### 8.1 Common Libraries
- **Definition**: Extract shared system primitives (logging, config parsing, security, IPC, filesystem helpers) into `sigma-system` so all SigmaOS repos reuse one battle-tested foundation.
- **When to apply**: Whenever two or more SigmaOS repositories need the same core capability.
- **When NOT to apply**: Domain-specific logic belonging solely to a single tool.
- **SigmaOS-specific example**: `Sigma` (`sigma-system`) provides shared memory, network, security, filesystem, power, and monitoring modules for all component repos.

### 8.2 Code Reusability
- **Definition**: Design functions, traits, and crates with clean parameters and zero hidden global state so they can be reused across CLI, GUI, and daemon contexts.
- **When to apply**: All library crates in SigmaOS.
- **When NOT to apply**: Application entrypoints (`main.rs`) that wire CLI flags to library calls.
- **SigmaOS-specific example**: Keep `stdout` printing out of `sigma-system` library functions; return structured `Result<T, E>` values instead.

### 8.3 Interconnectivity of Multiple Repositories
- **Definition**: Connect all SigmaOS repositories through standardized `COMPONENT.toml` metadata, `tools-sigmaos.sh` scripts, and `SigmaOS-wiki-hub` indexing.
- **When to apply**: Every SigmaOS component repository.
- **When NOT to apply**: Temporary scratch/local-only experiments outside the SigmaOS org.
- **SigmaOS-specific example**: `tools-sigmaos.sh` discovers sibling SigmaOS repos and validates cross-repo health and wiki links.

### 8.4 Consolidate GitHub Repos
- **Definition**: Eliminate redundant, fragmented, or duplicate repositories by consolidating overlapping tools under canonical `SigmaOS-*` repositories.
- **When to apply**: When multiple repos serve the exact same purpose or represent stale splits.
- **When NOT to apply**: Distinct components that genuinely own separate domains per Multi-Repo Modularity.
- **SigmaOS-specific example**: Consolidate scattered documentation `.md` files from 117 repos into `SigmaOS-wiki-hub` / component GitHub Wikis.

### 8.5 Connect Various SigmaOS-Related Repos
- **Definition**: Maintain bidirectional traceability between `Sigma` (master), `sigma-system`, component repos, and `SigmaOS-wiki-hub` via manifests and dependency declarations.
- **When to apply**: Whenever adding a new repo or updating a component's public interface.
- **When NOT to apply**: Never create circular Cargo dependencies between component repos—depend downward on `sigma-system`.
- **SigmaOS-specific example**: `SigmaOS-wiki-hub/manifest.json` and `PARITY_MATRIX.md` track every SigmaOS repository and its wiki status.

---

## 9. Identity

### 9.1 Normalize OS & Components Identity to SigmaOS
- **Definition**: Ensure every crate, binary, CLI banner, config path, UI label, and documentation page consistently uses `SigmaOS` / `sigma-*` branding.
- **When to apply**: All files in all repositories—new and existing.
- **When NOT to apply**: Never leave legacy or external names in user-visible or developer-visible strings.
- **SigmaOS-specific example**: Name binaries `sigma-sh`, `sigma-pkg`, and crates `sigma-system`, with config directories under `~/.config/sigmaos/`.

### 9.2 Hide References to Other Projects
- **Definition**: Remove all references, hints, URLs, or terminology linking SigmaOS components to other operating systems, distributions, or upstream projects.
- **When to apply**: In `README.md`, `AGENTS.md`, `COMPONENT.toml`, source comments, error messages, and wiki pages.
- **When NOT to apply**: Standard technical protocol/format names (e.g., POSIX, Wayland, Rust, SQL, OCI, ZFS) when referring to open standards.
- **SigmaOS-specific example**: Replace any external distro or project names in legacy docs with canonical `SigmaOS` terminology.

### 9.3 Protect Identity of SigmaOS
- **Definition**: Actively guard SigmaOS branding, trademarks, and architectural independence in CI checks, code reviews, and generated AI outputs.
- **When to apply**: Every PR review, automated audit, and wiki publication.
- **When NOT to apply**: Never relax identity checks for convenience.
- **SigmaOS-specific example**: Automated audit scans flag any unapproved external OS/project references before changes land on `main`.

### 9.4 Uphold Intellectual Property
- **Definition**: Guarantee all SigmaOS code, assets, and documentation are original or properly licensed under `GPL-3.0-or-later`, with zero unauthorized third-party IP.
- **When to apply**: Always—every commit, dependency addition, and asset import.
- **When NOT to apply**: Never—IP violations are immediate blockers.
- **SigmaOS-specific example**: Every SigmaOS repository includes the `GPL-3.0-or-later` `LICENSE` file and original SigmaOS-authored source code.
