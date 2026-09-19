"""Guard the self-hosted marketplace manifest.

Until 0.7.0 the only way in was the catalog repository ajitta/claude-plugins:
`/plugin marketplace add ajitta/claude-plugins`. Traffic said almost nobody
walked it — 21 unique cloners of the catalog against 355 of this repository in
the same fortnight — so this repository now carries its own marketplace.json and
serves itself, the way every comparable plugin does.

That makes two manifests in .claude-plugin/ that have to agree. The failure is
quiet: bump `name` or `version` in plugin.json, leave marketplace.json pointing
at the old name, and `/plugin install` resolves to nothing while local
validation still passes.

Asserted:
  * marketplace.json exists, parses, and lists exactly one plugin
  * that entry's name matches plugin.json's name (the install target)
  * its source is the repository root, "./" — not a URL that could point at a
    fork, and not a subdirectory that does not exist
  * the entry description fits the same 500-character upload limit as the
    manifest one (see test_manifest_limits)

Deliberately not asserted: description wording, or that the two descriptions
match — the catalog entry is a sales pitch, the manifest one is metadata.

Run with: python3 -m unittest tests.test_marketplace_manifest -v
"""
import json
import os
import unittest
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_DIR = Path(ROOT) / ".claude-plugin"
MARKETPLACE = PLUGIN_DIR / "marketplace.json"
MANIFEST = PLUGIN_DIR / "plugin.json"

# Same limit as the plugin.json description; see test_manifest_limits.
DESCRIPTION_MAX = 500


class MarketplaceManifestTest(unittest.TestCase):
    def setUp(self):
        self.assertTrue(
            MARKETPLACE.is_file(),
            "%s is missing; without it `/plugin marketplace add "
            "ajitta/know-your-unknowns` fails and the README's Quick start is a "
            "dead end." % MARKETPLACE,
        )
        self.marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
        self.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_lists_exactly_one_plugin(self):
        plugins = self.marketplace.get("plugins")
        self.assertIsInstance(plugins, list)
        self.assertEqual(
            len(plugins), 1,
            "this repository serves one plugin; a second entry means the "
            "catalog repository's job leaked in here.",
        )

    def test_entry_name_matches_the_manifest(self):
        """`/plugin install <name>@<marketplace>` resolves through this name."""
        entry = self.marketplace["plugins"][0]
        self.assertEqual(
            entry["name"], self.manifest["name"],
            "marketplace.json advertises %r but plugin.json declares %r; the "
            "install command in both READMEs names the former and would "
            "resolve to nothing." % (entry.get("name"), self.manifest["name"]),
        )

    def test_source_is_this_repository_root(self):
        entry = self.marketplace["plugins"][0]
        self.assertEqual(
            entry["source"], "./",
            "the plugin lives at the repository root, so the source must be "
            "'./'. A URL here would pin installs to whatever that URL serves, "
            "defeating the point of self-hosting.",
        )

    def test_owner_is_declared(self):
        owner = self.marketplace.get("owner") or {}
        self.assertTrue(
            (owner.get("name") or "").strip(),
            "marketplace.json needs an owner.name; it is what the plugin "
            "browser shows as the publisher.",
        )

    def test_entry_description_fits_the_upload_form(self):
        description = self.marketplace["plugins"][0]["description"]
        self.assertLessEqual(len(description), DESCRIPTION_MAX)
        self.assertGreater(len(description), 80)
        self.assertIn("unknowns", description.lower())


if __name__ == "__main__":
    unittest.main()
