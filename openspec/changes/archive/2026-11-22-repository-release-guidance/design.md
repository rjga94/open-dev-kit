# Design

## Context

See the proposal for motivation and the release capability spec for the
behavior contract. ODK is installed from GitHub at a resolved commit, while
repository contributor guidance is not installed into consumer projects.
The current local checkout has no tags; this does not establish whether the
remote repository has releases or tags.

## Goals / Non-Goals

**Goals:**

- Make a plain-language Copilot chat request discover the release procedure.
- Keep version selection, publication, and recovery understandable without
  introducing release tooling or dependencies.

**Non-Goals:**

- Automatically release on push, publish packages, or upgrade installations.
- Decide when ODK graduates from alpha.

## Decisions

1. Put a concise repository-wide trigger and pointer in
   `.github/copilot-instructions.md`, with the detailed procedure in
   `CONTRIBUTING.md`. This lets VS Code Copilot discover the procedure while
   keeping maintainer instructions out of installed ODK assets. Duplicating
   the full procedure in multiple places risks drift.
2. Resolve the requested target to an exact commit and inspect remote version
   tags and GitHub Releases as well as local history. Use the previous
   applicable version as the baseline only when the release history and
   ancestry are unambiguous. Stop and explain when the baseline, target,
   access, or complete history cannot be verified; do not treat an unavailable
   remote or incomplete checkout as an empty release history.
3. Use SemVer `0.y.z` and increment the minor for every alpha release, as
   selected by the maintainer. SemVer allows initial-development versions but
   does not require this increment scheme. Analyze commit bodies and relevant
   diffs rather than relying solely on commit subject prefixes; summarize
   features, fixes, and breaking changes. For the first release, review the
   available history through the target.
4. Publish an annotated `v`-prefixed tag and a GitHub Release flagged as a
   pre-release. Verify the remote tag resolves to the requested commit and
   the release has the intended tag and flag. A direct release request
   authorizes the release workflow, but ambiguous choices or conflicts require
   clarification before publishing.
5. Never move or replace a published tag. If publication only partly succeeds,
   report the exact state and offer a safe continuation instead of silently
   overwriting or deleting anything.

## Risks / Trade-offs

- [Commit descriptions omit behavior] -> Inspect relevant diffs and identify
  uncertainty rather than inventing release notes.
- [Remote and local histories disagree] -> Verify remote state and ancestry;
  stop for clarification instead of choosing a potentially wrong baseline.
- [Tag push succeeds but release creation fails] -> Report the existing tag
  and failure so the maintainer can decide how to resume.
- [A GitHub pre-release may not be shown as the latest stable release] ->
  Explicitly describe this consequence in maintainer guidance.

## Migration Plan

Add the guidance without publishing a version. When the maintainer later
requests a release, assess the live remote state before applying the initial
version rule. Roll back the guidance through an ordinary repository change;
published versions remain immutable.
