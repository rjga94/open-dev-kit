# Design

## Context

See the proposal for motivation. The current release procedure is in
`CONTRIBUTING.md`, with automatic routing in `.github/copilot-instructions.md`.
ODK's install guide selects explicit core files and module metadata rather than
all repository skills.

## Goals / Non-Goals

**Goals:**

- Offer an explicit VS Code Copilot slash command for maintainers.
- Preserve the existing release process without introducing another copy.

**Non-Goals:**

- Install the release skill into projects using ODK.
- Change the alpha version policy, release safeguards, or publish a release.
- Add package dependencies or automated release infrastructure.

## Decisions

1. Put the procedure in `.github/skills/odk-release/SKILL.md`, named
   `odk-release`. This is a project skill location already used in this
   repository. Set `disable-model-invocation: true` and leave it
   user-invocable, so VS Code Copilot offers `/odk-release` without loading
   it automatically. Other hosts may implement skill metadata differently.
2. Move the release procedure into the skill and remove the old contributor
   section and its automatic instruction. Preserve unrelated content if those
   files change before implementation. Keeping only one authoritative copy
   avoids policy drift.
3. Keep the skill out of the ODK install manifest and module catalogs. Verify
   the installation guidance does not include it, rather than assuming every
   skill under `.github/skills/` is installed.
4. An explicit skill invocation authorizes the release workflow, subject to
   applicable tool approvals. Retain the current commit default, optional
   explicit target, complete history analysis, alpha policy, pre-release flag,
   immutable tags, verification, and partial-failure reporting. If publication
   tools or permissions are unavailable, report the blocker instead of
   claiming success or silently changing the workflow.

## Risks / Trade-offs

- [Some hosts may ignore the manual-only metadata] -> Scope the automatic
  invocation guarantee to VS Code Copilot and verify discovery in a fresh chat.
- [Moving the procedure drops safeguards] -> Compare the skill against the
  existing procedure and unchanged release requirements before removing it.
- [A skill-discovery test could publish] -> Validate the workflow with
  non-publishing scenarios; do not invoke a real release during implementation.

## Migration Plan

Add and validate the skill while removing the superseded guidance. Existing
published releases are unaffected. A repository change can restore the old
guidance if this approach is reverted.
