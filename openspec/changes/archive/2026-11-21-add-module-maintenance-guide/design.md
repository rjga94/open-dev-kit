# Design

## Context

See `proposal.md` for the motivation. The repository currently has `INSTALL.md` for consumers but no contributor guide. Module definitions live under `.opendevkit/modules/`, and the central manifest maps selected sources to project install destinations.

## Goals / Non-Goals

**Goals:**

- Keep module authoring guidance discoverable to ODK contributors.
- Keep that guidance separate from files and documentation intended for projects consuming ODK.

**Non-Goals:**

- Change the install process, manifest schema, module behavior, or project-facing guidance.
- Add an automated generator or module-validation framework.

## Decisions

### Put the guidance in a root-level `CONTRIBUTING.md`

Use the repository root because the document describes how contributors evolve the ODK source tree, not how projects install or use ODK. Do not put it under `.opendevkit/` or a module directory: those trees hold canonical kit/module sources and could be mistaken for consumable assets. `INSTALL.md` remains focused on consumer installation.

### Keep the checklist procedural and tied to current conventions

Describe the existing `core/` and adapter separation, central manifest source and `installAs` roles, and the difference between module sources and project runtime data. Include checks contributors can perform with current repository tools; do not introduce a new schema or claim that an adapter is supported before it is implemented and validated.

### Update capability specs only for behavior changes

This contributor document does not alter ODK runtime behavior or project-facing contracts, so no capability delta is appropriate. Changes to a module's observable behavior remain subject to the relevant capability specification.

## Risks / Trade-offs

- **Internal guidance is accidentally treated as installable project content** -> Keep it at the repository root and verify it is absent from the module manifest, install sources, and project-facing references.
- **The checklist becomes stale as module conventions evolve** -> Keep it concise, cite canonical source locations, and update it when the module layout or manifest contract changes.

## Migration Plan

Add the contributor document without changing installation assets or project files. Rollback is removal of the single root-level contributor document; no runtime migration is required.
