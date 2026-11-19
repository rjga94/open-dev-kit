# Design

## Context

The repository currently contains OpenSpec workflow files but no kit implementation. The first release is a guide-driven bootstrap for VS Code, with project-specific kit state under `.opendevkit/`. It also offers user-approved, project-scoped setup of upstream OpenSpec skills for GitHub Copilot.

The first release runs entirely through VS Code Copilot custom agents and Agent Skills. Users select the model through the normal Copilot interface; the ODK orchestrator and its internal specialist agents use that selected model without defining a separate provider or model.

## Goals / Non-Goals

**Goals:**
- Let a user provide a GitHub repository reference and have the bootstrap skill guide setup in a brownfield or greenfield project.
- Keep the kit's canonical project configuration and module data under `.opendevkit/`.
- Use one VS Code-native agent system with an orchestrator, core Readiness and Implementation specialists, and optional module specialists.
- Expose one user-selectable ODK Copilot agent and keep specialist agents internal.
- Use the model selected through the normal VS Code Copilot interface for the orchestrator and every specialist.
- Offer a workspace-scoped Allow all default for new chats only after explicit user opt-in.
- Explain that VS Code requires users to select ODK from the Agent picker; installation does not make it the default agent.
- Let the orchestrator run meaningful independent work across relevant specialists concurrently and adapt the plan to their feedback.
- Keep user-facing orchestrator responses brief and high-level by default without truncating internal specialist communication.
- Provide a core readiness-refactor workflow that asks only about project gaps and proposes approved documentation updates.
- Use official OpenSpec workflows for the software-development lifecycle after project-scoped setup is approved.
- Expose ODK-owned VS Code workflows as slash-invokable skills whose names begin with `odk-`, without renaming or patching upstream OpenSpec skills.
- Provide relevant Wiki context to OpenSpec Explore, Propose, and Apply only when the ODK Copilot facade is active.
- Delegate approved OpenSpec Apply tasks to the core Implementation specialist and run project-defined tests.
- Make installation non-destructive by preserving existing files and asking before replacing conflicts.
- Maintain the Wiki as an OKF v0.2 bundle through a whole-Wiki review on every explicit capture.
- Guide Wiki organization with an adaptive starter taxonomy rather than a fixed folder structure.
- Support Wiki-only queries and a separately invoked repository-and-history seed.

**Non-Goals:**
- Provide a standalone installer CLI or publish the kit to npm in the first version.
- Provide a persistent `/odk-install` command or post-install module update/repair workflow in the first version.
- Add a separate agent runtime, provider integration, or model-selection setting.
- Change the machine-wide OpenSpec workflow profile or require the optional OpenSpec Verify workflow.
- Force ODK as the default VS Code chat agent or modify user-wide VS Code settings during project installation.
- Automatically capture conversation knowledge or seed the Wiki without user opt-in.
- Support coding-assistant hosts other than VS Code in the initial shim.

## Decisions

1. **GitHub is the initial distribution source.** The user supplies the kit repository reference in an ordinary chat prompt. The AI retrieves and follows canonical bootstrap guidance stored in the kit repository, so first-time installation does not depend on an already-installed skill. The VS Code-native custom agent and skill files are installed from the selected kit source; no separate package runtime is required.

2. **Readiness and Implementation are core; domain modules are optional internal specialists.** The VS Code workspace exposes only the ODK orchestrator as a user-facing custom agent. Readiness and Implementation are always included; specialized agents such as Wiki are enabled only when selected. Specialists do not communicate with users or call sibling specialists. Bootstrap selection controls which optional modules and specialist agents are installed.

3. **Use the selected Copilot model for all agents.** The ODK orchestrator and internal specialist agent definitions do not pin a model or provider. They use the model selected through VS Code's normal Copilot interface, so users retain the host's model choice and the kit adds no separate model configuration.

