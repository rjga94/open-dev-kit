# ODK Wiki format: canonical OKF v0.2

The Wiki is one OKF v0.2 bundle rooted at `.opendevkit/wiki/`. Follow the canonical specification at <https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md>. Do not make non-standard fields part of the required format profile.

## Concept documents

Every Markdown document other than reserved `index.md` and `log.md` files is a concept document. Each concept must have a parseable YAML frontmatter block with a non-empty string `type`.

Canonical `title` and `description` are optional. `summary` is not a canonical v0.2 field; do not require it or substitute it for `description`. Additional producer-defined fields are allowed by OKF, but are extensions, not canonical fields. Preserve unknown fields when maintaining existing content; do not require them for conformance.

## Provenance

Captured project knowledge must retain its sources in the `sources` frontmatter field. Each source entry must be a mapping with a non-empty canonical `resource` value. Use an absolute URL for an external source or an appropriate bundle-relative path or scope descriptor for other sources, as allowed by OKF v0.2.

Do not require `kind`, `uri`, `revision`, `locator`, or `retrieved_at`; these are not canonical v0.2 source-entry fields. Do not invent values. Additional source metadata may be preserved as producer-defined extensions when already present, but it does not replace `resource`.

## Reserved documents

- `index.md` is navigation, not a concept. Its body uses headings and link bullets for directory entries. A bundle-root `index.md` may have frontmatter only to declare `okf_version: "0.2"`; do not add concept metadata to it.
- `log.md` is reserved for date-grouped update history. If present, use ISO 8601 `YYYY-MM-DD` headings.
- Reserved filenames are not required to exist. Broken links and unknown extension fields do not by themselves make a bundle non-conformant.

## Validation and version declaration

Before declaring a bundle conformant:

1. Enumerate every `.md` file under the bundle, excluding only reserved `index.md` and `log.md` files from the concept-document checks.
2. For every concept, verify a frontmatter delimiter pair, parseable YAML, and a non-empty string `type`.
3. For each `sources` entry that is present, verify it is a mapping with a non-empty `resource`. Captured knowledge must retain its source entries; do not claim a sourced capture if provenance is missing.
4. Verify each reserved `index.md` and `log.md` follows its reserved structure. When present, root-index frontmatter contains only `okf_version: "0.2"`.
5. Declare `okf_version: "0.2"` in the root index only after every concept and present reserved document passes these checks. If any check fails or could not be completed, omit the version declaration and report the incomplete validation.

An empty bundle or one with non-conforming concepts must not claim v0.2 conformance. Do not infer validation success from file extensions or from the presence of the root index alone.
