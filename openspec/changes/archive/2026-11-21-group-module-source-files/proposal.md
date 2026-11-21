# Proposal

## Why

Optional module source files are scattered across shared agent, skill-template, and workflow directories, making each module harder to understand and maintain as a unit. Grouping a module's canonical source files together will make module ownership clearer and simplify future module additions without changing installed behavior.

## What Changes

- Group optional-module source assets under `.opendevkit/modules/<module>/`.
- Update the module manifest and installation/readiness guidance to resolve canonical sources from each module directory.
- Keep shared core instructions and project-wide configuration outside module directories.
- Preserve VS Code installation destinations and the target project's `.opendevkit/wiki/` knowledge bundle path.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

None. This is an internal source-layout refactor with no intended behavior change; the change opts out of spec deltas.

## Impact

- `.opendevkit/agents/manifest.json` and optional module source files.
- `INSTALL.md` and the readiness workflow's module-install guidance.
- Existing installation destinations, shared ODK configuration, and project Wiki data remain unchanged.
