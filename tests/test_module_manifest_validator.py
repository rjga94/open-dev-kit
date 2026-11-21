"""Focused standard-library tests for module catalog and mapping validation."""

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_module_manifests import validate_catalog


ROOT = Path(__file__).resolve().parents[1]


class ModuleManifestValidatorTests(unittest.TestCase):
    def test_current_catalog_is_valid(self):
        self.assertEqual(validate_catalog(ROOT), [])

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / ".opendevkit/agents").mkdir(parents=True)
        (self.root / ".opendevkit/modules/wiki").mkdir(parents=True)
        (self.root / "source.md").write_text("source", encoding="utf-8")
        (self.root / "install.md").write_text("guide", encoding="utf-8")
        self.catalog_path = ".opendevkit/agents/manifest.json"
        self.module_path = ".opendevkit/modules/wiki/manifest.json"
        self.catalog = {
            "schemaVersion": 1,
            "optionalModules": {
                "wiki": {"manifest": self.module_path, "installGuide": "install.md"}
            },
        }
        self.module = {
            "schemaVersion": 1,
            "id": "wiki",
            "files": [
                {"id": "specialist", "source": "source.md",
                 "installAs": ".opendevkit/wiki/specialist.md", "host": "core"},
                {"id": "profile", "source": "source.md",
                 "installAs": ".github/agents/wiki.agent.md", "host": "github-copilot"},
                {"id": "skill", "source": "source.md",
                 "installAs": ".github/skills/wiki/SKILL.md", "host": "github-copilot"},
            ],
            "adapters": {
                "github-copilot": {
                    "agent": {
                        "specialistFile": "specialist",
                        "profileFile": "profile",
                    },
                    "commands": ["wiki"],
                    "skills": [{"name": "wiki", "file": "skill"}],
                }
            },
        }
        self.write_fixtures()

    def tearDown(self):
        self.temp_dir.cleanup()

    def write_fixtures(self):
        (self.root / self.catalog_path).write_text(
            json.dumps(self.catalog), encoding="utf-8"
        )
        (self.root / self.module_path).write_text(
            json.dumps(self.module), encoding="utf-8"
        )

    def errors(self):
        return validate_catalog(self.root)

    def test_missing_catalog_manifest_reference_fails(self):
        self.catalog["optionalModules"]["wiki"]["manifest"] = (
            ".opendevkit/modules/missing/manifest.json"
        )
        self.write_fixtures()
        self.assertTrue(any("does not exist" in error for error in self.errors()))

    def test_missing_source_path_fails(self):
        self.module["files"][0]["source"] = "missing.md"
        self.write_fixtures()
        self.assertTrue(any("source does not exist" in error for error in self.errors()))

    def test_unsafe_install_destination_fails(self):
        self.module["files"][0]["installAs"] = "../outside.md"
        self.write_fixtures()
        self.assertTrue(any("installAs" in error and "path" in error
                            for error in self.errors()))

    def test_duplicate_install_target_fails(self):
        self.module["files"][1]["installAs"] = self.module["files"][0]["installAs"]
        self.write_fixtures()
        self.assertTrue(any("duplicate install target" in error for error in self.errors()))


if __name__ == "__main__":
    unittest.main()
