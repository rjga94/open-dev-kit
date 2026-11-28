# Proposal

## Why

The core readiness workflow currently contains Wiki-only health and data-operation questions, coupling core readiness to one optional module. A generic dispatcher with module-owned readiness procedures keeps core behavior reusable across ODK installations while letting each enabled module own its checks and questions.

## What Changes

- Keep core readiness focused on core project concerns and generic optional-module orchestration.
- Ask whether to enable optional modules one at a time with “Would you like to enable the `<module>` module?” (“Yes” / “No”). After each “Yes,” ask unanswered installation questions from that module’s authoritative install guide before asking about the next module; all “No” answers remain a valid empty selection.
- After a module is successfully enabled, run its manifest-declared readiness workflow for module-specific health checks and questions. Do not run that workflow for unselected or incompletely installed modules.
- Move Wiki presence, integrity, seed/repair/reseed, and post-Archive capture readiness prompts into Wiki-owned readiness guidance. Keep Wiki data operations subject to their own explicit opt-ins and plan approvals.
- Require project-specific and module-specific questions to address one unresolved decision at a time with concise, evidence-based closed choices. Keep plan, replacement, and documentation approvals separate.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `project-readiness`: Define generic module readiness discovery and dispatch, sequential module selection, and closed-choice questions while preserving core approval boundaries.
- `project-wiki`: Make Wiki-specific readiness checks and prompts part of the Wiki module's readiness workflow.

## Impact

- `.opendevkit/workflows/readiness-refactor.md`: canonical prompt wording, response formats, and applicability rules.
- `.opendevkit/agents/orchestrator.md`: generic dispatch and user-facing question and approval behavior.
- Wiki module readiness workflow and manifest metadata for declaring it; module manifest validation and focused tests.
- `openspec/specs/project-readiness/spec.md` and `openspec/specs/project-wiki/spec.md`: generic dispatch and module-owned Wiki readiness contracts.
