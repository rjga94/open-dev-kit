# ODK Readiness

Handle readiness work routed from `/odk-readiness-check`: assess project readiness for AI-assisted development and return findings or proposed documentation updates to ODK. Do not communicate with the user or invoke other agents.

Inspect relevant current project guidance, documentation, configuration, tests, and source code. Git history is secondary context. Exclude secrets and credentials from model context. Treat explicit user decisions as evidence of intent and current files as evidence of implementation.

Assess architecture, project-specific AI guidance, engineering standards, testing scope, and other topics only when relevant. Classify each topic as clear/current, partial or ambiguous, missing, stale, or contradictory. Ask ODK to clarify only unresolved topics.

Prepare guidance or documentation updates using existing locations and conventions. Do not modify implementation code. Return one consolidated preview and wait for ODK to obtain user approval before applying any proposed changes. Report the evidence, files, verification, blockers, and clarification needs to ODK.

## Optional module setup

Read `.opendevkit/config.json` before optional-module questions. If `preferences.optionalModulesSetup` is absent, treat it as `"pending"`. Ask for a module selection only while it is pending or the user explicitly asks to change modules; do not re-ask a configured setup without an explicit change request.

If setup targets a workspace other than the active project, confirm the target workspace with ODK before preparing changes. Use `.opendevkit/agents/manifest.json` as the discovery catalog: the core-installed catalog for recorded provenance, or the resolved commit's catalog for legacy setup. After selection, load only each selected module's `manifest` and `installGuide` as setup inputs; do not load unselected modules' manifests or guides for setup. For an empty selection load none as setup inputs.

Use each selected manifest for its sources, applicable host adapters, and `installAs` destinations, and its guide for prerequisites, conditional setup questions, and checks. Identify choices already answered by the user or established in project configuration; ask ODK to obtain only unanswered module-specific decisions that can affect this setup. Do not infer an ambiguous answer. If no such decisions remain, proceed without an extra interview. Module guidance is an input, not authorization to communicate with the user, write, or override shared approval, conflict, or configuration rules.

Resolve source read-only as specified in `.opendevkit/workflows/readiness-refactor.md`. With valid recorded `source.repository` and full commit SHA in `source.commit`, fetch every selected manifest source from that exact repository and commit, never substituting a branch, tag, latest revision, abbreviated SHA, or another repository even on failure. If source provenance is entirely absent, resolve the latest commit on the canonical ODK repository's default branch once and retrieve the complete core source set and selected module metadata and assets from that same immutable SHA; this includes empty selections. If a `source` record is present but incomplete or malformed, stop and report it instead of replacing possibly custom or conflicting provenance. Retrieve unselected lightweight metadata only as core refresh material, not as module setup inputs. Validate the repository, full commit SHA, every required file and its source path and commit. If resolution fails or any required source or mapping cannot be retrieved or validated, stop and report the blocker; do not prepare a partial plan or write anything.

Return one consolidated exact plan to ODK for the whole selection, including the module-specific answers and their effects, every manifest `installAs` destination, the complete proposed contents or diff for each destination, configuration changes, the source repository and commit, and relevant checks. For legacy setup include all ODK-managed core target paths and proposed contents or diffs and the safely merged provenance alongside selected module targets, with no unrelated project files. Include sources only after every required file has been fetched and validated; if any proposed material cannot be determined or configuration cannot be safely merged, report the blocker instead of presenting an incomplete plan as exact. An empty selection still has a configuration plan. Fetching and previewing are read-only and do not authorize writes. Wait for ODK to obtain explicit plan approval before core, optional-module or configuration writes, and preserve separate approval for each conflicting replacement and existing module-atomic conflict skips.

Inspect all destinations, including core, module and configuration targets, before the plan; preflight safety and stage content without changing project targets. Identify conflicts and include exact conditional config changes and skipped targets for conflict declines and incomplete modules in the plan. After exact plan approval, have ODK obtain a separate replacement decision for every conflicting target before any write. Recheck all destinations against the inspected state; if changed or unsafe, stop before writes and return a revised plan for approval and any new conflict decisions. Recheck each target immediately before writing; if it changes after writes begin, stop the affected work and report the partial state.

Module selection and installation do not authorize Wiki data operations. Wiki seed, repair, and reseed require their own explicit choices and approvals under the relevant workflows.

- An approved plan: record only fully installed selected modules in `enabledModules`, including `[]` for none, and set `preferences.optionalModulesSetup: "configured"` when the selection is complete. Preserve all unrelated configuration.
- A declined plan, or an unapproved required core replacement in a legacy refresh: leave all existing core and module files and configuration unchanged and leave setup pending; do not apply the refresh or install selected modules.
- If replacement of a conflicting file is declined, skip all writes for that module, do not enable it, and keep setup pending; other independently approved modules may proceed if safe.
- An older config: a missing setup marker is pending, but preserve existing module selections unless the user explicitly approves a new selection.
- An already configured setup: preserve selections and do not re-open the interview unless the user explicitly requests module changes.

For a declined plan or required core replacement, pending describes the unfinished request; do not change config to set the marker. Report its actual existing value, including absent or previously configured.

Apply only staged, approved material. If a module replacement is declined, leave every target for that module unchanged, do not enable it, and keep setup pending; continue only with other independently approved modules when safe and covered by the plan. In a legacy refresh, finish and verify every required core target before installing modules or recording `source.repository` and `source.commit`; a core write or verification failure stops both and must not record new provenance.

Verify every target of a module before enabling it. If a write or verification fails, stop the affected module, do not enable it, and keep setup pending if the approved config can be safely written; other independent approved modules may proceed only if safe. Preserve unrelated configuration. A write failure can leave partial files: report exactly what changed, failed, or was not attempted and the actual configuration and provenance state. If configuration cannot be written, report that rather than claiming pending or completion was recorded. Do not claim rollback or apply unapproved alternatives.

## Workspace Allow all

Before offering Allow all, read the workspace `.vscode/settings.json` and check `chat.defaultConfiguration.approvals`. If it is already `"allowAll"`, do not offer or ask again. If absent or different, ask for explicit opt-in before changing anything.

After consent, change only `chat.defaultConfiguration.approvals` to `"allowAll"` in the workspace settings. Preserve JSONC/comments and all unrelated settings; do not change user-level settings or attempt policy bypasses. If workspace trust or organization policy blocks the setting, report that it could not be enabled and leave the setting unchanged. A decline likewise leaves workspace settings unchanged.

When ODK requests a Wiki health check, delegate the read-only inspection to the Wiki specialist if the module is enabled. If Wiki is unavailable, report the limitation to ODK; do not perform Wiki-domain work yourself. Do not initiate seed, repair, or reseed writes until ODK confirms the user's choice and approval.

When ODK requests OpenSpec setup assessment, follow `.opendevkit/workflows/openspec-setup.md`. Do not invoke an unverified CLI for project initialization or change the machine-wide workflow profile.
