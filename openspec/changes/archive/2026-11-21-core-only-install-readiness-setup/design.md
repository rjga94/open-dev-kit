# Design

## Context

See `proposal.md` for motivation. `INSTALL.md` is retrieved before ODK exists in a target project, while `/odk-readiness-refactor` is available only after the core kit is installed. The current `.opendevkit/config.json` records enabled modules but does not distinguish an unasked selection from a deliberate choice to enable none.

## Goals / Non-Goals

**Goals:**
- Keep the initial installation limited to core ODK and independent of the Readiness skill.
- Let Readiness own optional module and workspace-permission setup choices after core installation.
- Avoid overwriting existing core files and avoid asking again about completed setup.

**Non-Goals:**
- Installing or seeding Wiki content during core installation.
- Changing user-wide VS Code settings.
- Changing the existing documentation-refactor approval boundary.

## Decisions

1. **Make `INSTALL.md` a non-interactive core installer.** Use the project explicitly named by the install request, or the active project when the request targets it. If the target cannot be determined, report that and stop rather than starting an interview. Resolve core files from the kit manifest; do not install optional modules or change workspace settings.
2. **Preflight all core destinations before writing.** Treat absent paths and paths already containing the same ODK content as safe. If any core target contains different content, report all conflicting paths and stop before writing any core files. This avoids partial installation and does not require the uninstalled Readiness skill to ask for replacement approval.
3. **Record optional setup state separately from module selection.** Initialize `preferences.optionalModulesSetup` to `pending` in the core config. Readiness asks about optional modules only while setup is pending; after the user approves a selection, it records the successfully enabled modules and marks setup `configured`, including when the user selected none. A declined plan leaves setup pending for a later invocation. If a selected module is skipped after a declined conflict replacement, do not write any files for that module or enable it; leave setup pending while allowing other independently approved modules to proceed. An explicit request to change modules reopens the selection flow.
4. **Have Readiness inspect settings before asking.** It checks current module configuration and workspace permissions on each invocation. It does not re-ask about a completed module selection unless the user requests a change, and does not offer Allow all when the workspace setting is already enabled. If the workspace setting is not enabled, it asks for explicit opt-in; a decline leaves settings unchanged. The setting remains workspace-scoped.
5. **Keep optional-file conflict handling interactive and module-atomic.** After module selection, Readiness presents the exact planned paths and obtains approval before writes. It asks separately before replacing any conflicting optional-module file. If replacement is declined, skip all writes for that module and do not enable it; only independently approved modules that remain safe may proceed.

## Risks / Trade-offs

- [The initial install may stop on a conflicting core file] → Report every conflicting path before writing and direct the user to resolve the conflict before retrying.
- [Readiness gains responsibility for installing optional modules and changing workspace settings] → Keep those writes behind an explicit preview and user approval, and keep the core installer out of that scope.
- [The added setup-state field may be absent from older configs] → Treat a missing value as `pending`; preserve all unrelated configuration when updating it.
- [A declined Allow all offer can recur while the setting remains disabled] → Check the actual workspace setting before every offer and never change it without explicit opt-in.

## Migration Plan

1. Make `INSTALL.md` the canonical install guide and update repository references.
2. Change the guide to install only core content, preflight all core targets, and stop without writes on conflicts.
3. Update the Readiness skill and workflow to handle pending optional setup, optional-file approvals, and the workspace Allow all check.
4. Update core configuration templates and manifest-related validation for the pending setup marker.
5. Validate the clean-install, conflict, no-modules, optional-module, declined-approval, and already-enabled-Allow-all paths.

Rollback is a repository change revert; no project data migration is needed. Projects with an older config and no setup marker are treated as having pending optional setup.

