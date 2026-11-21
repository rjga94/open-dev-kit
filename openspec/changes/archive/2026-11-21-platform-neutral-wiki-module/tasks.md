# Tasks

## 1. Separate the shared Wiki core

- [x] 1.1 Move the reusable Wiki workflows and format/taxonomy guidance into `core/workflows/` and `core/standards/`; update their internal references and verify every referenced source path resolves.
- [x] 1.2 Extract platform-neutral Wiki scope, evidence, approval, and maintenance rules into `core/specialist.md`; keep host-specific tool usage, profile metadata, and handoff instructions out of core and verify the core contains no Copilot/VS Code-specific integration syntax.

## 2. Add the GitHub Copilot adapter

- [x] 2.1 Move the agent profile and capture/query/seed skill shims under `adapters/github-copilot/`; update their references to the shared core and verify each shim still delegates through ODK to the same Wiki operation.
- [x] 2.2 Reshape the Wiki entry in `.opendevkit/agents/manifest.json` to distinguish core sources from GitHub Copilot adapter sources; verify the manifest parses, all declared sources exist, and every existing `installAs` destination is unchanged.
- [x] 2.3 Update installation, readiness, orchestrator, and module guidance references to the new source paths; verify no live documentation or agent source references the old Wiki paths.

## 3. Verify the source-only migration

- [x] 3.1 Run repository-defined validation and `openspec validate platform-neutral-wiki-module`; verify the change validates without a spec delta and no Wiki behavior or runtime data-path changes are introduced.
- [x] 3.2 Check the final adapter/core tree, manifest mappings, preserved GitHub Copilot destinations and command names, and `.opendevkit/wiki/` path; verify no non-Copilot adapter is declared or claimed as supported.
