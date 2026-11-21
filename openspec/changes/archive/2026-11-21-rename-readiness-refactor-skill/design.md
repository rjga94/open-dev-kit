# Design

## Context

The readiness workflow is exposed as the `/odk-readiness-refactor` skill, declared in the ODK agent profile and `.opendevkit/agents/manifest.json`. Its instructions live in `.github/skills/odk-readiness-refactor/SKILL.md` and the canonical `.opendevkit/workflows/readiness-refactor.md`; the command is also referenced by the orchestrator, Readiness guidance, installation guide, tests, and existing capability specs. The change replaces the public command name while preserving the workflow behavior; see `proposal.md` and the delta specs.

## Goals / Non-Goals

**Goals:**
- Make `/odk-readiness-check` the only current user-invokable name for the existing readiness workflow.
- Keep ODK discovery and all active documentation, tests, and requirements consistent with the new name.
- Preserve the canonical workflow file path and its existing operational behavior.

**Non-Goals:**
- Change readiness assessment, setup, approval, or documentation-update behavior.
- Keep `/odk-readiness-refactor` as an alias.
- Rewrite archived change records, which describe the historical command name.

## Decisions

- **Rename the skill directory and its declared name together.** Move the skill to `.github/skills/odk-readiness-check/SKILL.md`, update its frontmatter name, and update the agent profile and catalog references. This keeps VS Code discovery, metadata, and the installed skill source aligned. Leaving the old directory or exposing two skill names was rejected because the user chose replacement rather than a compatibility alias.
- **Retain the canonical workflow file path.** Keep `.opendevkit/workflows/readiness-refactor.md` as the internal canonical workflow location while updating the command references and user-facing title inside it. Renaming that file would add path churn to its consumers without changing the user-facing skill identity.
- **Update active references, not archived history.** Change the current agent instructions, installation guidance, tests, and both affected capability deltas. Archived proposals and specs remain historical records and are not rewritten.
- **Use the existing focused guidance tests.** Update their skill path and add coverage that the new command is declared consistently and the old command is not exposed as an alias; run the focused readiness-guidance test and OpenSpec validation.

## Risks / Trade-offs

- [Existing installations may still expose the old skill until their ODK files are updated] → The source installation guide and current skill catalog will point only to the new skill; users must refresh existing installed ODK content to receive the rename.
- [A stale active reference could leave the new command undiscoverable or break guidance checks] → Search active project files for the old command and update all current entry points and tests; preserve old references only in archived history.

## Migration Plan

Update the repository's skill source, agent metadata, active guidance, installation references, tests, and capability specifications as one change. Existing installations are not changed automatically; they must receive the updated ODK files. Rollback consists of restoring the prior skill name and references; no data migration or compatibility alias is planned.
