# project-wiki Specification

## Purpose

This capability gives a project a local knowledge base that users can explicitly maintain and query alongside the current repository.

## Requirements

### Requirement: Wiki operations belong to the internal Wiki specialist
The orchestrator SHALL delegate Wiki commands and readiness-requested Wiki checks to the internal Wiki specialist, which SHALL return findings, outcomes, source evidence, structural changes, and clarification needs to the orchestrator.

#### Scenario: Wiki command is delegated
- **WHEN** the orchestrator receives an enabled Wiki command
- **THEN** it delegates the Wiki operation to the Wiki specialist and communicates with the user on the specialist's behalf

#### Scenario: Wiki specialist completes an operation
- **WHEN** the Wiki specialist completes capture, query, or seed work
- **THEN** it returns the result and relevant evidence or changes to the orchestrator

### Requirement: Readiness Wiki integrity checks are read-only
When readiness requests a Wiki integrity check, the Wiki specialist SHALL inspect the bundle and report findings without changing Wiki content.

#### Scenario: Readiness checks an existing Wiki
- **WHEN** the readiness workflow requests an integrity check for an existing Wiki
- **THEN** the specialist checks format, provenance, references, index, taxonomy, and consistency, and returns findings without writing

### Requirement: Readiness Wiki repair requires approval
When the user chooses Wiki repair during readiness, the Wiki specialist SHALL prepare and apply only the approved whole-Wiki maintenance changes without performing a broad repository or Git-history scan.

#### Scenario: User approves a repair plan
- **WHEN** the user approves the proposed Wiki repair changes
- **THEN** the specialist applies the approved repairs and reports structural changes to the orchestrator

#### Scenario: User declines a repair plan
- **WHEN** the user declines the proposed Wiki repair changes
- **THEN** the Wiki remains unchanged

### Requirement: One Wiki specialist owns each Wiki-changing operation
Each capture, seed, readiness-repair, or opted-in post-Archive capture operation SHALL be performed by one active Wiki specialist instance for the bundle; the operation SHALL NOT be split across concurrent Wiki specialists.

#### Scenario: Wiki operation restructures the bundle
- **WHEN** capture, seed, or approved readiness repair needs to inspect and modify multiple Wiki pages
- **THEN** one Wiki specialist owns the review and all bundle changes for that operation

#### Scenario: Archive triggers an opted-in capture
- **WHEN** a successful OpenSpec Archive triggers an enabled Wiki capture
- **THEN** one Wiki specialist owns the post-Archive review and all Wiki changes

### Requirement: Wiki specialist work is limited to the Wiki domain
The Wiki specialist SHALL perform capture, query, seed, and Wiki maintenance only. It MAY read relevant project sources but SHALL write only under `.opendevkit/wiki/`.

#### Scenario: Wiki operation needs project context
- **WHEN** capture or seed needs project context to create or verify knowledge
- **THEN** the specialist reads relevant sources and confines writes to the Wiki bundle

### Requirement: Wiki captures require an explicit request
The `/odk-wiki-capture` command SHALL capture only knowledge the user explicitly identifies. A successful OpenSpec Archive SHALL also authorize capture when the project has explicitly opted in to automatic post-Archive capture. The specialist MAY inspect directly relevant project sources and retrieve linked external sources or assets when needed, but SHALL NOT perform a broad repository or Git-history scan or capture unrelated material. Secrets and credentials SHALL be excluded.

#### Scenario: User requests capture
- **WHEN** the user invokes `/odk-wiki-capture` and requests project knowledge capture
- **THEN** the module records the requested knowledge in the project wiki

#### Scenario: Related project sources provide context
- **WHEN** the user identifies a topic and directly relevant project sources exist
- **THEN** the module consults those sources, records only knowledge relevant to the requested topic, and retains source provenance

#### Scenario: Opted-in Archive requests capture
- **WHEN** a successful OpenSpec Archive occurs in a project with automatic Wiki capture enabled
- **THEN** the Wiki specialist captures durable knowledge from the archived change and directly relevant current project sources, records provenance, and does not perform a broad repository or Git-history scan

