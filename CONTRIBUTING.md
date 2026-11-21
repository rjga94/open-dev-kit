# Contributing to ODK

## Module maintenance

ODK modules separate shared behavior from host-specific integration. Put host-independent guidance and workflows in a module's `core/`; put host-specific agent/profile and command or skill packaging in `adapters/<host>/`. For example, Wiki's shared specialist, workflows, and standards are under `.opendevkit/modules/wiki/core/`, while its GitHub Copilot agent and skills are under `.opendevkit/modules/wiki/adapters/github-copilot/`.

Treat files in the module source tree as canonical. `.opendevkit/agents/manifest.json` points to those sources and uses `installAs` to name their project destinations. For example, the GitHub Copilot agent profile template at `.opendevkit/modules/wiki/adapters/github-copilot/agent.md` is installed as `.github/agents/odk-wiki.agent.md`; skill sources under the adapter are similarly mapped to `.github/skills/...`. The Wiki specialist source remains shared in `core/`. Maintain the sources and manifest mappings; do not treat installed copies as the source of truth.

Keep project runtime data (for example, data created when a module is used in a consuming project) separate from ODK's module definitions, workflows, and adapter assets. Only claim support for host adapters that actually exist and have been validated; do not imply support for hosts without an adapter.

Before completing a module change:

- Check references in canonical sources for accuracy and confirm referenced files and paths exist.
- Parse `.opendevkit/agents/manifest.json` as JSON and verify every declared source and template exists.
- Check that each adapter's declared commands map to its skills, and that source-to-`installAs` destinations match the intended install layout.
- Update relevant OpenSpec behavior contracts when observable module behavior changes; source-organization-only changes do not require a capability change.
- Run focused validation for the changed module and affected adapter (such as manifest/reference checks and relevant tests or install checks), then check the diff for whitespace errors.

This guidance is for maintaining ODK in this repository only. It is not installed into projects that use ODK.
