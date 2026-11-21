# Proposal

## Why

Optional-module file mappings and setup behavior are currently coordinated from shared ODK guidance and a central manifest. As modules grow, module-specific questions and setup checks should live with the module without weakening the shared readiness flow's approval, conflict, and configuration safeguards.

## What Changes

- Keep initial `INSTALL.md` installation core-only; continue handling optional-module setup through `/odk-readiness-refactor`.
- Give each optional module an authoritative machine-readable manifest for its installable sources and host-specific destinations, with a central catalog that points to module manifests rather than duplicating their mappings.
- Include lightweight module manifests and installation guidance with core ODK so Readiness can consult them later; install module agents, skills, workflows, and other functional assets only when selected and approved.
- Record the ODK source repository and exact commit used for core installation; Readiness fetches selected module assets only from that same commit.
- For legacy installations without source provenance, resolve the latest commit from the canonical ODK repository and include refreshing all ODK-managed core files and selected module assets from that same commit in one approved plan.
- Add module-owned installation guidance for prerequisites, conditional module-specific questions, and post-install checks.
- Have Readiness consult only selected modules' manifests and installation guidance, gather needed answers before preparing one consolidated exact plan, and retain ownership of user communication, approval, conflict handling, and configuration updates.
- Keep module operations that need separate consent, such as Wiki seeding, outside the authorization to install the module itself.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `dev-kit-bootstrap`: Preserve the core-only initial bootstrap boundary while defining modular source and destination declarations for optional modules.
- `project-readiness`: Use selected modules' own setup guidance and manifests when preparing approved optional-module installation plans.

## Impact

Potentially affected areas include `.opendevkit/agents/manifest.json`, lightweight module setup metadata and ODK source provenance included with core ODK, optional module source trees, `.opendevkit/agents/readiness.md`, `.opendevkit/agents/orchestrator.md`, readiness workflow guidance, ODK-managed core files refreshed for legacy installations, and focused manifest/reference and installation validation. Module functionality and module data operations remain separately selected and consented.