#### Scenario: Relevant external source is linked
- **WHEN** an external page or asset is directly relevant to the requested topic and needed to ground it
- **THEN** the specialist retrieves it when accessible and records its provenance

#### Scenario: Unrelated repository content exists
- **WHEN** the user requests capture of a specific topic and unrelated repository or Git-history content exists
- **THEN** the module does not scan or capture that unrelated content

#### Scenario: No capture request was made
- **WHEN** a conversation contains potentially useful knowledge but the user has not invoked `/odk-wiki-capture` and no opted-in successful Archive has occurred
- **THEN** the module does not create or modify wiki content

### Requirement: Capture requires an initialized Wiki
The `/odk-wiki-capture` command SHALL not initialize a missing Wiki; it SHALL report that the Wiki does not exist and direct the user to `/odk-wiki-seed`.

#### Scenario: Capture is invoked without a Wiki
- **WHEN** the user invokes `/odk-wiki-capture` and `.opendevkit/wiki/` does not exist
- **THEN** the command reports that the Wiki must first be initialized with `/odk-wiki-seed` and does not create Wiki content

### Requirement: Each capture maintains the whole Wiki
Each `/odk-wiki-capture`, each opted-in post-Archive capture, each `/odk-wiki-seed` run against an existing Wiki, and each user-approved readiness repair SHALL review the entire Wiki for organization, duplicate or conflicting knowledge, broken references, index consistency, and OKF conformance before changing the bundle.

#### Scenario: Capture triggers whole-Wiki review
- **WHEN** the user invokes `/odk-wiki-capture`
- **THEN** the module reviews the complete Wiki bundle before integrating the requested knowledge

#### Scenario: Archive capture triggers whole-Wiki review
- **WHEN** a successful OpenSpec Archive triggers an opted-in capture
- **THEN** the module reviews the complete Wiki bundle before integrating the archived change knowledge

#### Scenario: Reseeding an existing Wiki triggers whole-Wiki review
- **WHEN** the user invokes `/odk-wiki-seed` and a Wiki already exists
- **THEN** the module reviews the complete Wiki bundle before reconciling repository knowledge

#### Scenario: Approved readiness repair triggers whole-Wiki review
- **WHEN** the user approves Wiki repair proposed by the readiness workflow
- **THEN** the Wiki specialist reviews the complete Wiki bundle before making repairs

#### Scenario: New knowledge overlaps existing content
- **WHEN** the requested knowledge duplicates or conflicts with existing Wiki content
- **THEN** the module reconciles the relevant existing content instead of creating an unreviewed duplicate

### Requirement: Whole-Wiki maintenance may restructure the Wiki when justified
During capture, reseeding, or approved readiness repair, the module SHALL create, move, rename, merge, split, or delete pages and change taxonomy when needed to keep information clear, concise, and separated by topic. It SHALL preserve unique knowledge and source provenance and update affected links and indexes.

#### Scenario: Taxonomy needs restructuring
- **WHEN** the whole-Wiki review finds that topics are conflated or separated poorly
- **THEN** the module restructures the affected pages and taxonomy and updates their links and indexes

#### Scenario: Duplicate pages are consolidated
- **WHEN** the review finds pages with overlapping knowledge
- **THEN** the module consolidates them, preserves unique information and provenance, and updates or removes affected links and index entries

### Requirement: Whole-Wiki maintenance avoids unnecessary rewrites
Capture, reseeding, and approved readiness repair SHALL leave pages unchanged when their content, structure, provenance, references, and format do not need maintenance.

#### Scenario: A page needs no maintenance
- **WHEN** a page has no content, relationship, index, provenance, or format issue relevant to the capture
- **THEN** the module leaves that page unchanged

### Requirement: Wiki taxonomy follows adaptive guidance
The Wiki SHALL use a starter taxonomy as guidance rather than a fixed directory tree. Suggested areas such as overview, architecture, development, operations, decisions, and reference SHALL be created, retained, or refactored only when project knowledge warrants them.

