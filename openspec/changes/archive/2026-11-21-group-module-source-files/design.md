# Design

## Context

See `proposal.md` for the motivation. The Wiki module's canonical sources currently span `.opendevkit/agents/`, `.opendevkit/skill-templates/`, and `.opendevkit/workflows/`. The central agent manifest maps these sources to VS Code installation destinations. The Wiki specialist and shared readiness/orchestrator guidance refer to workflow paths directly.

## Goals / Non-Goals

**Goals:**
- Keep each optional module's canonical agent instructions, profile template, skill sources, and module workflows together under `.opendevkit/modules/<module>/`.
- Make the module manifest and all source references resolve to the new locations.
- Preserve existing install destinations and module behavior.

**Non-Goals:**
- Moving shared core agents, core workflows, the central module manifest, or `.opendevkit/config.json`.
- Moving or changing the target project's `.opendevkit/wiki/` knowledge bundle.
- Changing installed VS Code paths or the Wiki's user-visible commands and behavior.
- Moving OpenSpec specifications or repository-level Wiki documentation into module source folders.

## Decisions

### Store optional-module sources beneath a module directory

Use `.opendevkit/modules/<module>/` as the canonical source root. For Wiki, keep its specialist instructions and profile template, three skill sources, and Wiki-specific workflows in that directory, using subdirectories for agents, skills, and workflows. This gives current and future optional modules a consistent boundary.

The alternative—keeping shared `agents/`, `skill-templates/`, and `workflows/` directories and relying on names to identify ownership—preserves the current layout but leaves module files scattered.

### Keep the central manifest as the installation registry

Keep `.opendevkit/agents/manifest.json` as the single registry read by installation and readiness. Update each module entry's source paths to point into its module directory; retain `installAs` destinations unchanged. This avoids introducing a second discovery mechanism or duplicating module-selection metadata.

The alternative—adding a manifest inside each module—would make modules more independently described but require discovery and merge rules that are unnecessary for the current single optional module.

### Separate kit sources from project-owned Wiki data

Keep source workflows under `.opendevkit/modules/wiki/` and keep runtime knowledge under `.opendevkit/wiki/`. Update Wiki instructions and shared readiness/orchestrator references to the new source paths, without changing the runtime bundle path or its contents.

### Preserve installation behavior

Treat this as a source-only move. `INSTALL.md`, the manifest, and readiness guidance must resolve canonical source paths from the new layout while generated or copied agent/skill files continue to use their existing destinations. No migration of already-installed target projects is required because their installed paths and runtime data locations do not change.

## Risks / Trade-offs

- **A stale source reference can break installation or delegation** -> Update all manifest entries and references in module and shared guidance together; validate that every referenced source exists and that every module source is under its module directory.
- **Source paths could be confused with installed or runtime paths** -> Keep `source` and `installAs` distinct in the manifest and explicitly retain `.opendevkit/wiki/` for project data.
- **No dedicated test files are currently present** -> Validate manifest paths and documented install mappings with focused checks, and run any repository-defined validation available during implementation.

## Migration Plan

Move the Wiki-owned source files into the module directory, update the central manifest and every affected source-path reference in install, module, and shared workflow guidance, then verify the source references and install destinations. Rollback consists of restoring the previous paths and references; no target-project data migration is needed.
