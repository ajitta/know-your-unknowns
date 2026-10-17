"""render-page.py wraps a page fragment in the shared template and enforces the page contract."""
import importlib.util
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills" / "loop" / "scripts" / "render-page.py"
ASSETS = ROOT / "skills" / "loop" / "assets"
ROUTING = ROOT / "skills" / "loop" / "references" / "output-routing.md"

spec = importlib.util.spec_from_file_location("render_page", SCRIPT)
render_page = importlib.util.module_from_spec(spec)
spec.loader.exec_module(render_page)

FRAGMENT = """<title>Options</title>
<style>.demo{color:var(--accent)}</style>
<h1>Options</h1>
<p>Source: <a href="https://example.com/spec">spec</a></p>
<div class="grid"><div class="card">
<label class="pick"><input type="checkbox" data-reply="A: cache"> resonates</label>
</div></div>
<section class="reply" data-label="Reply" data-copy="Copy" data-copied="Copied">
Proceed with A &amp; B &lt;in order&gt;
</section>
"""


class RenderTest(unittest.TestCase):
    def test_file_form_inlines_template(self):
        page = render_page.render(FRAGMENT, "ko", artifact=False)
        self.assertTrue(page.startswith("<!doctype html>"))
        self.assertIn('<html lang="ko">', page)
        self.assertIn(ASSETS.joinpath("page.css").read_text(encoding="utf-8").strip(), page)
        self.assertIn(ASSETS.joinpath("page.js").read_text(encoding="utf-8").strip(), page)
        # the fragment's own style goes to the head, after the base CSS
        self.assertLess(page.index("--bg:#fff"), page.index(".demo{"))
        self.assertLess(page.index(".demo{"), page.index("</head>"))

    def test_artifact_form_has_no_wrapper(self):
        page = render_page.render(FRAGMENT, "en", artifact=True)
        self.assertTrue(page.startswith("<title>Options</title>\n<style>"))
        self.assertIsNone(re.search(r"<!doctype|<html|<head|<body", page, re.I))
        self.assertIn('<main class="page" lang="en">', page)

    def test_reply_text_survives_without_js(self):
        page = render_page.render(FRAGMENT, "en", artifact=False)
        box = re.search(r'<textarea id="reply"[^>]*>(.*?)</textarea>', page, re.S)
        self.assertEqual(box.group(1), "Proceed with A &amp; B &lt;in order&gt;")
        self.assertIn('id="copy-reply" data-copied="Copied">Copy</button>', page)

    def test_theme_and_accessibility_come_from_the_template(self):
        css = ASSETS.joinpath("page.css").read_text(encoding="utf-8")
        for needle in (':root{--bg', '@media (prefers-color-scheme:dark){:root:not([data-theme="light"])',
                       ':root[data-theme="dark"]', "body{margin:0;background:var(--bg)",
                       ":focus-visible", "prefers-reduced-motion"):
            self.assertIn(needle, css)

    def test_contract_violations_are_refused(self):
        cases = {
            "no title": FRAGMENT.replace("<title>Options</title>", ""),
            "remote image": FRAGMENT + '<img src="https://cdn.example.com/x.png">',
            "cdn script": FRAGMENT + '<script src="//cdn.example.com/lib.js"></script>',
            "fetch": FRAGMENT + "<script>fetch('/api')</script>",
            "css url": FRAGMENT + "<style>body{background:url(https://x.example/a.png)}</style>",
            "no reply": re.sub(r"<section.*</section>", "", FRAGMENT, flags=re.S),
            "empty reply": re.sub(r"(<section[^>]*>).*(</section>)", r"\1\n\2", FRAGMENT, flags=re.S),
            "two replies": FRAGMENT + '<section class="reply">again</section>',
            "document wrapper": "<!doctype html>" + FRAGMENT,
        }
        for name, fragment in cases.items():
            with self.subTest(name), self.assertRaises(ValueError):
                render_page.render(fragment, "en", artifact=False)

    def test_fonts_and_links_are_allowed(self):
        fragment = FRAGMENT + '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter">'
        page = render_page.render(fragment, "en", artifact=False)
        self.assertLess(page.index("fonts.googleapis.com"), page.index("</head>"))

    def test_rendering_twice_is_refused(self):
        page = render_page.render(FRAGMENT, "en", artifact=False)
        with self.assertRaises(ValueError):
            render_page.render(page, "en", artifact=False)

    def test_cli_renders_in_place(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "page.html"
            path.write_text(FRAGMENT, encoding="utf-8")
            done = subprocess.run([sys.executable, str(SCRIPT), str(path), "--lang", "ko"],
                                  capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(done.returncode, 0, done.stderr)
            self.assertIn("1 reply controls", done.stdout)
            self.assertIn('<html lang="ko">', path.read_text(encoding="utf-8"))
            again = subprocess.run([sys.executable, str(SCRIPT), str(path)],
                                   capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(again.returncode, 1)

    def test_routing_doc_names_the_real_paths(self):
        text = ROUTING.read_text(encoding="utf-8")
        self.assertIn("${CLAUDE_PLUGIN_ROOT}/skills/loop/scripts/render-page.py", text)
        for name in ("page.css", "page.js"):
            self.assertIn(f"assets/{name}", text)
            self.assertTrue(ASSETS.joinpath(name).exists())


if __name__ == "__main__":
    unittest.main()