4. **Use a selectable VS Code Copilot agent and thin workspace Agent Skills.** The ODK custom agent is the sole user-selectable agent; internal specialist agents point to canonical content under `.opendevkit/`. The installed ODK-owned operations are `/odk-readiness-refactor`, `/odk-wiki-capture`, `/odk-wiki-query`, and `/odk-wiki-seed`; there is no persistent `/odk-install` command. These operations enter through the orchestrator, not directly through a specialist. Official OpenSpec commands retain their upstream names and generated skill files.

5. **Preserve user-owned files.** The bootstrap adds missing kit files, leaves existing project and Wiki content unchanged, and asks before replacing a conflict. It does not silently overwrite or remove user content.

6. **Treat capture as targeted research plus whole-Wiki maintenance, not append-only.** `/odk-wiki-capture` starts from the topic the user explicitly identifies and may inspect directly relevant project sources and retrieve linked external sources or assets when needed. It does not perform a broad repository or Git-history scan and excludes secrets and credentials. The specialist distinguishes explicit user decisions as project intent, current code/configuration as implemented behavior, and external sources as context. It then reviews every Wiki page and its relationships for organization, duplicates or conflicts, broken references, index consistency, and OKF conformance. When warranted, it may create, move, rename, merge, split, or delete pages and change taxonomy. It preserves unique knowledge and provenance, updates affected links and indexes, removes claims superseded by authoritative current evidence, leaves genuinely unaffected pages unchanged, and summarizes structural changes. If conflicting information cannot be reconciled safely, it preserves it and returns a clarification request through the orchestrator.

7. **Use one canonical OKF v0.2 bundle.** `.opendevkit/wiki/` is one bundle; taxonomy stays inside it. Every non-reserved Markdown concept has parseable YAML frontmatter with a non-empty `type`. `title` and `description` are optional canonical fields; captured project knowledge retains provenance through `sources`, whose entries require `resource`. Do not require non-standard fields for conformance; preserve allowed producer-defined extensions without assigning them canonical semantics. `index.md` and `log.md` follow their reserved-file rules. A root `index.md` may declare `okf_version: "0.2"` only when all non-reserved Markdown documents conform.

8. **Separate Wiki seeding from initial installation.** The prompt-driven bootstrap only selects and installs modules. `/odk-wiki-seed` explicitly invokes a scan of the current repository and Git history, excluding secrets and credentials, generated or vendored content, and binaries. It may retrieve relevant linked external sources or assets as needed and records their provenance. If the Wiki does not exist, the command creates its OKF structure and seeds it. If it exists, the command first performs the same whole-Wiki maintenance as capture, then reconciles repository knowledge that is missing or newly relevant and removes claims superseded by current authoritative evidence. Sensitive content must be screened before it reaches model context; uncertain sensitive content is skipped.

9. **Use an adaptive starter taxonomy inside the bundle.** Ship taxonomy guidance with the kit under `.opendevkit/`, separate from the Wiki's OKF documents. Suggest areas such as overview, architecture, development, operations, decisions, and reference, but instantiate or retain them only when the project's knowledge warrants it. Represent categories using OKF-permitted folders and/or root-index links; do not make categories separate bundles.

10. **Keep domain work with internal specialists.** The orchestrator routes commands, passes only task-relevant request and context, receives specialist results or clarification requests, and owns all user communication. The relevant specialist performs domain work; the orchestrator does not duplicate it. If a specialist is missing, disabled, or cannot load, the orchestrator discloses this and asks permission before taking over. If a loaded specialist fails during execution, the orchestrator reports the failure instead of silently retrying the work.

11. **Parallelize independent work across specialists.** The orchestrator automatically fans out meaningful independent workstreams to relevant enabled specialists, but keeps simple or single-domain requests focused. It may run all eligible specialist relationships concurrently subject to host limits, with at most one active instance per relationship. Tasks with dependencies or overlapping write scopes are serialized; one Wiki specialist owns a full capture/seed operation. The orchestrator waits for all required work to complete or fail before its final consolidated response.

