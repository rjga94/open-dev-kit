# Wiki Query

Answer questions using only `.opendevkit/wiki/`. This operation is read-only and does not search the current project, Git history, or external sources.

## Preconditions and search

1. If `.opendevkit/wiki/` does not exist, report that the Wiki is not initialized and direct ODK to offer `/odk-wiki-seed`. Do not create files.
2. Search only Markdown content under `.opendevkit/wiki/`, including its root index and pages.
3. Use page contents and links as the only evidence for the answer. Do not inspect other project paths even if the answer appears to be readily available there.
4. If the Wiki does not contain enough information, say that the Wiki does not answer the question. Identify the missing information or point ODK to request an explicit capture or seed; do not fill the gap from repository files or other sources.

## Report

Return the answer and supporting Wiki page paths to ODK. Distinguish documented intent, implemented behavior, and external context when the Wiki itself makes that distinction. Report uncertainty or conflicting Wiki claims without resolving them through an outside search.
