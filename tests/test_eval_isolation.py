"""Both eval runners launch claude outside the signed-in account; no model is called."""
import importlib.util
import json
import os
import shutil
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "evals" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RUNNERS = [load("run_manual_isolation", "run-manual.py"),
           load("run_multiturn_isolation", "run-multiturn.py")]
SIGN_IN_KEYS = ("ANTHROPIC_API_KEY", "CLAUDE_CODE_OAUTH_TOKEN")


class IsolatedEnvTest(unittest.TestCase):
    def setUp(self):
        self.home = tempfile.mkdtemp(prefix="unknowns-test-home-")
        self.addCleanup(shutil.rmtree, self.home, ignore_errors=True)
        self.fresh = os.path.join(self.home, "fresh")
        patcher = mock.patch.dict(os.environ, {"CLAUDE_CONFIG_DIR": self.home})
        patcher.start()
        self.addCleanup(patcher.stop)
        for key in SIGN_IN_KEYS:
            os.environ.pop(key, None)

    def sign_in(self, minutes):
        expires = int((time.time() + minutes * 60) * 1000)
        with open(os.path.join(self.home, ".credentials.json"), "w", encoding="utf-8") as handle:
            json.dump({"claudeAiOauth": {"accessToken": "token-under-test",
                                         "expiresAt": expires}}, handle)

    def test_env_leaves_the_account_out_and_passes_the_token(self):
        self.sign_in(120)
        for runner in RUNNERS:
            env = runner.isolated_env(self.fresh)
            self.assertEqual(env["CLAUDE_CONFIG_DIR"], self.fresh)
            self.assertEqual(env["ENABLE_CLAUDEAI_MCP_SERVERS"], "false")
            self.assertEqual(env["CLAUDE_CODE_OAUTH_TOKEN"], "token-under-test")
            self.assertFalse(os.path.exists(os.path.join(self.fresh, ".credentials.json")))

    def test_an_api_key_is_not_replaced_by_the_login_token(self):
        self.sign_in(120)
        os.environ["ANTHROPIC_API_KEY"] = "key-under-test"
        for runner in RUNNERS:
            env = runner.isolated_env(self.fresh)
            self.assertEqual(env["ANTHROPIC_API_KEY"], "key-under-test")
            self.assertNotIn("CLAUDE_CODE_OAUTH_TOKEN", env)

    def test_no_sign_in_stops_before_the_first_run(self):
        for runner in RUNNERS:
            self.assertNotIn("CLAUDE_CODE_OAUTH_TOKEN", runner.isolated_env(self.fresh))
            with self.assertRaises(SystemExit) as raised:
                runner.check_sign_in()
            self.assertIn("--own-config", str(raised.exception))

    def test_a_token_about_to_expire_stops_before_the_first_run(self):
        self.sign_in(5)
        for runner in RUNNERS:
            with self.assertRaises(SystemExit) as raised:
                runner.check_sign_in()
            self.assertIn("expires", str(raised.exception))


class SandboxDirTest(unittest.TestCase):
    def test_sandbox_avoids_a_temp_dir_under_dot_claude(self):
        home = tempfile.mkdtemp(prefix="unknowns-test-tmp-")
        self.addCleanup(shutil.rmtree, home, ignore_errors=True)
        inside = os.path.join(home, ".claude", "tmp")
        os.makedirs(inside)
        for runner in RUNNERS:
            with mock.patch.object(tempfile, "tempdir", inside):
                made = runner.sandbox_dir("unknowns-test-")
            self.addCleanup(shutil.rmtree, made, ignore_errors=True)
            parts = os.path.normpath(made).replace("\\", "/").lower().split("/")
            self.assertNotIn(".claude", parts)
            self.assertTrue(os.path.isdir(made))

    def test_crowd_run_needs_the_filler_plugin_in_the_cli_log(self):
        manual = RUNNERS[0]
        folder = tempfile.mkdtemp(prefix="unknowns-test-crowd-")
        self.addCleanup(shutil.rmtree, folder, ignore_errors=True)
        log = os.path.join(folder, "eval-debug.log")
        line = ("Skill listing over budget: 71 skills, 35443 chars > 6000 budget"
                " - descriptions will be truncated.")
        with open(log, "w", encoding="utf-8") as handle:
            handle.write("x Loaded inline plugin from path: evalcrowd\n"
                         "x Loaded inline plugin from path: unknowns\nx %s\n" % line)
        listing = manual.listing_report(log)
        self.assertEqual(listing["skills"], 71)
        self.assertEqual(listing["listing_lines"], [line])
        self.assertTrue(manual.crowd_loaded(listing))
        # 2026-11-24: the filler path did not resolve, and only this plugin loaded
        with open(log, "w", encoding="utf-8") as handle:
            handle.write("x Loaded inline plugin from path: unknowns\n"
                         "x Skill listing over budget: 28 skills, 10349 chars > 6000 budget\n")
        self.assertFalse(manual.crowd_loaded(manual.listing_report(log)))
        self.assertFalse(manual.crowd_loaded(None))

    def test_sandbox_keeps_an_ordinary_temp_dir(self):
        # made by the runner itself, so it is outside .claude even when TMP is not
        plain = RUNNERS[0].sandbox_dir("unknowns-test-plain-")
        self.addCleanup(shutil.rmtree, plain, ignore_errors=True)
        for runner in RUNNERS:
            with mock.patch.object(tempfile, "tempdir", plain):
                made = runner.sandbox_dir("unknowns-test-")
            self.assertEqual(os.path.dirname(made), plain)


if __name__ == "__main__":
    unittest.main()