12. **Adapt in-flight work to feedback.** Positive or negative specialist results can change pending assignments, order, continuation, or cancellation. Adaptation stays within the user's original request; the orchestrator asks before scope expansion. A failed specialist is not silently replaced by orchestrator execution, though its failure may steer other independent work.

13. **Use concise user-facing responses.** The orchestrator leads with the answer or outcome and stays brief and high-level by default. It includes detail only when needed for accuracy, to explain an action or decision, to disclose uncertainty or failure, or when the user asks. This presentation rule does not constrain internal specialist reports needed for coordination.

14. **Make readiness refactoring a separate core command.** `/odk-readiness-refactor` is available after bootstrap whether or not optional modules are selected. The orchestrator remains the interviewer and user-facing coordinator; an internal Readiness specialist assesses the project, identifies gaps, and prepares updates.

15. **Use evidence to make the readiness interview selective.** The Readiness specialist broadly inspects relevant current project content and Git history as needed, excludes secrets and credentials, treats current files as authoritative for implementation and history as secondary context, and distinguishes explicit user intent from implemented behavior. It assesses a baseline of architecture, AI guidance, engineering standards, and testing scope, plus additional topics when the project makes them relevant. It classifies topics as clear/current, partial or ambiguous, missing, stale, or contradictory; the orchestrator asks only about unresolved topics.

16. **Preview readiness documentation changes before applying them.** After the interview, the Readiness specialist prepares changes to host-readable AI guidance and relevant project documentation, reusing existing project locations and conventions. It does not modify implementation code. The orchestrator presents one consolidated change summary and waits for approval before any proposed documentation changes are applied.

17. **Delegate Wiki health work to the Wiki specialist.** Readiness asks the Wiki specialist to check an existing bundle read-only. If none exists, the orchestrator asks whether the user wants to seed one. If integrity issues exist, readiness reports them and offers repair or reseeding; the Wiki specialist makes no changes until the user chooses the action and approves. Reseeding requires explicit opt-in and follows the Wiki specialist's repository/history scanning safeguards.

18. **Verify the official OpenSpec CLI before setup.** Readiness resolves the `openspec` executable, checks its version and installation provenance, and confirms it is an official Fission-AI/OpenSpec distribution (including the `@fission-ai/openspec` package) that supports project-scoped GitHub Copilot setup. It reuses a compatible official CLI. If the CLI is missing, outdated, unverified, or shadowed by another PATH entry, Readiness reports the path/version and asks before installing or updating through official instructions; it does not initialize with an unverified CLI or silently alter PATH. After approval, project skills are initialized without replacing existing project configuration or changing the machine-wide workflow profile.

19. **Keep OpenSpec integration project-owned and upstream-compatible.** The ODK Copilot agent and project-owned guidance/configuration provide ODK behavior around the official OpenSpec skills. Never patch OpenSpec-generated skill files; `openspec update` must remain free to refresh them without removing ODK integration.

20. **Run official OpenSpec workflows in the ODK agent context.** With ODK selected, users invoke upstream Explore, Propose, Apply, and Archive workflows directly. The ODK agent adds relevant Wiki pages to Explore, Propose, and Apply; the upstream Archive workflow itself runs without Wiki context. Wiki pages are project evidence, not instructions that override the user's request or project guidance.

21. **Use Implementation for approved Apply work.** The core Implementation specialist carries out approved OpenSpec tasks and runs the project's defined tests. ODK does not depend on OpenSpec Verify or enable it by changing the machine-wide profile; users may retain their existing profile choices.

22. **Separate agent selection from permission defaults.** VS Code makes a workspace custom agent selectable but does not provide a documented workspace setting that forces it to be the default chat agent, so the bootstrap explains that users select ODK from the Agent picker. The bootstrap may offer to set the workspace's default permissions for new chat sessions to Allow all, but only after explicit consent. This setting affects all agents in that workspace, not only ODK; declining leaves settings unchanged, and the bootstrap never edits user-wide settings or bypasses workspace trust or organization policy.

