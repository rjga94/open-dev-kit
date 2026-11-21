# Design

## Context

See `proposal.md` for the motivation and intended scope. The Wiki module currently groups files under `agents/`, `skills/`, and `workflows/`; the specialist prompt includes both Wiki-domain rules and GitHub Copilot/ODK execution details. The central `.opendevkit/agents/manifest.json` maps module sources to GitHub Copilot installation destinations. The existing `project-wiki` capability describes runtime behavior, which this source refactor is intended to preserve.

## Goals / Non-Goals

**Goals:**

- Make the boundary between reusable Wiki behavior and host-specific integration visible in the directory structure.
- Keep GitHub Copilot as the only implemented adapter while making the registry capable of describing adapter-owned artifacts separately from shared core sources.
- Preserve the current command entrypoints, install destinations, specialist ownership, and Wiki data path.

**Non-Goals:**

- Implement or claim support for another assistant, IDE, or command-line host.
- Change Wiki capture, query, seed, readiness, or post-Archive behavior.
- Move the project-owned `.opendevkit/wiki/` data bundle or create a separate manifest/discovery mechanism per module.
- Reorganize shared ODK agents or workflows outside the Wiki module except to update references to moved Wiki sources.

## Decisions

### Separate shared Wiki guidance from host adapters

Use the following module layout:

```text
.opendevkit/modules/wiki/
  core/
    specialist.md
    workflows/
      wiki-module.md
      wiki-capture.md
      wiki-query.md
      wiki-seed.md
    standards/
      wiki-okf-v0.2.md
      wiki-taxonomy.md
  adapters/
    github-copilot/
      agent.md
      skills/
        odk-wiki-capture/SKILL.md
        odk-wiki-query/SKILL.md
        odk-wiki-seed/SKILL.md
```

`core/` owns Wiki-domain scope, evidence handling, approval rules, workflow outcomes, and format/taxonomy requirements. It must not depend on VS Code-specific frontmatter, skill syntax, tool names, or installation paths. `adapters/github-copilot/` owns the Copilot agent profile and command/skill surfaces, including their ODK handoff and tool bindings. The adapter points to or packages the shared core according to the host's supported mechanism; do not duplicate core policy in adapter prompts.

Host-specific execution mechanics belong in the adapter. Shared workflows should describe required outcomes and safety constraints without making a particular host's tool API part of the domain contract.

### Keep the central registry and represent adapter mappings explicitly

Retain `.opendevkit/agents/manifest.json` as the single module/install registry, consistent with the existing source-layout decision. Reshape the Wiki entry to distinguish shared core sources from an `adapters.github-copilot` entry that owns its source files and existing `installAs` destinations. Keep user-facing command identifiers with the adapter that exposes them rather than treating a Copilot skill format as a core Wiki capability.

Do not add another platform entry in this change. A future adapter can be added as a sibling registry entry and directory without moving or copying Wiki workflows.

### Preserve the installed contract and runtime data boundary

Keep the existing `.github/agents/odk-wiki.agent.md` and `.github/skills/odk-wiki-{capture,query,seed}/SKILL.md` destinations, command names, hidden-specialist routing, and `.opendevkit/wiki/` data location. Update module, orchestrator, readiness, install, and skill references when their source paths move. The central manifest remains authoritative for source-to-destination mappings.

## Risks / Trade-offs

- **A moved source leaves a stale path and breaks setup or delegation** -> Update all manifest and live guidance references together; validate that every declared source exists and search for old paths.
- **Host-specific details leak into shared core guidance** -> Keep tool names, profile metadata, skill syntax, and install destinations under `adapters/github-copilot/`; review core references for host-specific assumptions.
- **The layout could be mistaken for support of multiple hosts** -> Keep only the GitHub Copilot adapter and state explicitly that additional platform support requires a separately designed and validated adapter.
- **The central registry grows more adapter-aware** -> Keep it as one registry for now; avoid a discovery or plugin-loading mechanism until an actual second adapter establishes its requirements.

## Migration Plan

1. Move the current Wiki specialist rules, workflows, and standards into the `core/` layout; separate host-specific execution instructions into the GitHub Copilot adapter.
2. Move the Copilot agent profile and skill shims into `adapters/github-copilot/`.
3. Update the Wiki entry in the central manifest and every live source reference, retaining all `installAs` values.
4. Verify manifest parsing, source existence, installation destinations, resolved references, and absence of stale old paths. Run relevant repository-defined validation, including OpenSpec validation.
5. Roll back by restoring the old module source paths and references. No runtime Wiki data migration is needed because `.opendevkit/wiki/` and installed destinations remain unchanged.
