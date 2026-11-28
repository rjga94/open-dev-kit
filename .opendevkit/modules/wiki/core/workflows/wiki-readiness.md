# Wiki readiness

Run this workflow only when the Wiki module is enabled and core readiness has
dispatched its manifest-declared readiness workflow. Return findings and
unresolved choices to ODK; do not communicate with the user directly. ODK
obtains every user choice and approval. A readiness check is read-only.

## Read-only health check

Ask the Wiki specialist to check whether `.opendevkit/wiki/` exists and, when
it does, inspect it without changing files. Report findings for canonical OKF
format, source provenance, references, index, taxonomy, and consistency. Do
not scan the repository or Git history as part of this health check.

If the Wiki is missing, ODK asks exactly:

> Would you like to seed a Wiki by scanning this repository and its Git history?

Offer “Yes” and “No”. “Yes” authorizes the seed scan only; it does not approve
any Wiki content or writes. On “No”, leave the Wiki absent.

If the existing Wiki has integrity issues, ODK asks exactly:

> How should I handle the Wiki issues?

Offer “Repair,” “Reseed from repository/history,” and “Leave unchanged”.
“Leave unchanged” ends Wiki data work without changes. “Repair” authorizes
preparing a repair proposal, not writing; repair must not perform a broad
repository or Git-history scan. “Reseed from repository/history” is the
separate explicit opt-in to a seed scan.

## Prepare and approve data changes

For an explicitly opted-in missing-Wiki seed or reseed, follow
`.opendevkit/modules/wiki/core/workflows/wiki-seed.md`, including its
pre-context screening and provenance requirements. A scan opt-in authorizes
screened source inspection and proposal preparation only. For repair, review
the whole Wiki and prepare only needed repairs without a broad repository or
Git-history scan.

Return the findings and a complete proposed file-change preview to ODK. ODK
must present the preview and ask exactly:

> Do you approve these proposed Wiki changes?

Offer “Approve” and “Decline”. This is a separate explicit approval required
before any Wiki write. The seed/reseed choice is not approval of proposed
changes, and plan approval does not authorize unrelated Wiki operations. If
approval is declined, leave the Wiki unchanged. Apply only approved changes under
`.opendevkit/wiki/`, and report incomplete checks, changes, and outcomes.

## Post-Archive capture preference

Offer the one-time preference only when OpenSpec is configured, the Wiki is
initialized, and `.opendevkit/config.json` has
`preferences.postArchiveWikiCapture` exactly `"not-offered"`. ODK asks exactly:

> Enable automatic Wiki capture after OpenSpec Archive?

Offer “Enable” and “Leave disabled”. After an explicit answer, record
`"enabled"` or `"declined"` respectively in
`preferences.postArchiveWikiCapture`, preserving all other configuration.
Do not offer the choice when any gate is unmet or the preference has any other
value; do not seed a missing Wiki to enable it. Recording `"enabled"` only
opts in. Automatic capture runs only after a successful OpenSpec Archive when
the Wiki module remains enabled, `.opendevkit/wiki/` is initialized, and the
stored preference is `"enabled"`; the Archive capture follows the existing
Wiki capture workflow.
