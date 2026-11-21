# Proposal

## Why

The Wiki module's sources are grouped together, but shared operating guidance and GitHub Copilot-specific entrypoints are still organized by file type rather than by platform boundary. Separating a platform-neutral core from host adapters will make it possible to add another integration without duplicating Wiki behavior or coupling it to VS Code conventions.

## What Changes

- Organize reusable Wiki specialist policy, workflows, and format/taxonomy guidance under a `core/` directory.
- Organize GitHub Copilot agent and skill entrypoints under an `adapters/github-copilot/` directory.
- Update the central module registry and installation/readiness guidance to map the Wiki core and adapter sources while preserving current GitHub Copilot install destinations.
- Keep current Wiki commands, runtime behavior, approval boundaries, and `.opendevkit/wiki/` data location unchanged.
- Prepare an extension point for additional host adapters, without implementing or claiming support for another platform in this change.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

None. This is a source-layout and integration-organization refactor with no intended user-visible or runtime behavior changes. Specs are intentionally skipped.

## Impact

- `.opendevkit/modules/wiki/` sources and references to them.
- `.opendevkit/agents/manifest.json` and installation/readiness guidance that resolves module sources and destinations.
- No changes to the Wiki data bundle, Wiki command behavior, dependencies, or supported runtime platforms.
