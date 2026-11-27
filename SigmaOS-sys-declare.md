# SigmaOS-sys-declare

**Category:** Config  
**License:** GPL-3.0-or-later  
**Rolling release:** Yes

Declarative system configuration with diff-and-apply semantics. Describe the desired state in a `SystemSpec`; the engine diffs against current state and produces a minimal `DiffPlan` listing only the changes required.

## Change Types

| Change | Description |
|--------|-------------|
| `Install` | Component not present in current state |
| `Remove` | Component not present in desired state |
| `Update` | Version or params differ |
| `SetEnabled` | Enabled flag differs |

## Tests: 6 AAA

## See Also
- [SigmaOS-rollback](SigmaOS-rollback)
- [SigmaOS-config-system](SigmaOS-config-system)
- [SigmaOS-pkg-core](SigmaOS-pkg-core)
