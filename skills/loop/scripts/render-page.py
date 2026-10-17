#!/usr/bin/env python3
"""Wrap a page fragment in the unknowns page template, in place.

Usage: python3 render-page.py PAGE.html [--lang ko] [--artifact] [--out OUT.html]

The fragment holds only the page's content: a <title> first, the cards and
controls, and one <section class="reply">default assembled reply</section>.
This script inlines ../assets/page.css and ../assets/page.js around it, so the
model never writes the shared theme, accessibility or reply-assembly code.

--artifact  emit the Artifact tool form: no doctype/html/head/body wrapper,
            starting with <title> and <style>.
Exit 1 with a message when the fragment breaks the page contract.
"""
import argparse
import html
import re
import sys
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
MARK = "<!-- unknowns-page -->"
FONT_HOSTS = ("fonts.googleapis.com", "fonts.gstatic.com")
REPLY = re.compile(r"<section\b([^>]*\bclass=\"[^\"]*\breply\b[^\"]*\"[^>]*)>(.*?)</section>", re.S | re.I)
ATTR = re.compile(r"([\w-]+)\s*=\s*\"([^\"]*)\"")


def external_refs(text: str) -> list[str]:
    """Remote resources the page would load. Plain <a href> links are navigation, not loads."""
    bad = []
    loads = re.findall(r"\b(?:src|poster)\s*=\s*[\"']?((?:https?:)?//[^\s\"'>]+)", text, re.I)
    loads += re.findall(r"<link\b[^>]*\bhref\s*=\s*[\"']?((?:https?:)?//[^\s\"'>]+)", text, re.I)
    loads += re.findall(r"url\(\s*[\"']?((?:https?:)?//[^\s\"')]+)", text, re.I)
    loads += re.findall(r"@import\s+[\"']((?:https?:)?//[^\"']+)", text, re.I)
    bad += [url for url in loads if not any(host in url for host in FONT_HOSTS)]
    for script in re.findall(r"<script\b[^>]*>(.*?)</script>", text, re.S | re.I):
        bad += re.findall(r"\bfetch\s*\(|\bXMLHttpRequest\b|\bimport\s*\(|\bWebSocket\b", script)
    return bad


def reply_panel(attrs: str, inner: str) -> str:
    fields = dict(ATTR.findall(attrs))
    label = fields.pop("data-label", "Reply")
    copy = fields.pop("data-copy", "Copy")
    copied = fields.pop("data-copied", "Copied")
    text = re.sub(r"<[^>]+>", "", re.sub(r"<br\s*/?>", "\n", inner, flags=re.I))
    text = html.unescape(text)
    text = "\n".join(line.strip() for line in text.splitlines()).strip()
    keep = " ".join(f'{k}="{html.escape(v)}"' for k, v in fields.items() if k != "class")
    return (f'<section class="reply" {keep}>\n<h2>{html.escape(label)}</h2>\n'
            f'<textarea id="reply" aria-label="{html.escape(label)}">{html.escape(text)}</textarea>\n'
            f'<div class="row"><button type="button" id="copy-reply" data-copied="{html.escape(copied)}">'
            f'{html.escape(copy)}</button></div>\n</section>')


def render(fragment: str, lang: str, artifact: bool) -> str:
    if MARK in fragment:
        raise ValueError("already rendered — edit this page directly, or rewrite the fragment and render again")
    if re.search(r"<!doctype|<html\b|<head\b|<body\b", fragment, re.I):
        raise ValueError("write a fragment: no <!doctype>, <html>, <head> or <body>")
    title = re.search(r"<title>(.*?)</title>", fragment, re.S | re.I)
    if not title:
        raise ValueError("start the fragment with <title>…</title>")
    bad = external_refs(fragment)
    if bad:
        raise ValueError("external resources are not allowed: " + ", ".join(sorted(set(bad))[:5]))
    replies = REPLY.findall(fragment)
    if len(replies) != 1:
        raise ValueError('add exactly one <section class="reply">default assembled reply as plain text</section>')
    if not replies[0][1].strip():
        raise ValueError("the reply section must hold the default assembled reply (it is what shows with JS off)")

    body = fragment.replace(title.group(0), "", 1)
    styles = re.findall(r"<style\b[^>]*>.*?</style>", body, re.S | re.I)
    links = re.findall(r"<link\b[^>]*>", body, re.I)
    for chunk in styles + links:
        body = body.replace(chunk, "", 1)
    body = REPLY.sub(lambda m: reply_panel(m.group(1), m.group(2)), body, count=1).strip()
    css = (ASSETS / "page.css").read_text(encoding="utf-8").strip()
    js = (ASSETS / "page.js").read_text(encoding="utf-8").strip()
    head = "\n".join([f"<title>{title.group(1).strip()}</title>", *links,
                      f"<style>\n{css}\n</style>", *styles])
    main = f'<main class="page" lang="{html.escape(lang)}">\n{body}\n</main>\n<script>\n{js}\n</script>'
    if artifact:
        return f"{head}\n{MARK}\n{main}\n"
    return (f'<!doctype html>\n<html lang="{html.escape(lang)}">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n{head}\n</head>\n'
            f"<body>\n{MARK}\n{main}\n</body>\n</html>\n")


def main() -> int:
    ap = argparse.ArgumentParser(description="Wrap a page fragment in the unknowns page template.")
    ap.add_argument("page")
    ap.add_argument("--lang", default="en", help="language of the page's prose (BCP 47, e.g. ko, en)")
    ap.add_argument("--artifact", action="store_true", help="Artifact tool form (no document wrapper)")
    ap.add_argument("--out", help="write here instead of overwriting PAGE")
    args = ap.parse_args()
    src = Path(args.page)
    try:
        fragment = src.read_text(encoding="utf-8")
        page = render(fragment, args.lang, args.artifact)
    except (ValueError, OSError) as err:
        print(f"render-page: {err}", file=sys.stderr)
        return 1
    out = Path(args.out) if args.out else src
    out.write_text(page, encoding="utf-8")
    controls = len(re.findall(r"\bdata-reply\s*=", fragment))
    print(f"render-page: wrote {out} ({len(page.encode('utf-8'))} bytes, {controls} reply controls)")
    if controls == 0:
        print("render-page: warning — no [data-reply] controls, so the reply never changes", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
