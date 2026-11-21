# Tasks

## 1. Write repository-internal module guidance

- [x] 1.1 Add a root-level `CONTRIBUTING.md` module-maintenance section documenting the `core/` versus host-adapter boundary, canonical source and `installAs` manifest mappings, separation of runtime project data, and the rule to add only validated platform adapters; verify the guidance matches the current Wiki layout and manifest.
- [x] 1.2 Include a concise maintenance checklist for source references, manifest validity, adapter/command/install mapping, relevant OpenSpec updates, and scoped validation; verify it is actionable for future modules without describing unsupported platform behavior.

## 2. Verify the project boundary

- [x] 2.1 Confirm the contributor guide is repository-only and is not added to `.opendevkit/`, the module manifest, or any install destination; verify installation guidance and project-facing prompts remain unchanged.
- [x] 2.2 Run `openspec validate add-module-maintenance-guide` and `git diff --check`; verify only contributor documentation and the OpenSpec change artifacts are affected.
