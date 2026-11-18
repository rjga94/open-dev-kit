---
name: openspec-capture
description: Capture durable conversation and project knowledge into the OpenSpec project wiki (openspec/wiki/), including reference files and links. Use when the user wants to preserve lasting project knowledge, with or without a prior explore session. Also use when the user says "openspec capture" or "opsx capture".
allowed-tools: Bash(openspec:*)
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: openspec
  version: "1.0"
  generatedBy: "1.16.0"
---

Capture durable project knowledge into the wiki.

**This workflow records knowledge; it does not plan or implement.** It writes only to the wiki at `openspec/wiki/` (and the Git LFS files described below). Do not create or edit changes, specs, or project code here.

**Store selection:** If the user names a store (a store is a standalone OpenSpec repo registered on this machine) or the work lives in one, run `openspec store list --json` to discover registered store ids, then pass `--store <id>` on the commands that read or write specs and changes (`new change`, `status`, `instructions`, `list`, `show`, `validate`, `archive`, `doctor`, `context`, `schemas`, `view`). Once selected, treat `--store <id>` as sticky for the rest of the workflow. Every unscoped example of those commands below is shorthand: before running it, append the flag. For example, run `openspec status --change "<name>" --json --store "<id>"`, not the unscoped form shown below. Other commands do not take the flag. Hints printed by commands already carry the flag; keep it on follow-ups. Without a store, commands act on the nearest local `openspec/` root.

**Project check:** These steps expect a project that already uses OpenSpec. Before the first step that writes anything (`new change`, `archive`, `sync specs`, or authoring an artifact file), confirm the project has a root: run `openspec list --json` (with `--store <id>` when a store is selected, since the store is then the root) and read `root`. A root object means the project is set up. `"root": null` means it is not - there is no `openspec/` directory here, and a write such as `openspec new change` would create one as a side effect. The command also exits non-zero, which is that answer rather than a broken CLI, so read the JSON instead of retrying or working around it.

One `"root": null` is not about setup: when a `status` error message starts with `Declared in` or `Invalid store declaration in` and names this project's `openspec/config.yaml` (or `config.yml`), the project does use OpenSpec through a store it declares, which this machine cannot resolve (the store is not registered, or the `store:` line is malformed). Do not treat it as uninitialized and skip the branches below: stop before writing and show the user that error's `message` and `fix`.

Otherwise, with no root, what happens next depends on how this workflow was reached:

- **Auto-selected**: you chose this workflow yourself, without the user naming OpenSpec, naming this skill, or running its slash command. Stop using OpenSpec and answer the request normally, as you would with no OpenSpec installed. Do not ask them to set anything up and do not mention OpenSpec setup.
- **Explicit OpenSpec request**: the user named OpenSpec, named this skill, or ran its slash command. Stop before writing and ask how to proceed: set this project up (`openspec init`), target a store they already have (`--store <id>`), or continue without OpenSpec for this request. Wait for their answer.

In both branches, never create the root as a side effect: do not run `openspec init` until the user asks for it, do not hand-create `openspec/` files, and do not let a command create it.

**Input**: Optionally a focus after the request (for example "capture the auth decisions"). If omitted, capture everything worth keeping from the conversation and relevant project evidence.

It does not matter whether explore was used earlier: capture durable knowledge from the conversation and relevant project evidence.

**Capture procedure** (records durable project knowledge into the wiki):

1. **Resolve the wiki.** Run `openspec context --json` (add `--store "<id>"` when a store is selected). If it reports `no_openspec_root` or fails, write nothing and tell the user the project needs OpenSpec set up first; never create `openspec/` as a side effect. Otherwise the wiki is `<root.path>/openspec/wiki/` (where `root.path` is the root returned by `openspec context --json`, with `--store "<id>"` when a store is selected). The folder is always named `wiki`.

2. **Collect durable knowledge and evidence.** From the whole conversation, collect project background, goals, decisions and their rationale, constraints, open questions, terminology, people and systems involved, and reference material. Also review relevant project evidence; the conversation is not the only source:
   - For a broad or initial capture, including a wiki that exists but lacks established project knowledge, inspect high-signal project documentation and configuration, OpenSpec specs and relevant change artifacts, project structure, and representative source. Capture a useful project overview, architecture, key flows, or design system only when the evidence supports it; do not create empty placeholder pages.
   - For focused or repeated captures, inspect sources relevant to the requested topic and update existing wiki knowledge rather than repeating a broad inventory.
   - Use current source and configuration to describe observed implementation. Use specs, proposals, designs, archived changes, and conversation for requirements, rationale, and historical or planned decisions; label these separately, and report conflicts that cannot be resolved.
   - Record sources for material project claims in the concept's OKF `sources` metadata, and use portable repository-relative Markdown paths. A target that later becomes unavailable does not by itself make a concept nonconformant.
   - Keep source review proportional to the topic; do not scan unrelated code or infer undocumented behavior.
   Leave out chit-chat, step-by-step tool output, and anything already recorded. If the conversation and relevant project evidence contain no durable knowledge missing from the wiki, say so and write nothing, unless the user explicitly requested a format migration.