#### Scenario: Wiki is seeded without content for a category
- **WHEN** `/odk-wiki-seed` creates or updates the Wiki and finds no eligible knowledge for a suggested area
- **THEN** it does not create an empty or irrelevant taxonomy category

#### Scenario: Project knowledge needs a new category
- **WHEN** capture, seeding, or approved repair finds a coherent topic that does not fit the existing taxonomy
- **THEN** the module may create a project-appropriate category and update the Wiki index and links

### Requirement: Whole-Wiki maintenance reports structural changes
After capture, reseeding, or approved readiness repair refactors the Wiki, the module SHALL summarize created, changed, moved, merged, or deleted pages and taxonomy changes.

#### Scenario: Wiki maintenance completes a refactor
- **WHEN** capture, seed, or approved repair finishes with changes to Wiki structure
- **THEN** the response identifies the structural changes made

### Requirement: Whole-Wiki maintenance asks when knowledge cannot be safely reconciled
If capture, reseeding, or approved repair encounters conflicting information that cannot be reconciled without risking loss of unique knowledge or provenance, the Wiki specialist SHALL preserve it and return a clarification request to the orchestrator rather than guessing or deleting it.

#### Scenario: Conflicting facts remain unresolved
- **WHEN** capture, seed, or approved repair encounters materially conflicting knowledge with no reliable basis to choose
- **THEN** the specialist preserves the conflicting information and asks the orchestrator to obtain user clarification

### Requirement: Wiki distinguishes intent from implementation evidence
The Wiki specialist SHALL treat explicit user decisions as evidence of project intent, current code and configuration as evidence of implemented behavior, and external sources as context; it SHALL preserve these distinctions when they disagree.

#### Scenario: Intent differs from current implementation
- **WHEN** an explicit user decision conflicts with current code or configuration
- **THEN** the Wiki records the intended decision separately from the observed implementation state

#### Scenario: External source conflicts with project evidence
- **WHEN** an external source conflicts with an explicit project decision or current implementation evidence
- **THEN** the specialist does not treat the external source as authoritative over the project evidence

### Requirement: Superseded Wiki claims are removed
When current authoritative evidence shows that a Wiki claim is obsolete, the specialist SHALL replace or remove that claim rather than keep a historical copy in the Wiki; Git history remains the historical record.

#### Scenario: Current evidence supersedes a Wiki claim
- **WHEN** current authoritative evidence establishes that a Wiki claim no longer describes the intended or implemented project
- **THEN** the specialist updates or removes the obsolete claim without preserving an archive copy in the Wiki

### Requirement: Wiki pages follow OKF v0.2
The Wiki SHALL be one canonical OKF v0.2 Markdown bundle. Each non-reserved concept SHALL have parseable YAML frontmatter with a non-empty `type`; canonical `title` and `description` fields are optional, and captured project knowledge SHALL retain provenance in `sources`.

#### Scenario: Capture validates the Wiki bundle
- **WHEN** a capture completes its maintenance pass
- **THEN** the module validates concept frontmatter and provenance against OKF v0.2, including every concept's required `type`

### Requirement: Source records identify their evidence
Each `sources` entry SHALL include the canonical `resource` field. The resource SHALL identify an absolute external URL or a bundle-relative project source path; optional canonical fields and producer-defined extensions SHALL NOT replace `resource`.

#### Scenario: Repository source is recorded
- **WHEN** captured knowledge is grounded in a repository source
- **THEN** its source entry identifies the project source with a bundle-relative `resource`

#### Scenario: External source is recorded
- **WHEN** captured knowledge is grounded in an external source
- **THEN** its source entry identifies the source with an absolute URL in `resource`

### Requirement: Root index version requires bundle conformance
The root `index.md` SHALL declare `okf_version: "0.2"` only when all non-reserved Markdown concepts conform to OKF v0.2. Its frontmatter, when present, SHALL contain only the version declaration.

#### Scenario: All documents conform
- **WHEN** every non-reserved Markdown document has parseable YAML frontmatter with a non-empty `type` and reserved files follow their OKF structure
- **THEN** the root index may declare `okf_version: "0.2"`

