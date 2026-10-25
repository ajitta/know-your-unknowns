"""render-page.py wraps a page fragment in the shared template and enforces the page contract."""
import importlib.util
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "plugins" / "unknowns" / "skills" / "loop" / "scripts" / "render-page.py"
ASSETS = ROOT / "plugins" / "unknowns" / "skills" / "loop" / "assets"
ROUTING = ROOT / "plugins" / "unknowns" / "skills" / "loop" / "references" / "output-routing.md"

spec = importlib.util.spec_from_file_location("render_page", SCRIPT)
render_page = importlib.util.module_from_spec(spec)
_bytecode = sys.dont_write_bytecode
try:
    sys.dont_write_bytecode = True
    spec.loader.exec_module(render_page)
finally:
    sys.dont_write_bytecode = _bytecode

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
            again = subprocess.run([sys.executable, str(SCRIPT), str(path), "--lang", "ko"],
                                   capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(again.returncode, 1)

    def test_cli_survives_a_legacy_windows_console(self):
        # Windows consoles often run cp1252 or cp949; a Korean file name must not crash the run.
        import os
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "지출-요약.html"
            path.write_text(FRAGMENT, encoding="utf-8")
            env = dict(os.environ, PYTHONIOENCODING="cp1252", PYTHONUTF8="0")
            done = subprocess.run([sys.executable, str(SCRIPT), str(path), "--lang", "ko"],
                                  capture_output=True, env=env)
            self.assertEqual(done.returncode, 0, done.stderr)
            again = subprocess.run([sys.executable, str(SCRIPT), str(path), "--lang", "ko"],
                                   capture_output=True, env=env)
            self.assertEqual(again.returncode, 1)
            self.assertIn(b"already rendered", again.stderr)

    def test_output_uses_lf_on_every_os(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "page.html"
            path.write_text(FRAGMENT, encoding="utf-8")
            subprocess.run([sys.executable, str(SCRIPT), str(path), "--lang", "en"], check=True,
                           capture_output=True)
            self.assertNotIn(b"\r\n", path.read_bytes())

    def test_routing_doc_names_paths_relative_to_itself(self):
        # Reference files are opened with Read, so ${CLAUDE_PLUGIN_ROOT} is never substituted
        # in them and is not set in the shell; the doc must locate the template from itself.
        text = ROUTING.read_text(encoding="utf-8")
        self.assertIn('"<template>/scripts/render-page.py"', text)
        self.assertNotIn("${CLAUDE_PLUGIN_ROOT}/skills/loop/scripts", text)
        template = ROUTING.parent.parent
        self.assertTrue((template / "scripts" / "render-page.py").exists())
        for name in ("page.css", "page.js"):
            self.assertIn(f"<template>/assets/{name}" if name == "page.css" else name, text)
            self.assertTrue((template / "assets" / name).exists())

    def test_attribute_entities_are_decoded_once(self):
        fragment = FRAGMENT.replace('data-label="Reply"', 'data-label="Q&amp;A" data-head="Brief &quot;v2&quot;&#10;Points:"')
        page = render_page.render(fragment, "en", artifact=False)
        self.assertIn("<h2>Q&amp;A</h2>", page)
        self.assertIn('data-head="Brief &quot;v2&quot;\nPoints:"', page)
        self.assertNotIn("&amp;amp;", page)
        self.assertNotIn("&amp;quot;", page)
        self.assertNotIn("&amp;#10;", page)

    def test_reply_section_variants(self):
        single = FRAGMENT.replace('<section class="reply"', "<section class='card reply' id=\"reply\" data-label='회신'")
        page = render_page.render(single, "ko", artifact=False)
        self.assertIn('<section class="reply card"', page)
        self.assertIn("<h2>회신</h2>", page)
        self.assertEqual(page.count('id="reply"'), 1)
        hint = FRAGMENT + '<p class="reply-hint">hint</p><section class="no-reply">x</section>'
        render_page.render(hint, "en", artifact=False)  # only the class token "reply" counts
        with self.assertRaises(ValueError):
            render_page.render(FRAGMENT.replace("Proceed with", "<section>x</section>Proceed with"), "en", False)

    def test_block_markup_in_the_reply_keeps_its_lines(self):
        fragment = re.sub(r"(<section[^>]*>).*(</section>)", r"\1<p>one</p><ul><li>two</li><li>three</li></ul>\2",
                          FRAGMENT, flags=re.S)
        page = render_page.render(fragment, "en", artifact=False)
        self.assertIn('<textarea id="reply" aria-label="Reply">one\ntwo\nthree</textarea>', page)

    def test_script_text_is_left_alone(self):
        fragment = FRAGMENT + '<script>const s = "<style>.a{}</style>";</script>'
        page = render_page.render(fragment, "en", artifact=False)
        self.assertIn('const s = "<style>.a{}</style>";', page)

    def test_title_with_attributes_and_bom(self):
        page = render_page.render(FRAGMENT.replace("<title>", '<title id="t">'), "en", artifact=False)
        self.assertIn("<title>Options</title>", page)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "page.html"
            path.write_bytes(b"\xef\xbb\xbf" + FRAGMENT.encode("utf-8"))
            subprocess.run([sys.executable, str(SCRIPT), str(path), "--lang", "en"], check=True, capture_output=True)
            self.assertNotIn("\ufeff", path.read_text(encoding="utf-8"))

    def test_external_resources_more_forms(self):
        refused = [
            '<img srcset="https://cdn.example.com/a.png 1x">',
            '<svg><image href="https://cdn.example.com/a.png"/></svg>',
            '<svg><use xlink:href="https://cdn.example.com/s.svg#i"/></svg>',
            '<object data="https://cdn.example.com/a.pdf"></object>',
            '<button onclick="fetch(\'https://x.example\')">x</button>',
            "<script>navigator.sendBeacon('/x')</script>",
            '<link rel="stylesheet" href="https://evil.example/fonts.googleapis.com.css">',
            '<script src="https://fonts.googleapis.com/evil.js"></script>',
            '<script src="app.js"></script>',
            '<img src="shot.png">',
        ]
        for extra in refused:
            with self.subTest(extra), self.assertRaises(ValueError):
                render_page.render(FRAGMENT + extra, "en", artifact=False)
        refused += [
            '<script>const i = new Image(); i.src = "https://x.example/p.gif";</script>',
            '<pre><img src="https://cdn.example.com/a.png"></pre>',
            '<pre style="background:url(https://cdn.example.com/a.png)">x</pre>',
        ]
        for extra in refused[-3:]:
            with self.subTest(extra), self.assertRaises(ValueError):
                render_page.render(FRAGMENT + extra, "en", artifact=False)
        allowed = [
            # canvas and data-URI demos written in JS are not markup
            "<script>for(var i=0;i<w*h;i++){} var src=new Float32Array(3); x=a>>>0;</script>",
            "<script>for(let i=0;i<n;i++){ img.src = c.toDataURL(); } if(a>b){}</script>",
            '<script>canvas.toDataURL("image/png"); URL.createObjectURL(new Blob([s]));</script>',
            "<script>new URL(location.href).searchParams</script>",
            "<script>items.map(c => `<img src=\"${c.img}\">`)</script>",
            "<p><code>background:url(https://cdn.example.com/a.png)</code></p>",
            '<textarea>&lt;img src="https://x"&gt; fetch(x)</textarea>',
            '<pre>&lt;img src="https://cdn.example.com/a.png"&gt;</pre>',
            "<pre><code>const r = await fetch(url)</code></pre>",
            '<img src="data:image/png;base64,iVBORw0KGgo=">',
            '<svg><use href="#icon"/></svg>',
            "<style>@import url('https://fonts.googleapis.com/css2?family=Inter');</style>",
        ]
        for extra in allowed:
            with self.subTest(extra):
                render_page.render(FRAGMENT + extra, "en", artifact=False)

    def test_cli_errors_are_messages_not_tracebacks(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "page.html"
            path.write_text(FRAGMENT, encoding="utf-8")
            done = subprocess.run([sys.executable, str(SCRIPT), str(path), "--lang", "en",
                                   "--out", str(Path(tmp) / "missing" / "x.html")],
                                  capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(done.returncode, 1)
            self.assertNotIn("Traceback", done.stderr)
            no_lang = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True)
            self.assertEqual(no_lang.returncode, 2)  # --lang is required

    def test_skill_zips_carry_the_template(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([sys.executable, str(ROOT / "scripts" / "build-skill-zips.py"), "--out", tmp],
                           check=True, capture_output=True)
            import zipfile
            with zipfile.ZipFile(Path(tmp) / "brainstorm.zip") as zf:
                names = set(zf.namelist())
                self.assertTrue({"brainstorm/assets/page.css", "brainstorm/assets/page.js",
                                 "brainstorm/scripts/render-page.py",
                                 "brainstorm/references/output-routing.md"} <= names)
                self.assertNotIn("CLAUDE_PLUGIN_ROOT", zf.read("brainstorm/SKILL.md").decode("utf-8"))
            with zipfile.ZipFile(Path(tmp) / "interview.zip") as zf:
                self.assertFalse(any("/assets/" in n for n in zf.namelist()))

if __name__ == "__main__":
    unittest.main()
