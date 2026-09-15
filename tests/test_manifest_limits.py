"""Guard the manifest limits that only the Claude apps upload enforces.

`claude plugin validate --strict` passes a manifest the Customize → Plugins
upload rejects. 0.7.0 shipped a 579-character `description` through local
validation and CI, and the upload form answered "Plugin description must be at
most 500 characters" — the first time anyone had run that check, because until
0.7.0 nobody installed this plugin anywhere but Claude Code.

So the limit lives here instead. The number came from the upload form's own
error message, not from documentation; if the form ever states a different one,
change MANIFEST_DESCRIPTION_MAX and say where the new number came from.

Run with: python3 -m unittest tests.test_manifest_limits -v
"""
import json
import os
import unittest
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = Path(ROOT) / ".claude-plugin" / "plugin.json"

# Observed 2026-09-15, uploading unknowns 0.7.0 to Customize → Plugins.
MANIFEST_DESCRIPTION_MAX = 500


class ManifestLimitsTest(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_description_fits_the_upload_form(self):
        description = self.manifest["description"]
        self.assertLessEqual(
            len(description), MANIFEST_DESCRIPTION_MAX,
            "plugin.json description is %d characters; the Claude apps upload "
            "rejects anything over %d, and `claude plugin validate --strict` "
            "will not tell you." % (len(description), MANIFEST_DESCRIPTION_MAX),
        )

    def test_description_still_says_what_this_is(self):
        """A length cap invites truncation to a phrase nobody can install from."""
        description = self.manifest["description"]
        self.assertGreater(len(description), 80)
        self.assertIn("unknowns", description.lower())


if __name__ == "__main__":
    unittest.main()