3. **Read before writing.** If the wiki exists, read its root index when present and consult the pages related to what you collected. If no index is available, use relevant available concepts directly. Update an existing page in place when the topic is already covered; do not create a second page for the same topic. Preserve edits people made by hand and unrecognized frontmatter fields. When updating a legacy page, add OKF metadata to that page in place, preserving its body and links; do not migrate unrelated legacy pages during ordinary capture. If the user explicitly requests a full migration, upgrade every legacy concept in place. If the conversation contradicts a page, update it to the newer information, note on the page that it replaces earlier information, and tell the user.

4. **Organize for navigation.** The wiki is a multi-level OKF v0.2 bundle of Markdown concepts. Every new or updated concept has parseable YAML frontmatter with a non-empty `type`; material evidence is represented in `sources` metadata. Choose categories and page boundaries to fit the knowledge being captured. Possible topics include project context, domain concepts, architecture and decisions, integrations, or research. Create folders and pages only when they help organize real content, not as empty placeholders. Keep an existing layout when it still works. Indexes are optional navigation aids; when an index exists, update it for pages added, changed, or moved in that directory. Create or update indexes when they improve discovery, not to satisfy a required layout or solely to declare a version. Only a root index may carry `okf_version: "0.2"`, and only when every non-reserved Markdown document conforms. A wiki without an index remains readable through its available concepts, and unavailable links do not by themselves make it nonconformant.

5. **Preserve reference material.** Include references from the conversation and relevant project artifacts, such as image paths or links recorded in proposals and designs.
   - **Proposal images:** When the current change's proposal or design links an image in its `references/` directory, copy that linked image into `<wiki>/assets/<change-name>/`. Link the wiki copy from the page that explains the requirement or decision it informed, and record the change name, reference path relative to the change root, and capture date. Do not link the wiki page to the active change path; it will move when archived.
   - Links: record the link, its title, and the date in the page that uses it.
   - Files (images, video, audio, PDFs, Word documents, other files): copy each accessible referenced file that supports captured knowledge into an `assets/` folder inside the wiki and link it from the page that uses it, recording the original source and the capture date. Ensure repository-relative asset links resolve on Windows, macOS, and Linux. Never move or modify the original. If a file is not accessible, record the reference and its original location and tell the user it was not copied.
   - Markdown files copied as references: add minimal OKF `type: Reference` and source metadata to the wiki copy while preserving its body, then list it in the parent index.
   - Very large files: state the file's size and ask the user before copying. If they decline, record the reference and original location without copying.
   - **Git LFS, lazily:** only immediately before copying the first binary file in a capture, and not at all for text-only captures, check the project's Git setup. If the project is not a Git repository, skip this. Otherwise run `git lfs version`. If Git LFS is not installed, do not copy the binary: tell the user how to install it, and record the reference and original location instead. If it is installed, use `git check-attr filter -- <path>` to check the wiki destination and, for proposal images, the source under the change's `references/` directory. If either is not tracked with `filter=lfs`, run `git lfs install --local` and `git lfs track` with patterns covering the resolved wiki assets and change-reference paths, relative to the Git root. Tell the user which Git files changed (normally `.gitattributes`); do not ask for confirmation. Do not rewrite history or migrate files that are already committed.

6. **Review the wiki.** After updating pages and copying accessible files, review the wiki for useful navigation and conflicts in the knowledge being captured. Check indexes that exist and update entries affected by this capture. When moving or reorganizing pages, update affected links whose destinations are known; unrelated missing indexes or unavailable links do not block capture or make the bundle nonconformant. Confirm every new or updated concept has parseable OKF frontmatter with a non-empty `type`. For an ordinary capture, leave unrelated legacy pages in place and do not declare the root version while any non-reserved Markdown document remains nonconformant; for an explicitly requested full migration, upgrade every legacy concept in place before declaring the version. Preserve unique information and hand edits. Keep existing structure and wording when they already work; do not make cosmetic rewrites.

7. **Stay in bounds.** Write only under the wiki folder, plus the Git LFS files above. Never modify `openspec/specs/`, `openspec/changes/`, or project source. Do not merge wiki content into specs; the wiki is a separate knowledge layer that later proposals draw from.

8. **Report.** List the pages created, updated, moved, or removed; assets copied; anything not copied and why; and whether the bundle is fully OKF v0.2-conformant or still contains legacy pages.

**Guardrails**
- Capture is optional; the user can go straight to planning without it. Do not insist on it
- Never create `openspec/` when the project has no OpenSpec root
- Never write outside the wiki folder, except the Git LFS configuration files when a binary file is about to be added
- Never copy a binary file without Git LFS in place; record the reference instead
- Do not duplicate a topic already in the wiki; update the existing page

When the user is ready to plan a change, point them at `/opsx-propose`, which draws on the wiki.
