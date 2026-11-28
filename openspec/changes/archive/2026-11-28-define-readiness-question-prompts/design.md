# Design

## Context

The core workflow currently contains both general readiness behavior and Wiki-specific health/data questions. Modules already own their install guides, manifests, workflows, and specialist responsibilities. ODK remains the sole user-facing agent; specialists return findings and clarification needs to it.

## Goals / Non-Goals

**Goals:**
- Keep core readiness generic and dispatch enabled modules through a manifest-declared readiness workflow.
- Ask a module's install questions immediately after the user opts into it, then run its module-owned readiness only after successful enablement.
- Move Wiki health and data-operation prompts into Wiki-owned readiness guidance.
- Preserve concise closed choices, source provenance, and explicit approval boundaries.

**Non-Goals:**
- Change core readiness assessment topics or make module selection imply installation approval.
- Run a module readiness workflow for an unselected or incompletely installed module.
- Let module workflows communicate with users directly or bypass ODK approvals.

## Decisions

### Keep core readiness as the generic dispatcher

Keep baseline project assessment, sequential module selection, common plan approvals, and dispatch in `.opendevkit/workflows/readiness-refactor.md`. Each optional module may declare a readiness-workflow file ID in its manifest, pointing to a module-owned workflow file. The core workflow discovers and invokes only declared workflows for enabled modules; it does not contain module-specific questions or checks.

**Alternative considered:** Put module paths or behavior branches in the core workflow or central catalog. Rejected because this duplicates module ownership and requires core edits whenever a module adds readiness behavior.

### Separate installation questions from post-enable readiness

For pending setup, ask each catalog module “Would you like to enable the `<module>` module?” with “Yes” and “No” choices. After “Yes,” consult that module's install guide and resolve its unanswered installation decisions before prompting for another module. A “No” skips its setup inputs; all “No” answers remain a valid empty selection.

Run the selected module's readiness workflow only after its installation plan is approved and it is successfully enabled. Also run it for already-enabled modules. This lets module specialists perform their own health checks and return module-specific choices through ODK. Modules without a declared workflow need no special-case core logic.

**Alternative considered:** Run module health/data checks immediately after selection but before installation. Rejected because the module may not yet be installed or its specialist available, and a module-selection answer must not authorize data operations.

### Move Wiki readiness into the Wiki module

The Wiki module's readiness workflow owns its read-only presence/integrity check, missing-Wiki seed choice, repair/reseed choices, and one-time post-Archive capture opt-in. The Wiki install guide remains authoritative for installation questions; it currently specifies that no Wiki-specific installation answer is needed. Seed, repair, and reseed remain separate user-authorized data operations with their own proposed-change approval.

**Alternative considered:** Leave Wiki health and data-operation prompts in the core workflow. Rejected because those behaviors are specific to one optional module.

### Keep user communication and approvals centralized

Module readiness workflows return findings and unanswered choices to ODK; they do not address the user or write files. ODK retains the existing boundaries: module selection is not installation approval, a Wiki seed opt-in is not approval of the resulting file changes, and plan/conflict/documentation approvals remain separate.

### Validate discovery and dispatch with focused tests

Extend module-manifest validation to check any declared readiness-workflow reference, and extend readiness tests to verify per-module sequencing, dispatch only after successful enablement, no dispatch for unselected modules, and preservation of approval boundaries.

## Risks / Trade-offs

- **A manifest may point to a missing or invalid readiness workflow** → Validate the optional reference and target as part of the existing module-manifest checks.
- **Core and module workflows could duplicate or disagree on a question** → Keep module-specific questions in the module workflow and retain only generic dispatch and approval rules in core.
- **An enabled module may have no readiness workflow** → Treat the hook as optional and skip module-specific checks when it is absent.

## Migration Plan

Add the optional manifest readiness reference and Wiki-owned readiness workflow, then update the core dispatcher, relevant specs, and focused validators/tests. Existing module selections and `.opendevkit/config.json` settings do not require migration. Preserve explicit opt-in and approval behavior for Wiki data operations.