#### Scenario: A document does not conform
- **WHEN** one or more non-reserved Markdown documents lack parseable YAML frontmatter or a non-empty `type`
- **THEN** the root index does not declare `okf_version: "0.2"` until conformance is restored

### Requirement: Taxonomy remains inside the Wiki bundle
Project taxonomy SHALL organize documents within the single `.opendevkit/wiki/` bundle using only structure and navigation permitted by OKF v0.2; taxonomy categories SHALL NOT be separate OKF bundles.

#### Scenario: Taxonomy is refactored
- **WHEN** capture or seeding changes Wiki categories
- **THEN** the documents remain in the project Wiki bundle and the root index and references are updated

### Requirement: Wiki content is stored in the kit directory
The Wiki module SHALL store its project knowledge under `.opendevkit/wiki/` in the target project. `/odk-wiki-seed` SHALL create that location if it does not already exist.

#### Scenario: Seed creates a missing Wiki
- **WHEN** the user invokes `/odk-wiki-seed` or explicitly opts in through readiness and `.opendevkit/wiki/` does not exist
- **THEN** the module creates the Wiki there and seeds it with eligible repository knowledge

#### Scenario: Knowledge is captured
- **WHEN** the user invokes `/odk-wiki-capture` and requests knowledge capture
- **THEN** the new or updated content is stored under `.opendevkit/wiki/`

#### Scenario: Seed updates an existing Wiki
- **WHEN** the user invokes `/odk-wiki-seed` or explicitly opts in through readiness and `.opendevkit/wiki/` exists
- **THEN** the module performs whole-Wiki maintenance and adds or reconciles missing or newly relevant repository knowledge

### Requirement: Wiki queries use only Wiki content
The `/odk-wiki-query` command SHALL search only `.opendevkit/wiki/` and SHALL not consult current project files to answer the query.

#### Scenario: Wiki contains the answer
- **WHEN** `.opendevkit/wiki/` contains sufficient information to answer
- **THEN** the command answers using Wiki content

#### Scenario: Wiki does not contain the answer
- **WHEN** `.opendevkit/wiki/` does not contain enough information to answer
- **THEN** the command reports that the Wiki does not contain the answer and does not search the repository

### Requirement: Repository seeding requires explicit user opt-in
Repository and Git-history seeding SHALL run only through the `/odk-wiki-seed` operation, either by direct invocation or through the readiness workflow after the user explicitly opts in. The Wiki specialist MAY retrieve relevant external links or assets when needed and SHALL retain their provenance.

#### Scenario: User invokes seed
- **WHEN** the user invokes `/odk-wiki-seed`
- **THEN** the module begins the repository knowledge scan

#### Scenario: User opts in to seed during readiness
- **WHEN** the readiness workflow finds no Wiki or recommends reseeding and the user explicitly opts in
- **THEN** the orchestrator delegates the `/odk-wiki-seed` operation to the Wiki specialist

#### Scenario: Seed encounters a relevant external reference
- **WHEN** repository knowledge links to an external source needed to understand or verify a relevant topic
- **THEN** the specialist may retrieve that source and records its provenance

#### Scenario: User does not invoke seed
- **WHEN** the user installs the module or invokes capture, query, or readiness without opting in to seed
- **THEN** the module creates no seeded Wiki content

### Requirement: Seeded knowledge excludes prohibited source content
A directly invoked or readiness-approved seed SHALL inspect the current repository and Git history, but SHALL exclude secrets and credentials, generated or vendored content, and binary files from model context and Wiki content.

#### Scenario: Seed scans eligible content
- **WHEN** the user directly invokes `/odk-wiki-seed` or explicitly opts in through readiness
- **THEN** the scan uses eligible current repository content and Git history while excluding the prohibited content

#### Scenario: Sensitive content is detected
- **WHEN** the scan encounters content identified as a secret or credential
- **THEN** that content is neither sent to the model for summarization nor written to the wiki
