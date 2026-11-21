"""Check documented module setup flows, not a runtime installation."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class ReadinessModuleGuidanceTests(unittest.TestCase):
    def test_selected_and_empty_selection_use_only_selected_metadata(self):
        workflow = read(".opendevkit/workflows/readiness-refactor.md")
        catalog = json.loads(read(".opendevkit/agents/manifest.json"))
        wiki = catalog["optionalModules"]["wiki"]
        self.assertTrue((ROOT / wiki["manifest"]).is_file())
        self.assertTrue((ROOT / wiki["installGuide"]).is_file())
        self.assertIn("load only each selected module's", workflow)
        self.assertIn("do not load unselected modules' manifests or guides as setup inputs", workflow)
        self.assertIn("For an empty selection load none as setup inputs", workflow)
        self.assertIn("An empty selection still has a configuration plan", workflow)
        self.assertIn("`installAs` destinations", workflow)

    def test_questions_and_answers_precede_one_plan(self):
        workflow = read(".opendevkit/workflows/readiness-refactor.md")
        self.assertIn("only unanswered module-specific decisions", workflow)
        self.assertIn("already answered by the user or established in project configuration", workflow)
        self.assertIn("do not infer an ambiguous answer", workflow)
        self.assertIn("without an extra module-specific interview", workflow)
        self.assertIn("one consolidated exact plan", workflow)
        self.assertIn("module-specific answers and their effects", workflow)
        self.assertIn("configuration changes", workflow)
        self.assertLess(workflow.index("ODK asks those targeted questions"),
                        workflow.index("one consolidated exact plan"))
        guide = read(".opendevkit/modules/wiki/install.md")
        self.assertIn("No Wiki-specific answer is needed", guide)
        self.assertIn("Do not ask whether to\nseed or repair Wiki data", guide)

    def test_readiness_command_metadata_uses_only_the_new_name(self):
        readiness = read(".opendevkit/agents/readiness.md")
        catalog = read(".opendevkit/agents/manifest.json")
        agent_profile = read(".github/agents/odk.agent.md")
        skill = read(".github/skills/odk-readiness-check/SKILL.md")

        self.assertIn("/odk-readiness-check", readiness)
        self.assertIn('"commands": ["odk-readiness-check"]', catalog)
        self.assertIn('"name": "odk-readiness-check"', catalog)
        self.assertIn("skills: ['odk-readiness-check']", agent_profile)
        self.assertIn("name: odk-readiness-check", skill)
        for text in (readiness, catalog, agent_profile, skill):
            self.assertNotIn("odk-readiness-refactor", text)

    def test_entry_points_preserve_shared_boundaries(self):
        for path in (
            ".opendevkit/agents/readiness.md",
            ".opendevkit/agents/orchestrator.md",
            ".github/skills/odk-readiness-check/SKILL.md",
        ):
            with self.subTest(path=path):
                text = read(path)
                self.assertIn("pending", text)
                self.assertIn("configured", text)
                self.assertIn("selected module", text)
                self.assertIn("unanswered module-specific", text)
                self.assertIn("consolidated exact plan", text)
                self.assertIn("conflict", text)
                self.assertIn("approval", text)
                self.assertIn("seed", text)
                self.assertIn("repair", text)

    def test_recorded_provenance_never_falls_back_on_retrieval_failure(self):
        for path in (
            ".opendevkit/workflows/readiness-refactor.md",
            ".opendevkit/agents/readiness.md",
            ".opendevkit/agents/orchestrator.md",
            ".github/skills/odk-readiness-check/SKILL.md",
        ):
            with self.subTest(path=path):
                text = read(path)
                self.assertIn("source.repository", text)
                self.assertIn("source.commit", text)
                self.assertIn("read-only", text)
                self.assertIn("branch", text)
                self.assertIn("latest", text)
                self.assertIn("abbreviated", text)
                self.assertIn("partial plan", text)
                self.assertIn("cannot be retrieved or validated", text)
                self.assertRegex(text, r"even (?:on|if) (?:retrieval )?fail")

        workflow = read(".opendevkit/workflows/readiness-refactor.md")
        self.assertIn("`files[].source`", workflow)
        self.assertIn("every manifest `installAs` destination", workflow)
        self.assertIn("complete proposed contents or diff for each destination", workflow)
        self.assertIn("retrieved and validated above", workflow)
        self.assertIn("separate replacement approval", workflow)
        self.assertIn("module-atomic conflict behavior", workflow)

    def test_legacy_resolution_and_complete_same_commit_plan(self):
        workflow = read(".opendevkit/workflows/readiness-refactor.md")
        for requirement in (
            "If source provenance is entirely absent",
            "https://github.com/rjga94/ai-dev-ki",
            "current default branch",
            "Resolve once",
            "full 40-hex commit SHA",
            "retrieve everything by that immutable SHA",
            "applies even for an empty selection",
            "pinned `INSTALL.md` and core catalog",
            "every catalog-referenced lightweight module manifest and install guide",
            "every selected module's manifest, guide, and functional sources",
            "from the same repository and SHA",
            "Use the pinned selected manifests and guides",
            "not consulted for module setup",
            "do not retrieve or install unselected functional assets or module data",
            "all ODK-managed core target paths and their proposed contents or diffs",
            "If a `source` record is present but incomplete or malformed",
            "do not include unrelated project files",
            "preserving unrelated settings and existing selections",
            "source resolution",
            "do not prepare a partial plan or write anything",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, workflow)

    def test_legacy_decline_and_core_conflict_stop_the_entire_refresh(self):
        workflow = read(".opendevkit/workflows/readiness-refactor.md")
        self.assertIn(
            "If the legacy plan is declined, or a required core replacement is not approved",
            workflow,
        )
        self.assertIn(
            "do not apply any of the core refresh or selected module installation",
            workflow,
        )
        self.assertIn(
            "leave existing core and module files and configuration unchanged and setup pending",
            workflow,
        )
        self.assertIn("Before any legacy refresh or module write", workflow)
        self.assertIn("separate replacement approval for each required core replacement", workflow)
        self.assertIn("separate replacement approval for each conflicting target", workflow)
        self.assertIn("leave all files for that module unchanged", workflow)
        for path in (
            ".opendevkit/agents/readiness.md",
            ".opendevkit/agents/orchestrator.md",
            ".github/skills/odk-readiness-check/SKILL.md",
        ):
            with self.subTest(path=path):
                text = read(path)
                self.assertRegex(
                    text,
                    r"(?:unapproved required core replacement|"
                    r"required core replacement is unapproved)",
                )
                self.assertIn("core and module files and configuration unchanged", text)
                self.assertIn("setup pending", text)

    def test_preflight_exact_approval_and_module_atomic_conflict_decline(self):
        workflow = read(".opendevkit/workflows/readiness-refactor.md")
        for requirement in (
            "inspect every destination, including all core and module targets and configuration",
            "stage validated proposed content without changing project targets",
            "exact conditional config changes and skipped targets",
            "obtains explicit approval of that exact plan",
            "separate explicit replacement decision for every conflicting core and module target",
            "before any target write",
            "Recheck all destinations against the inspected state before applying",
            "Recheck each target immediately before writing it",
            "leave all files for that module unchanged",
            "skip every target of that module, including nonconflicting ones",
            "their dependencies and destinations remain safe",
            "their resulting config is covered by the approved plan",
            "Do not write unapproved alternatives",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, workflow)
        self.assertLess(workflow.index("inspect every destination"),
                        workflow.index("obtains explicit approval of that exact plan"))
        self.assertLess(workflow.index("obtains explicit approval of that exact plan"),
                        workflow.index("separate explicit replacement decision"))
        self.assertLess(workflow.index("separate explicit replacement decision"),
                        workflow.index("Apply only staged, approved material"))

    def test_completed_state_and_partial_failure_are_documented(self):
        workflow = read(".opendevkit/workflows/readiness-refactor.md")
        for requirement in (
            "finish and verify every required core target before installing any selected module or recording",
            "Only after the complete core refresh succeeds",
            "do not record the new provenance",
            "verify each selected module's complete set of targets before enabling it",
            'only when the approved selection is complete, including `[]` for no modules',
            'keep setup `"pending"` and do not enable that module',
            "Preserve unrelated configuration, including other preferences",
            "A write failure can leave a partially written module",
            "do not claim the conflict-decline no-write guarantee applies to failures",
            "do not claim the intended enabled-module, setup, or provenance state was recorded",
            "exactly which files changed, which failed or were not attempted",
            "actual configuration/provenance state",
            "never use a success-shaped fallback",
            "Wiki data",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, workflow)
        for path in (
            ".opendevkit/agents/readiness.md",
            ".opendevkit/agents/orchestrator.md",
            ".github/skills/odk-readiness-check/SKILL.md",
        ):
            with self.subTest(path=path):
                text = read(path)
                for phrase in ("every conflicting target", "before any write",
                               "source.repository", "source.commit",
                               "provenance", "failed", "pending"):
                    self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
