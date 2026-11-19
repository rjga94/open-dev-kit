# Proposal

## Why

Software projects need a repeatable way to add focused AI development capabilities without requiring every project to adopt the same language or workflow. This change establishes a guided, project-local bootstrap for a composable AI dev kit with a project-readiness workflow, OpenSpec-based SDLC integration, and optional Wiki module.

## What Changes

- Add canonical GitHub-hosted bootstrap guidance, invoked by an ordinary chat prompt, that interviews the user about which kit modules to enable and installs selected content.
- Define the kit as a VS Code-native Copilot agent system with a sole user-facing orchestrator, a core internal Readiness and Implementation specialist, and optional domain-owned specialists; commands enter through the orchestrator, which adaptively delegates scoped independent work. All agents use the model selected through the normal VS Code Copilot interface rather than a kit-defined model or provider.
- Add a selectable VS Code Copilot facade for the orchestrator and hidden Copilot-native adapters for internal Readiness, Wiki, and Implementation specialists, backed by canonical `.opendevkit/` guidance.
- Offer an explicit opt-in to set the project workspace's default permissions for new chat sessions to Allow all; never modify user-wide settings. Explain that users still select ODK from the Agent picker.
- Add `/odk-readiness-refactor` as a core workflow that assesses current project files and Git history, asks only about missing, partial, stale, or contradictory readiness areas, and proposes AI-guidance and project-document updates for one user approval.
- When both Wiki and OpenSpec are enabled, let Readiness ask for a one-time project opt-in to automatically update the Wiki after each successful OpenSpec Archive; after opt-in, the orchestrator delegates post-Archive capture to the Wiki specialist without another approval.
- Have Readiness verify the resolved OpenSpec CLI's path, provenance, and version against official [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) before use; offer user-approved official installation or upgrade and project-scoped setup without modifying generated skills or the machine-wide workflow profile.
- Integrate OpenSpec Explore, Propose, Apply, and Archive with the selected ODK Copilot agent; load relevant Wiki context during Explore, Propose, and Apply. Use the core OpenSpec workflow set and omit the optional Verify workflow.
- Add a core Implementation specialist to carry out approved OpenSpec Apply tasks and run project-defined tests; defer a separate independent code-review agent.
- Delegate Wiki integrity checks to the Wiki specialist; ask before seeding a missing Wiki or repairing/reseeding an existing one.
- Keep orchestrator responses brief and high-level by default, adding detail only when needed to answer accurately or explain actions, uncertainty, or failures.
- Add VS Code workspace Agent Skills with `/odk-*` command names; keep canonical kit state and module content under `.opendevkit/`.
- Add Wiki commands for explicit capture grounded in relevant project and external sources, whole-Wiki maintenance and justified structural refactoring, Wiki-only queries, and an explicitly invoked repository-and-history seed that creates or refreshes the Wiki.
- Distinguish project intent, implemented behavior, and external reference context; remove superseded Wiki claims instead of retaining a second history archive.
- Maintain `.opendevkit/wiki/` as one OKF v0.2 Markdown bundle with YAML frontmatter and source provenance; keep the adaptive taxonomy inside that bundle.
- Use canonical OKF v0.2 concept frontmatter with non-empty `type`, optional `title` and `description`, and `sources[].resource` provenance; follow reserved index/log structures and root-index version conformance.
- Exclude secrets and credentials, generated or vendored content, and binaries from Wiki seeding.
- Defer post-install module management, updating, and repair commands.

## Capabilities

### New Capabilities
- `dev-kit-bootstrap`: Guided setup of the composable kit and selected modules in a project.
- `project-readiness`: Evidence-based project-readiness assessment, selective interview, and approved guidance/documentation updates.
- `openspec-workflow-integration`: Project-scoped OpenSpec setup and use with ODK agent and Wiki context.
- `project-wiki`: Explicit project knowledge capture, opted-in post-Archive capture, whole-Wiki maintenance, Wiki-only queries, and opt-in repository seeding.

### Modified Capabilities

## Impact

- Adds a VS Code Copilot custom-agent facade and hidden specialist adapters without patching OpenSpec's generated skills; the agents inherit the user's selected Copilot model.
- Checks the active OpenSpec CLI's official source and version before setup; does not silently replace an unverified CLI or change PATH.
- May update `.vscode/settings.json` only when the user explicitly opts in to workspace-scoped Allow all for new chats; the setting applies to all agents in that workspace.
- After a separate project opt-in during Readiness, a successful OpenSpec Archive can invoke Wiki maintenance using the archived change and relevant implementation evidence.
- Adds GitHub-hosted bootstrap guidance and VS Code workspace skills for Wiki workflows.
- Creates project-local kit state and Wiki content under `.opendevkit/`.
- All agent execution uses VS Code Copilot; the kit does not provide a separate agent runtime.
