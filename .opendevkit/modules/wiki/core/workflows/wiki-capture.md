# Wiki Capture

Use this workflow only when the user explicitly invokes `/odk-wiki-capture` or a successful Archive is authorized by the project's explicit post-Archive opt-in. The orchestrator delegates the complete operation to one Wiki specialist and communicates with the user on its behalf.

## Scope and preconditions

- Capture only the topic the user identified, or the directly relevant durable knowledge in an opted-in archived change.
- Require an existing `.opendevkit/wiki/` bundle. If it is missing, report that capture cannot initialize it and direct ODK to offer `/odk-wiki-seed`.
- Read only project sources directly relevant to the identified topic. Do not perform a broad repository or Git-history scan.
- Retrieve a linked external page or asset only when it is directly relevant and needed to ground the requested knowledge. When its contents inform captured claims, record its exact absolute URL in the concept's canonical `sources[].resource` entries along with the relevant project sources. Do not imply an external page was consulted unless it was actually retrieved.
- Exclude secrets and credentials from model context and Wiki output.
- Write only inside `.opendevkit/wiki/`.

## Research and reconciliation

1. Establish the topic and relevant project sources before researching. If the requested topic is ambiguous, ask ODK to obtain clarification.
2. Treat explicit user decisions as evidence of project intent, current code and configuration as evidence of implemented behavior, and external sources as context. Preserve these distinctions when they disagree.
3. Review every page in the Wiki and its relationships before changing anything. Check organization, duplicate or conflicting knowledge, broken references, index consistency, provenance, and OKF conformance using `.opendevkit/modules/wiki/core/standards/wiki-okf-v0.2.md`.
4. Reconcile the new knowledge with the existing bundle. Replace or remove obsolete claims when current authoritative evidence supersedes them; do not retain archive copies in the Wiki.
5. If safely needed, create, move, rename, merge, split, or delete pages and adjust taxonomy according to `.opendevkit/modules/wiki/core/standards/wiki-taxonomy.md`. Preserve unique knowledge and provenance, and repair affected links and indexes.
6. Leave pages unchanged when their content, structure, provenance, links, and format do not need maintenance. Do not rewrite, re-title, re-describe, reformat, or otherwise touch an unaffected page for stylistic consistency; update only navigation affected by actual page changes.
7. If materially conflicting information cannot be reconciled without risking loss of unique knowledge or provenance, preserve it and ask ODK to obtain clarification. Do not guess or delete it.

## Complete and report

After integrating the requested knowledge, validate the entire bundle and the affected links and indexes using `.opendevkit/modules/wiki/core/standards/wiki-okf-v0.2.md`. Report to ODK:

- The captured topic and sources used, including provenance.
- The distinction between user intent, implemented behavior, and external context when they differ.
- Created, changed, moved, merged, split, or deleted pages and taxonomy changes.
- Checks run and their outcomes, plus any unresolved conflict or incomplete maintenance.

Do not claim the capture succeeded if the Wiki was not fully reviewed or an error left the operation incomplete.
