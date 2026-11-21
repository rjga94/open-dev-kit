# Proposal

## Why

ODK's module sources now distinguish shared domain guidance from host-specific adapters, but the repository has no contributor-facing guide for maintaining that boundary. A repository-only guide will help future ODK development preserve module consistency without changing anything installed into projects that use ODK.

## What Changes

- Add a root-level `CONTRIBUTING.md` section for maintaining ODK modules.
- Document the shared `core/` versus host `adapters/` boundary, manifest source/destination mappings, project-data separation, adapter support expectations, and a focused validation checklist.
- Keep this guidance internal to the ODK source repository; do not add it to `.opendevkit/`, the module manifest, install targets, project-facing prompts, configuration, commands, or runtime workflows.
- Treat module behavior changes separately from source organization: update capability specifications only when a module's observable contract changes.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

None. This change adds repository contributor documentation only and does not change ODK installation or project behavior. Specs are intentionally skipped.

## Impact

- Adds `CONTRIBUTING.md` at the ODK repository root.
- No changes to code, module manifests, installation assets, project configuration, or user-facing behavior.
