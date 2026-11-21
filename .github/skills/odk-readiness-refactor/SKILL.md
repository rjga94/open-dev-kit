---
name: odk-readiness-refactor
description: Assess project readiness and prepare approved AI-guidance and documentation updates
---

This is a core ODK command and is available even when no optional modules are enabled. It enters through the ODK orchestrator.

1. Read `.opendevkit/workflows/readiness-refactor.md`.
2. Delegate evidence review and readiness classification to the internal Readiness specialist.
3. Before optional-module questions, inspect `.opendevkit/config.json` and treat a missing `preferences.optionalModulesSetup` as `"pending"`.
4. Ask about optional modules only when setup is pending or the user explicitly requests module changes. For another workspace, confirm it before preparing setup. Do not re-ask completed setup.
5. After explicit plan approval, record only fully installed modules in `enabledModules`; set `preferences.optionalModulesSetup: "configured"` when the approved selection is complete, including an empty list for no modules. Keep setup pending if a selected module is skipped after a declined conflict replacement. If the plan is declined, leave optional files and configuration unchanged and leave setup pending.
6. Prepare an exact path/content plan and read the source manifest plus only selected module sources. Obtain approval before any optional-module or configuration write. Ask separately before replacing each conflicting optional-module file; if replacement is declined, skip all writes for that module and do not enable it. Continue only with other approved modules that remain safe.
7. Check workspace `.vscode/settings.json` for `chat.defaultConfiguration.approvals === "allowAll"` before offering it. Do not offer it again when already enabled. If disabled or absent, ask before changing only that workspace setting. Preserve JSONC/comments/unrelated settings, make no user-level change or bypass, and report trust or policy restrictions.
8. Ask the user only about unresolved readiness topics reported by Readiness.
9. Have Readiness prepare one consolidated documentation preview after clarification.
10. Present the preview and wait for approval before applying any proposed documentation changes.

Readiness returns findings and proposed changes only to ODK. It does not communicate directly with the user or modify implementation code.
