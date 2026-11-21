# Readiness Refactor

Use this core workflow when the user invokes `/odk-readiness-refactor`. It is available whether or not optional modules are selected. ODK conducts the interview and owns all user communication; the internal Readiness specialist assesses the project and prepares proposed documentation changes.

## Evidence review

Inspect relevant current project guidance, documentation, configuration, tests, and source code. Review Git history only as secondary context. Exclude secrets, credentials, generated output, dependencies, vendored code, and binary files from model context. Treat explicit user decisions as evidence of intent and current project files as evidence of implemented behavior. Do not copy sensitive values into reports.

When project decisions conflict, distinguish the unresolved policy outcome from each source record's stated approval status and authority. Do not relabel an approved record as unapproved, superseded, or not current merely because it conflicts with another approved record. Preserve source records as written unless authoritative evidence or explicit user direction supports changing them; describe unresolved conflicts separately when needed.

Assess the baseline topics:

- Architecture and major project components.
- Project-specific AI guidance and supported agent workflows.
- Engineering standards, conventions, and quality expectations.
- Test strategy, test commands, and the intended scope of verification.

Assess other topics only when project evidence shows they are relevant. For each topic, record a status: `clear/current`, `partial or ambiguous`, `missing`, `stale`, or `contradictory`. A clear/current topic needs no user question or duplicate documentation.

Return concise evidence and unresolved gaps to ODK. ODK asks only the questions needed to clarify missing, partial, stale, or contradictory topics; do not ask the user to repeat established project facts.

## Change preparation

After ODK obtains the necessary answers:

1. Inspect existing AI guidance and relevant project documentation to identify their conventions and the best existing location for each topic.
2. Update an appropriate existing document instead of creating a duplicate. Propose a new document only when no suitable file or project convention exists.
3. Prepare proposed updates only to host-readable AI guidance and relevant project documentation. Do not modify implementation code, tests, or configuration as part of this refactor.
4. Return one consolidated preview to ODK. List every proposed path, whether it is new or changed, why it is needed, and the material being added or revised. Include a diff or complete proposed content when needed to make the change reviewable.
5. Wait while ODK presents the complete preview and obtains explicit user approval. Do not write, partially apply, or otherwise alter proposed files before approval.
6. After approval, apply only the approved documentation changes. If approval is declined or narrowed, leave declined files unchanged and apply only the remaining explicitly approved scope.

Report evidence, classifications, targeted clarification needs, proposed changes, and checks performed to ODK. Do not claim a change was applied unless it was approved and written successfully. Report any write failure and the exact files successfully changed; do not claim the approved set was fully applied if any write failed.

## Optional module setup

Before asking optional-module questions, inspect `.opendevkit/config.json`:

- If `preferences.optionalModulesSetup` is missing, treat setup as `"pending"` (migration behavior for older configs).
- Ask which optional modules to enable only if setup is pending or the user explicitly requests module changes.
- If setup is configured and no change was requested, preserve `enabledModules` and do not ask again.
- If setup is for a workspace other than the active project, confirm the target workspace before preparing it.
- Selecting no modules is valid and means `enabledModules: []`.

After the user makes a selection, prepare a complete exact plan before writes. Use `.opendevkit/agents/manifest.json` for destinations and read each selected optional-module source only as needed. Name every affected path and describe the proposed material/configuration change. Obtain explicit approval for the plan before any write.

- If approved, record only fully installed selected modules in `enabledModules` and set `preferences.optionalModulesSetup: "configured"` when the selection is complete, including `[]` for no modules. Preserve unrelated config preferences.
- If declined, leave all optional-module files and configuration unchanged and leave setup pending.
- Never re-ask about a configured selection merely because the readiness workflow ran again; reopen only for an explicit module-change request.

After overall plan approval, inspect each optional-module destination. If an existing file differs from its proposed content, ask ODK to obtain a separate replacement decision for that exact path. If replacement is declined, leave all files for that module unchanged, do not enable it, and keep setup pending; other independently approved modules may proceed if safe. Never write a conflicting file by assumption. A planned write that fails or becomes unsafe must be reported separately, and no unapproved alternatives may be applied.

## Workspace Allow all check

Before offering Allow all, read the workspace `.vscode/settings.json` and inspect `chat.defaultConfiguration.approvals`.

- If the value is `"allowAll"`, do not offer or ask again.
- If missing or not `"allowAll"`, ask for explicit opt-in to change it.
- A decline leaves workspace settings unchanged.
- After consent, change only `chat.defaultConfiguration.approvals` to `"allowAll"` in the workspace file.
- Preserve JSONC/comments and unrelated settings. Do not modify user-level settings or bypass workspace trust or organization policy.
- If trust or policy prevents the setting, report the restriction and leave it unchanged.

## Optional OpenSpec setup

Assess whether the project already has OpenSpec configuration and project-scoped GitHub Copilot workflow skills. If either is missing, report that state to ODK and offer setup for this project; do not install or initialize automatically. If OpenSpec is already configured, inspect and integrate with it rather than reinitializing or replacing its configuration.

When ODK asks Readiness to assess or carry out approved setup, follow `.opendevkit/workflows/openspec-setup.md`. Verify the resolved CLI path, version, official provenance, project-scope support, and PATH shadowing before any project initialization. Return the evidence and any install/update/setup approval needed to ODK. Never use an unverified CLI or change the machine-wide profile.

When project OpenSpec is configured and `.opendevkit/wiki/` is initialized, offer the one-time post-Archive Wiki capture choice only if `.opendevkit/config.json` has `preferences.postArchiveWikiCapture: "not-offered"`. ODK asks the user once. After an explicit choice, store `"enabled"` or `"declined"` in that field, preserving all other configuration. Do not offer the choice if OpenSpec or the Wiki is unavailable; do not seed a missing Wiki to enable the option. Never trigger automatic capture unless the stored value is `"enabled"`.

## Optional Wiki health check

When the Wiki module is enabled, ask the internal Wiki specialist to check for `.opendevkit/wiki/` and inspect its presence and integrity read-only. Request findings on canonical OKF format, source provenance, references, index, taxonomy, and consistency. The check must not change Wiki files.

- If no Wiki exists, report that to ODK so it can ask whether the user explicitly wants to seed one. Do not scan repository content or create a Wiki unless the user opts in.
- If an existing Wiki has integrity issues, report findings and offer repair or reseeding. Do not start a repository/history seed unless the user explicitly chooses reseed and approves that scan.
- After the user's choice, have Wiki prepare the chosen operation and its proposed file changes. ODK must present the changes and obtain approval before any Wiki writes. If the user declines, leave the Wiki unchanged.
- Repair is limited to the approved Wiki changes and must not perform a broad repository/history scan. Reseeding follows `.opendevkit/modules/wiki/workflows/wiki-seed.md`, including pre-context screening and provenance requirements.

Return the check findings, chosen action, and approval state to ODK. Keep Wiki diagnostics read-only until ODK confirms that the user approved the proposed changes.
