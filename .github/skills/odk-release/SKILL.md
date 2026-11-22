---
name: odk-release
description: Publish an ODK Git tag and GitHub pre-release for a selected commit.
disable-model-invocation: true
---

# Release ODK

This repository-local skill creates a Git tag and a GitHub Release for the
requested commit. An explicit invocation authorizes the release workflow; ask
for clarification before publishing if the target, baseline, repository, or
other necessary choice is ambiguous. Follow applicable tool permission prompts.
If the required tools or permissions are unavailable, report the blocker.
This skill is for maintaining ODK, not for installation in projects using it.

1. **Identify the target and repository.** Resolve the requested commit, or
   `HEAD` when no commit is specified, to its full commit SHA. Confirm the
   GitHub repository and push destination refer to the intended repository,
   and that the target commit is available on GitHub. Do not silently substitute
   a branch tip or include uncommitted changes. Stop if the target or
   destination cannot be verified.
2. **Establish the baseline.** Inspect all remote version tags and GitHub
   Releases, including pre-releases and all pages, alongside local history.
   Resolve annotated tags to commits and compare versions numerically, not
   lexically. Select the most recent applicable version whose commit is an
   ancestor of the target. Do not ignore a newer version on a different
   history, an existing version without a matching release, or conflicting
   local and remote tags: explain the ambiguity and ask before proceeding.
   Verify that the checkout has the complete history needed for the analysis;
   an inaccessible remote, incomplete pagination, missing objects, or shallow
   history is not evidence that no previous release exists. Stop if a
   trustworthy baseline or range cannot be established.
3. **Choose the alpha version.** Use [Semantic Versioning 2.0.0](https://semver.org/).
   While alpha policy remains in effect, use `v0.1.0` for the first release
   only when no previous version exists. For every later release, increment
   the previous version's minor component and reset its patch component to
   zero: for example, `v0.2.0` becomes `v0.3.0`. Keep the major version at
   zero until the maintainer explicitly changes the policy. This is ODK's
   chosen `0.y.z` policy, not a rule SemVer requires for initial development.
4. **Analyze the release.** Review every commit in the previous release
   commit's exclusive to target commit's inclusive range, including commit
   bodies and relevant diffs; for the first release, review the complete
   available history through the target. Do not rely only on commit subject
   prefixes. Prepare release notes describing user-visible features and fixes
   and clearly identifying breaking changes and their impact. If evidence is
   insufficient to assess an impact, say so rather than inventing details.
   The analysis informs the notes; the alpha policy determines the bump.
5. **Publish and verify.** Before writing, check that the selected version
   does not conflict with an existing local or remote tag or GitHub Release.
   Never move, replace, or delete an existing published version. Create an
   annotated `v`-prefixed tag at the resolved target commit, push that specific
   tag, and create a GitHub Release using the tag and prepared notes, marked
   as a pre-release. Verify that the remote tag resolves to the intended
   commit and that the GitHub Release references the tag and is marked as a
   pre-release. GitHub pre-releases may not appear as the latest stable
   release. Report the version, commit, release URL, and verification result.

If any step fails, stop and report what succeeded, what failed, and any
existing tag or release. In particular, if the tag was pushed but release
creation failed, do not overwrite or delete the tag; offer to resume after
checking that it still points to the intended commit. Do not claim success
unless publication has been verified.
