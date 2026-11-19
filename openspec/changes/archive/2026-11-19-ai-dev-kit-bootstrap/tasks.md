# Tasks

## 1. VS Code Copilot agent structure

- [x] 1.1 Define ODK as the sole user-facing agent with Readiness and Implementation as core specialists and Wiki as an optional internal specialist; verify VS Code exposes only ODK in the Agent picker.
- [x] 1.2 Define core/optional specialist relationships and module-selection configuration; verify Readiness and Implementation are always enabled, only selected optional specialists are enabled, and specialists cannot call sibling agents.
- [x] 1.3 Define the agent handoff contract; verify the orchestrator passes scoped context, specialists return results/clarification only to the orchestrator, and domain work stays with the relevant specialist.
- [x] 1.4 Define and verify unavailability fallback behavior: disclose a missing, disabled, or unloadable specialist and get user approval before orchestrator takeover; report loaded-specialist execution failures without silent retry.
- [x] 1.5 Define orchestrator fan-out and join behavior; verify meaningful independent tasks run concurrently across relevant specialists, at most one instance runs per relationship, dependencies and overlapping write scopes serialize, feedback adapts pending work only within the original request, and the final response waits for all required tasks.
- [x] 1.6 Document the Readiness workflow, OpenSpec SDLC integration, concise user-facing response policy, GitHub-hosted prompt-driven bootstrap guidance, model selection through VS Code, and deferral of post-install module management; verify docs distinguish user-facing style from internal specialist reporting.
- [x] 1.7 Add the selectable VS Code ODK agent and hidden Readiness, Wiki, and Implementation agents; verify canonical guidance remains under `.opendevkit/`, only ODK is user-selectable, and all agents use the model selected in the normal Copilot interface.

## 2. Prompt-driven bootstrap

- [x] 2.1 Add canonical bootstrap guidance to the kit's GitHub source; verify a user can start installation with an ordinary chat prompt in a clean project without any pre-installed kit skill.
- [x] 2.2 Document the GitHub-based module-selection interview and non-destructive file handling; walk through greenfield, brownfield, and conflicting-file cases in Copilot and verify module selection, error reporting, and approval-before-replacement behavior.
- [x] 2.3 Add initial-install verification guidance for users; verify it checks selected modules, `.opendevkit/` state, and installed module skill shims.
- [x] 2.4 Verify bootstrap installs the ODK Copilot facade and only the selected optional module adapters and commands; verify specialists remain internal and the user is told to select ODK from the Agent picker.
- [x] 2.5 Offer an explicit opt-in to set the workspace default permissions for new chats to Allow all; verify declining leaves settings unchanged, accepting changes only the relevant workspace setting, unrelated settings are preserved, user-wide settings are untouched, and policy/trust restrictions are respected.

## 3. Readiness and Wiki workflows

- [x] 3.1 Implement `/odk-wiki-capture` and canonical instructions; verify one Wiki specialist handles each operation, researches only the identified topic using relevant project and linked external sources, records provenance, distinguishes user intent from implemented behavior, removes superseded claims, and can restructure the whole Wiki while preserving unique knowledge, repairing links/indexes, leaving unaffected pages unchanged, summarizing changes, and escalating unresolved conflicts.
- [x] 3.2 Implement `/odk-wiki-query` to search only `.opendevkit/wiki/`; verify it answers from Wiki content and reports missing information without searching project files.
- [x] 3.3 Implement `/odk-wiki-seed` for current repository and Git history scans, retrieving relevant external references as needed; verify it creates or refreshes the Wiki, removes claims superseded by authoritative current evidence, retains provenance, and excludes generated, vendored, binary, and fake-secret fixture content from model context and Wiki output.
- [x] 3.4 Verify the canonical OKF v0.2 schema before implementing validation; validate required non-empty `type`, optional `title` and `description`, `sources[].resource`, reserved `index.md`/`log.md` structures, and the root-index rule that `okf_version: "0.2"` appears only when all non-reserved Markdown documents conform.
- [x] 3.5 Add adaptive taxonomy guidance under `.opendevkit/`; verify starter categories are optional, empty categories are not created, taxonomy stays inside one OKF bundle, and capture can add or remove categories when content warrants it.
- [x] 3.6 Document Wiki responsibilities, source precedence, external-source handling, superseded-claim cleanup, commands, whole-Wiki capture behavior, OKF v0.2 format, and taxonomy guidance; verify all user-invokable skill names use the `odk-` prefix and the query is Wiki-only.
- [x] 3.7 Implement `/odk-readiness-refactor` with the core Readiness specialist; verify it assesses the baseline and relevant project-specific topics, classifies readiness states, and asks only about missing, partial, stale, or contradictory areas.
- [x] 3.8 Implement readiness updates to AI guidance and relevant project documentation; verify existing conventions are reused, implementation code is untouched, and one consolidated preview is approved before any changes are applied.
- [x] 3.9 Integrate the Readiness workflow with the Wiki specialist; verify Wiki checks are read-only, missing Wiki offers opt-in seed, and existing integrity issues offer repair/reseed without changes until user choice and approval.
- [x] 3.10 Document Readiness command behavior and its evidence/approval boundaries; verify it is available after bootstrap even when no optional modules are selected.
- [x] 3.11 Implement the Readiness OpenSpec setup offer; verify the resolved CLI path, version, and provenance against official Fission-AI/OpenSpec, reuse only a compatible official CLI, require approval before installing/updating, and preserve project configuration and the machine-wide profile.
- [x] 3.12 Add ODK-owned OpenSpec context through the Copilot facade and project configuration; verify upstream-generated skill files are not modified and the ODK integration survives `openspec update`.
- [x] 3.13 Add a one-time Readiness opt-in for automatic Wiki capture after OpenSpec Archive; verify it is offered only when OpenSpec and an initialized Wiki are available and the preference is stored under `.opendevkit/`.
- [x] 3.14 Trigger a separate Wiki capture after successful Archive when the project opt-in is enabled; verify the Wiki specialist uses the archived change and directly relevant current sources without a second approval or broad repository/history scan.