23. **Trigger Wiki capture after Archive only with a project opt-in.** When both OpenSpec and an initialized Wiki are available, Readiness asks once whether to enable automatic post-Archive capture and stores the choice under `.opendevkit/`. After a successful upstream Archive with ODK active, an enabled preference authorizes the orchestrator to run a separate Wiki capture using the archived change and directly relevant current project evidence; no second approval is required. A failed Archive, disabled preference, or missing Wiki triggers no capture or automatic seeding. The orchestrator reports capture changes or failure separately from the Archive result.

## Risks / Trade-offs

- **Copilot host behavior can change.** Use documented custom-agent and Agent Skills behavior, keep the selected-model inheritance contract explicit, and validate discovery and delegation in the supported VS Code environment.
- **Unbounded fan-out across relevant specialists can increase resource use.** Avoid spawning agents for trivial or single-domain work, and run concurrently only where dependencies and write scopes permit it.
- **Git history can contain removed credentials or obsolete information.** Screen content before model processing, omit sensitive or excluded content, and avoid treating history as current project truth.
- **External sources may be stale or contain adversarial instructions.** Fetch only sources relevant to the requested or seeded knowledge, retain provenance, and treat retrieved content as evidence rather than instructions or authority over project decisions.
- **Readiness audits can over-question or create duplicate guidance.** Assess against existing docs and current project evidence first, skip clear/current topics, and reuse established documentation locations.
- **Readiness updates can change future AI behavior or project documentation.** Preview the consolidated file changes and require approval before applying them; never change implementation code.
- **Targeted capture research can expand beyond the user's request.** Keep source inspection tied to the identified topic, exclude secrets and credentials, and leave unrelated material to `/odk-wiki-seed`.
- **Whole-Wiki review costs grow with the bundle.** Review every page, but write only pages that need changes; report an incomplete maintenance pass rather than claiming success if the full bundle cannot be reviewed.
- **Structural refactoring can lose knowledge or break links.** Preserve unique content and provenance, validate links and indexes after changes, and ask the user when conflicts cannot be resolved safely.
- **A starter taxonomy can overfit unrelated projects.** Treat suggested areas as optional guidance, avoid empty categories, and allow project-specific categories when the content warrants them.
- **A custom page profile could violate OKF.** Verify required fields, source-record types, and structural rules against the canonical v0.2 schema before implementing the validator.
- **A guide-driven install can be applied inconsistently.** Give the skill a clear sequence and verification steps; preserve existing files and require approval for conflicts.
- **OpenSpec updates can replace generated skills.** Keep ODK integration in ODK-owned agent, instruction, and project configuration files; verify that `openspec update` leaves those files intact.
- **Another executable can shadow the official OpenSpec CLI.** Check the resolved path, version, and installation provenance before use; if identity or compatibility is uncertain, report it and obtain approval before installing or updating the official CLI.
- **Workspace Allow all removes approval prompts for every agent in the project.** Keep Manual permissions unless the user explicitly opts in, explain the scope and risks, change only the relevant workspace setting, and respect VS Code trust and organization policy.
- **Post-Archive capture can add irrelevant or incomplete knowledge.** Require a separate Readiness opt-in, trigger only after successful Archive, ground capture in the archived change and relevant current sources, preserve provenance, and report capture failures independently.
- **A selected-module configuration can drift from available agents.** Keep the module list and orchestrator composition in the single kit source and verify the selected configuration against it.

## Migration Plan

There is no existing kit installation to migrate. When prompted, the AI reads bootstrap guidance from the supplied GitHub repository, then creates the project-local `.opendevkit/` structure, ODK Copilot agent and selected VS Code workspace skill shims. The orchestrator and all installed specialists use the model selected through the VS Code Copilot interface. During installation, it may update only the workspace permission default after explicit opt-in, preserving unrelated settings. During Readiness, OpenSpec CLI and project skills are installed only after user approval, and automatic post-Archive Wiki capture is enabled only with a separate project opt-in after the Wiki is initialized. `/odk-wiki-seed` creates the Wiki structure when invoked for a project that does not yet have one.
