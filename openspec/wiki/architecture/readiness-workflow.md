---
type: architecture
title: Readiness workflow
description: Readiness assesses current project evidence and prepares approved guidance or documentation changes.
sources:
  - resource: "project:.opendevkit/agents/readiness.md"
  - resource: "project:.opendevkit/workflows/readiness-refactor.md"
  - resource: "project:openspec/specs/project-readiness/spec.md"
---

# Readiness workflow

The `/odk-readiness-refactor` command enters through ODK and delegates
assessment to the core Readiness specialist. The assessment uses relevant
current guidance, documentation, configuration, tests, and source code;
Git history is secondary evidence. It excludes secrets and credentials from
model context.

Readiness classifies relevant topics as clear/current, partial or ambiguous,
missing, stale, or contradictory, then asks only about unresolved gaps. It
prepares one consolidated preview of changes to AI guidance or project
documentation and waits for user approval. It does not modify implementation
code.

When the optional Wiki module is enabled, Readiness delegates a read-only Wiki
integrity check. Seeding or repair requires a separate user choice and
approval.
