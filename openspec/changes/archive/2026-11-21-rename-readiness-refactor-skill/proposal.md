# Proposal

## Why

The name `/odk-readiness-refactor` understates the workflow's broader project-readiness assessment and can suggest a narrower or automatic refactor. Renaming it to `/odk-readiness-check` makes its entry point clearer while preserving its existing assessment, setup, clarification, approval, and documentation-update behavior.

## What Changes

- Replace the user-invokable skill name `/odk-readiness-refactor` with `/odk-readiness-check`; do not retain the old name as a compatibility alias.
- Update the skill metadata, ODK command and skill catalog, orchestrator guidance, installation references, and relevant tests/specs to use the new name.
- Keep the readiness workflow's behavior and canonical workflow content unchanged apart from references needed to identify the new command.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `project-readiness`: Change the user-invokable readiness command name while retaining the existing readiness workflow behavior.
- `dev-kit-bootstrap`: Update bootstrap and command-routing requirements to use the renamed command.

## Impact

Affected project-owned skill and agent metadata, the ODK agent entry point and canonical workflow references, installation documentation, readiness guidance tests, and the two existing OpenSpec capability specs. No dependencies or implementation APIs change; the old slash command is intentionally not preserved.
