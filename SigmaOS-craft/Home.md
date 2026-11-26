# SigmaOS Craft

Crafting system for SigmaOS — item registry, recipes (ingredients → output), inventory management, and craft operations with atomic JSON state persistence.

## Capabilities

- `CraftState`: item + recipe registries (`BTreeMap`), `Inventory` with add/remove/has-ingredients
- `can_craft`, `craft` (consumes ingredients, produces output), `craftable` listing
- Validation rejects empty item/recipe ids; `Insufficient`/`RecipeNotFound` errors
- `save`/`load` via temp-file + rename for atomic persistence; `starter_state()` seeds wood/plank/stick/stone/torch examples
- CLI in `src/main.rs`; 6 unit tests cover inventory, crafting atomicity, craftable, validation, and round-trips (commit `f5d5df3`)

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-craft)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
