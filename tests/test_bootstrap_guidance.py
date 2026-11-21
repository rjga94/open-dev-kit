"""Validate the bootstrap guide's config example and metadata boundary.

Bootstrap is performed by an agent following the guide, not by a runtime
installer; these checks do not exercise an actual installation or GitHub.
"""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def assert_preserved(test, before, after):
    for key, value in before.items():
        test.assertIn(key, after)
        if isinstance(value, dict):
            test.assertIsInstance(after[key], dict)
            assert_preserved(test, value, after[key])
        else:
            test.assertEqual(after[key], value)


class BootstrapGuidanceTests(unittest.TestCase):
    def test_documented_source_merge_preserves_all_existing_settings(self):
        guide = (ROOT / "INSTALL.md").read_text(encoding="utf-8")
        blocks = re.findall(r"```json\n(.*?)\n```", guide, re.DOTALL)
        self.assertEqual(len(blocks), 2)
        before, after = (json.loads(block) for block in blocks)
        assert_preserved(self, before, after)
        self.assertEqual(after["preferences"]["optionalModulesSetup"], "pending")
        self.assertEqual(after["source"]["repository"], "https://github.com/example/odk")
        self.assertRegex(after["source"]["commit"], r"^[0-9a-f]{40}$")
        self.assertEqual(
            after["source"]["commit"], "0123456789abcdef0123456789abcdef01234567"
        )

    def test_catalog_metadata_is_distinct_from_module_assets(self):
        catalog = json.loads(
            (ROOT / ".opendevkit/agents/manifest.json").read_text(encoding="utf-8")
        )
        metadata = set()
        functional = set()
        for module in catalog["optionalModules"].values():
            metadata.update((module["manifest"], module["installGuide"]))
            manifest = json.loads((ROOT / module["manifest"]).read_text(encoding="utf-8"))
            for entry in manifest["files"]:
                functional.update((entry["source"], entry["installAs"]))
        self.assertTrue(metadata)
        self.assertTrue(all((ROOT / path).is_file() for path in metadata))
        self.assertTrue(metadata.isdisjoint(functional))


if __name__ == "__main__":
    unittest.main()
