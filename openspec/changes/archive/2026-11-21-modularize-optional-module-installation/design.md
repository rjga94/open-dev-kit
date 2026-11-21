# Design

## Context

See proposal.md for the motivation. Today `.opendevkit/agents/manifest.json` contains optional-module source and host-destination mappings, while core bootstrap deliberately omits optional-module functionality and Readiness handles later selection. The target project therefore needs lightweight setup metadata and a pinned source to support that later step.

## Goals / Non-Goals

**Goals:**
- Keep the initial bootstrap focused on core ODK while leaving enough module metadata for later setup.
- Let each module own its install mappings and any module-specific questions.
- Keep user communication, exact-plan approval, conflict handling, and config updates in the shared Readiness/orchestrator flow.
- Ensure all fetched files in a setup operation come from one resolved ODK commit.

**Non-Goals:**
- Move optional-module selection into the initial `INSTALL.md` interview.
- Install optional-module agents, skills, workflows, or runtime data during core bootstrap.
- Treat module installation as consent to seed, repair, or otherwise operate on module data.
- Update project files outside the ODK-managed install targets.

## Decisions

### Module-local install metadata with a central catalog

Keep a small central catalog for module discovery, but have each entry point to a module-owned machine-readable manifest and `install.md`. The module manifest is the single source of truth for source files, host adapters, and `installAs` destinations; `install.md` contains prerequisites, conditional questions, and post-install checks. Do not duplicate file mappings in the catalog or in prose.

The core bootstrap copies the catalog and lightweight module manifests/guides into `.opendevkit/` as setup metadata. It does not copy the optional functional assets. This makes later setup possible without exposing all optional workflows to the installed agent by default.

This intentionally revises the earlier decision in `group-module-source-files` to keep one central installation registry because Wiki was the only optional module. With module-specific setup guidance and pinned-source behavior, module-owned descriptors now provide a better ownership boundary; the central catalog remains the discovery entry point.

Alternative considered: keep every mapping in the central manifest and add module guides only. This avoids module-level manifests but leaves mapping ownership centralized and risks the two sources of setup behavior drifting as modules grow.

### Pin ODK source provenance at core bootstrap

Resolve the requested repository reference to a commit SHA during core bootstrap, then record the repository and SHA in the project-local ODK config. A branch or tag is a bootstrap input, not a future fetch target. After module selection, Readiness retrieves that module's source files from the recorded immutable commit while preparing the exact plan; retrieval is read-only, and target-project writes still wait for approval.

Alternative considered: resolve the default branch at each module installation. That would make the installed core guidance and fetched module assets come from potentially different revisions.

### Refresh legacy installations from the canonical latest commit

If an older installation lacks source provenance, Readiness resolves the latest commit on the canonical ODK repository's default branch. It includes all ODK-managed core files and the selected module assets from that same commit in one exact plan. The user approves that plan before any project writes; a declined plan leaves the installation unchanged and module setup pending.

Use the latest canonical commit rather than guessing an original fork or asking for a source on every legacy setup. This intentionally upgrades the whole ODK-managed installation as part of the user's optional-module setup request, including when the user selects no modules; in that case, install no optional functional assets. Do not update unrelated project files. If a required core-file conflict is not approved, do not apply the refresh or install module assets from the new revision. A selected module whose own conflict is declined remains unchanged and disabled; other safe, approved work may continue.

### Ask module questions before building one shared plan

After the user selects modules, Readiness loads only those modules' manifests and guides, then retrieves their declared source files from the resolved commit for review. It asks only unanswered module-specific questions that can affect their setup, then composes a single plan containing paths, proposed material, source commit, and any core refresh needed for a legacy install. Source retrieval is read-only. Module guidance can describe questions and checks but cannot authorize writes or override shared approval and conflict policies.

Alternative considered: ask each module to execute its own installer independently. This fragments consent and makes it harder to review the complete set of project changes.

### Keep module data operations separately consented

Selection authorizes preparing the module installation plan only. Wiki seed, repair, and other data operations retain their existing explicit opt-in and approval gates. The install guide may explain those later choices but must not perform them as an installation side effect.

### Validate the metadata without adding a test framework

The repository currently has no dedicated test runner or test suite. Add focused validation for catalog-to-module references, source existence, valid destinations, and duplicate/conflicting mappings using the repository's existing lightweight tooling or a small standard-library check; do not introduce a general plugin framework.

Alternative considered: rely only on manual review. That is insufficient once installation mapping is distributed across module-owned descriptors.

## Risks / Trade-offs

- **A pinned source may no longer be reachable** -> Report the exact repository/commit retrieval failure and leave the module uninstalled; do not fall back to a branch or newer commit.
- **Legacy refresh can change core ODK guidance while enabling a module** -> Include every ODK-managed target and its proposed content in the same plan, require approval, and stop the refresh if a required core conflict is not approved.
- **Module-local guides may imply broader permissions** -> Treat them as setup inputs only; the orchestrator retains user communication, consent, write, and scope boundaries.
- **A write can fail after part of an approved plan was applied** -> Preflight and stage planned content before writes; report the exact files changed and failures without claiming completion.

## Migration Plan

1. Update core bootstrap to install the lightweight module catalog/manifests/guides and record repository plus resolved commit SHA.
2. Update Readiness to use the recorded commit for new installations and to plan a full ODK-managed refresh from the canonical latest commit for legacy installations.
3. Move Wiki's install mapping and setup-specific guidance into its module-owned metadata; keep its functional assets selected and approved separately.
4. Validate source references, destination mappings, pinned-source behavior, conflict handling, and legacy refresh plans.

If a new installation plan is declined, keep existing files and config unchanged. If a legacy refresh plan is declined, leave the old core installation as-is and keep optional setup pending.
