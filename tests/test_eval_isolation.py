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
