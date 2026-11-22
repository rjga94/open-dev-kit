# Tasks

## 1. Release skill

- [x] 1.1 Create `.github/skills/odk-release/SKILL.md` with manual-only metadata and the existing release procedure; compare it with the existing procedure and release requirements to verify that versioning, analysis, publication, and failure safeguards are preserved.
- [x] 1.2 Remove the superseded release section from `CONTRIBUTING.md` and the automatic release instruction from `.github/copilot-instructions.md`, preserving unrelated content; verify no stale reference to the old procedure remains.
- [x] 1.3 Verify the skill is absent from ODK install and module catalogs and validate its name, location, and manual-only metadata against VS Code skill conventions.

## 2. Integration verification

- [x] 2.1 Walk through first and subsequent releases, breaking changes, target selection, conflicting tags, incomplete history, and partial publication without creating a tag or release; verify the skill retains the specified outcomes.
- [x] 2.2 Verify `/odk-release` discovery in a fresh VS Code Copilot chat without publishing, or report explicitly if the runtime is unavailable; confirm the skill is not auto-invoked by its metadata.