## 4. Integration verification

- [x] 4.1 Verify the prompt-driven bootstrap enables only selected module commands and preserves existing project and Wiki content; test clean and conflicting target projects, including a project with no prior kit installation.
- [x] 4.2 Run end-to-end capture and seed operations on empty and multi-page OKF fixtures with stale claims, conflicting user intent/current implementation, and linked external sources; verify relevant-source provenance, correct source distinctions, removal of superseded claims without Wiki archival copies, adaptive refactoring, repaired references/indexes, clarification escalation, and unchanged unrelated pages.
- [x] 4.3 Exercise orchestrator fan-out with multiple specialists; verify it joins required results, adapts outstanding work to positive/negative feedback, preserves the original scope, serializes dependencies/write conflicts, and reports failures and partial results.
- [x] 4.4 Verify straightforward user requests receive brief high-level responses, while actions, decisions, uncertainty, and failures include necessary detail; verify internal specialist handoffs retain the information needed for coordination.
- [x] 4.5 Verify installed `/odk-*` module command shims route through the orchestrator contract without exposing specialists, and verify all agents use the model selected in the normal VS Code Copilot interface.
- [x] 4.6 Exercise readiness against clear/current, missing, stale, and contradictory project evidence, including filtered Git history; verify skipped questions, targeted interview, one change preview, and no edits when approval is declined.
- [x] 4.7 Run the focused OpenSpec/spec and skill validation checks; verify the change requirements, slash command names, and VS Code discovery locations are consistent.
- [x] 4.8 Exercise upstream OpenSpec Explore, Propose, Apply, and Archive with ODK selected; verify relevant Wiki context is supplied only to Explore, Propose, and Apply, Archive itself runs without Wiki context, Apply delegates to Implementation and runs project tests, Verify is not required or added by ODK, and `openspec update` preserves ODK-owned files.
- [x] 4.9 Verify the workspace Allow all opt-in affects only new chats in the target workspace, applies to all agents there, does not alter the current session or user-wide settings, and reports when trust or organization policy blocks it.
- [x] 4.10 Verify a successful Archive triggers capture only after project opt-in; declined/unset opt-in, failed Archive, or missing Wiki causes no automatic Wiki writes or seeding, and a capture failure is reported separately from Archive success.
- [x] 4.11 Test OpenSpec CLI detection with no CLI, a compatible official CLI, an unsupported official version, an unverified CLI, and multiple PATH entries; verify no project init runs with an unverified executable and the user approves any official install or update.

## 5. Apply completion

- [x] 5.1 Sync delta specs into main specs and verify the intended requirements are present.
- [x] 5.2 Capture durable project knowledge to the wiki and verify relevant pages and indexes, or report that nothing new needed capture.
- [x] 5.3 Archive the change after sync and wiki capture, then verify its archive path.
- [x] 5.4 Commit the completed work and verify the resulting commit hash.
