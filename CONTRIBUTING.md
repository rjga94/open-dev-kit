# Contributing to ODK

## Module maintenance

ODK modules separate shared behavior from host-specific integration. Put host-independent guidance and workflows in a module's `core/`; put host-specific agent/profile and command or skill packaging in `adapters/<host>/`. For example, Wiki's shared specialist, workflows, and standards are under `.opendevkit/modules/wiki/core/`, while its GitHub Copilot agent and skills are under `.opendevkit/modules/wiki/adapters/github-copilot/`.

Treat files in the module source tree as canonical. `.opendevkit/agents/manifest.json` is the central discovery catalog: each optional-module entry points to that module's `manifest.json` and `install.md`. A module manifest uses `schemaVersion: 1`, an `id` matching its catalog key, and a `files` array of unique `{id, source, installAs, host}` records (`host` is `core` or a declared adapter). Adapter agent and skill metadata refer to those file IDs rather than repeating paths; each declared source and destination appears in one mapping only. The module-owned manifest alone declares installable sources and their `installAs` destinations, including host-adapter mappings; do not duplicate file mappings in the central catalog or prose. For example, Wiki owns the mapping from its GitHub Copilot profile template to `.github/agents/odk-wiki.agent.md` and its skill destinations in `.opendevkit/modules/wiki/manifest.json`. Maintain the sources and module manifest; do not treat installed copies as the source of truth.

Keep project runtime data (for example, data created when a module is used in a consuming project) separate from ODK's module definitions, workflows, and adapter assets. Only claim support for host adapters that actually exist and have been validated; do not imply support for hosts without an adapter.

Before completing a module change:

- Check references in canonical sources for accuracy and confirm referenced files and paths exist.
- Parse `.opendevkit/agents/manifest.json` as JSON and verify every declared source and template exists.
- Check that each adapter's declared commands map to its skills, and that source-to-`installAs` destinations match the intended install layout.
- Run `python3 scripts/validate_module_manifests.py` and `python3 -m unittest discover -s tests -p 'test_module_manifest_validator.py'` to validate module references, source paths, safe destinations, and duplicate targets.
- Update relevant OpenSpec behavior contracts when observable module behavior changes; source-organization-only changes do not require a capability change.
- Run focused validation for the changed module and affected adapter (such as manifest/reference checks and relevant tests or install checks), then check the diff for whitespace errors.

This guidance is for maintaining ODK in this repository only. It is not installed into projects that use ODK.
