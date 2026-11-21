# Tasks

## 1. Module-owned setup metadata

- [x] 1.1 Define the module-manifest shape and central catalog references, and add focused standard-library validation for referenced manifests, source paths, valid install destinations, and duplicate targets; verify the validator catches invalid references and passes on the current catalog.
- [x] 1.2 Add the Wiki module manifest and `install.md`, move its source/destination mappings out of the central catalog, and document the ownership convention in `CONTRIBUTING.md`; verify all Wiki source and destination references with the validator.

## 2. Core bootstrap provenance and metadata

- [x] 2.1 Update core bootstrap to include the catalog and lightweight module manifests/guides, resolve the requested ODK source to a commit SHA, and record repository plus SHA in project config while preserving existing fields; verify branch/tag inputs record the resolved SHA and config merges preserve unrelated settings.
- [x] 2.2 Update `INSTALL.md` to explain that setup metadata ships with core while optional functional assets and module data do not; verify a core-only install contains no optional agents, skills, workflows, or Wiki bundle.

## 3. Readiness-driven module installation

- [x] 3.1 Update Readiness to consult only selected modules' manifests and guides, ask only unanswered module-specific questions, and include answers in one consolidated plan; verify selected, unselected, and no-extra-question paths.
- [x] 3.2 Fetch selected module sources from the recorded repository commit as read-only plan inputs, and show exact target paths and proposed contents before writes; verify fetched files match the recorded SHA and declining the plan writes nothing.
- [x] 3.3 Implement the legacy path by resolving the canonical ODK repository's latest commit and planning all ODK-managed core refreshes plus selected module assets from that same SHA, even for an empty selection; verify one SHA is used and a declined plan or unapproved required core conflict leaves files unchanged.
- [x] 3.4 Apply only approved core and module changes, retain per-path conflict approval and module-atomic skips, and update enabled-module/setup state only for completed installation; verify replacement declines leave affected module files unchanged and setup pending.

## 4. Integration verification

- [x] 4.1 Run the manifest validator, focused clean-install/pinned-module/legacy-refresh/conflict checks, and `openspec validate`; verify unselected modules remain uninstalled and no Wiki data operation runs as an installation side effect.
