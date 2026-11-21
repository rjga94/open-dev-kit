# Tasks

## 1. Rename the readiness command

- [x] 1.1 Move the skill to `.github/skills/odk-readiness-check/SKILL.md`; update its frontmatter name, ODK agent profile, and manifest command/skill/source references. Verify VS Code discovery metadata points only to the new skill path and command.
- [x] 1.2 Update the active Readiness, orchestrator, canonical workflow, and installation guidance to name `/odk-readiness-check`, preserving the workflow behavior and canonical workflow file path. Verify active source and documentation references no longer expose `/odk-readiness-refactor`.
- [x] 1.3 Update `test_readiness_module_guidance.py` for the new skill path and command metadata, including a check that the old name is not retained as an alias; verify with `python3 -m unittest discover -s tests -p 'test_readiness_module_guidance.py'`.

## 2. Validate the change contract

- [x] 2.1 Validate the proposal, delta specs, design, and tasks with `openspec validate rename-readiness-refactor-skill --strict`; resolve any reported errors or warnings.
