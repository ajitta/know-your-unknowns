#!/usr/bin/env python3
"""Wrap a page fragment in the unknowns page template, in place.

Usage: python3 render-page.py PAGE.html --lang ko [--artifact] [--out OUT.html]
       (Windows without a python3 command: py -3 render-page.py ... or python render-page.py ...)

The fragment holds only the page's content: a <title> first, the cards and
controls, and one <section class="reply">default assembled reply</section>.
This script inlines ../assets/page.css and ../assets/page.js around it, so the
model never writes the shared theme, accessibility or reply-assembly code.

--artifact  emit the Artifact tool form: no doctype/html/head/body wrapper,
            starting with <title> and <style>.
Exit 1 with a message when the fragment breaks the page contract.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ASSETS = Path(__file__).resolve().parent.parent / "assets"
MARK = "<!-- unknowns-page -->"
FONT_HOSTS = {"fonts.googleapis.com", "fonts.gstatic.com"}
ATTR = re.compile(r"([\w:-]+)\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s\"'>]+))")
SECTION = re.compile(r"<section\b([^>]*)>(.*?)</section>", re.S | re.I)
SCRIPT = re.compile(r"<script\b[^>]*>.*?</script>", re.S | re.I)
# A text box's default holds text, never markup.
TEXTAREA = re.compile(r"<textarea\b[^>]*>.*?</textarea>", re.S | re.I)
LOADERS = r"\bfetch\s*\(|\bXMLHttpRequest\b|\bimport\s*\(|\bWebSocket\b|\bsendBeacon\b|\bEventSource\b"
REMOTE = r"(?:https?:)?//[^\s\"'`)]+"


def attrs(raw: str) -> dict[str, str]:
    """Attribute name -> decoded value, for any quoting style. The first of a repeated name wins, as in browsers."""
    found: dict[str, str] = {}
    for m in ATTR.finditer(raw):
        found.setdefault(m.group(1).lower(), html.unescape(m.group(2) or m.group(3) or m.group(4) or ""))
    return found


def font_url(url: str) -> bool:
    return (urlsplit(url).hostname or "") in FONT_HOSTS


def inline(url: str) -> bool:
    return url.strip().lower().startswith(("data:", "#", "blob:", "about:")) or not url.strip()


def css_refs(css: str) -> list[str]:
    bad = [f"url({u})" for u in re.findall(r"url\(\s*[\"']?([^\"')\s]+)", css, re.I)
           if not inline(u) and not font_url(u)]
    bad += [f"@import {u}" for u in re.findall(r"@import\s+(?:url\(\s*)?[\"']?([^\"')\s;]+)", css, re.I)
            if not font_url(u)]
    return bad


def external_refs(text: str) -> list[str]:
    """Anything the page would load from outside itself. <a href> links are navigation, not loads."""
    scripts = re.findall(r"<script\b[^>]*>(.*?)</script>", text, re.S | re.I)
    markup = TEXTAREA.sub("", SCRIPT.sub(lambda m: re.match(r"<script\b[^>]*>", m.group(0), re.I).group(0), text))
    bad = []
    for tag, raw in re.findall(r"<([a-z][\w:-]*)\b([^>]*)>", markup, re.I):
        tag, found = tag.lower(), attrs(raw)
        for name, value in found.items():
            if name in ("src", "poster", "srcset") or (name == "data" and tag == "object") \
                    or (name in ("href", "xlink:href") and tag in ("link", "image", "use", "feimage")):
                urls = [p.split()[0] for p in value.split(",") if p.strip()] if name == "srcset" else [value]
                bad += [f"<{tag} {name}={u}>" for u in urls
                        if not inline(u) and not (tag == "link" and font_url(u))]
            elif name == "style":
                bad += css_refs(value)
            elif name.startswith("on"):
                bad += re.findall(LOADERS, value)
    for css in re.findall(r"<style\b[^>]*>(.*?)</style>", markup, re.S | re.I):
        bad += css_refs(css)
    for script in scripts:
        bad += re.findall(LOADERS, script)
        # remote URLs a script assigns to a loading attribute or a CSS url()
        bad += [u for u in re.findall(r"(?:\bsrc|\bsrcset|\bposter)\s*=\s*\\?[\"'`]\s*(" + REMOTE + ")", script)
                if not font_url(u)]
        bad += [f"url({u})" for u in re.findall(r"url\(\s*\\?[\"']?(" + REMOTE + ")", script) if not font_url(u)]
    return bad


def reply_panel(raw_attrs: str, inner: str) -> str:
    fields = attrs(raw_attrs)
    label = fields.pop("data-label", "Reply")
    copy = fields.pop("data-copy", "Copy")
    copied = fields.pop("data-copied", "Copied")
    fields.pop("id", None)  # the textarea owns id="reply"
    classes = " ".join(["reply"] + [c for c in fields.pop("class", "").split() if c != "reply"])
    # keep the line structure of any block markup the model put in the reply
    text = re.sub(r"<br\s*/?>|</(?:p|div|li|h[1-6]|tr)>", "\n", inner, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = "\n".join(line.strip() for line in text.splitlines()).strip()
    keep = "".join(f' {k}="{html.escape(v)}"' for k, v in fields.items())
    return (f'<section class="{html.escape(classes)}"{keep}>\n<h2>{html.escape(label)}</h2>\n'
            f'<textarea id="reply" aria-label="{html.escape(label)}">{html.escape(text)}</textarea>\n'
            f'<div class="row"><button type="button" id="copy-reply" data-copied="{html.escape(copied)}">'
            f'{html.escape(copy)}</button></div>\n</section>')


def render(fragment: str, lang: str, artifact: bool) -> str:
    if MARK in fragment:
        raise ValueError("already rendered - edit this page directly, or rewrite the fragment and render again")
    markup = TEXTAREA.sub("", SCRIPT.sub("", fragment))
    if re.search(r"<!doctype|<html\b|<head\b|<body\b", markup, re.I):
        raise ValueError("write a fragment: no <!doctype>, <html>, <head> or <body>")
    title = re.search(r"<title\b[^>]*>(.*?)</title>", fragment, re.S | re.I)
    if not title:
        raise ValueError("start the fragment with <title>...</title>")
    bad = external_refs(fragment)
    if bad:
        raise ValueError("the page must be one self-contained file - inline or remove: "
                         + ", ".join(sorted(set(bad))[:5])
                         + " (loader words such as fetch inside a script's strings are refused too)")
    replies = [m for m in SECTION.finditer(fragment) if "reply" in attrs(m.group(1)).get("class", "").split()]
    if len(replies) != 1:
        raise ValueError('add exactly one <section class="reply">default assembled reply as plain text</section>')
    reply = replies[0]
    if re.search(r"<section\b", reply.group(2), re.I):
        raise ValueError("the reply section holds plain text only - no nested <section>")
    if not re.sub(r"<[^>]+>", "", reply.group(2)).strip():
        raise ValueError("the reply section must hold the default assembled reply (it is what shows with JS off)")

    body = fragment[:reply.start()] + reply_panel(reply.group(1), reply.group(2)) + fragment[reply.end():]
    body = body.replace(title.group(0), "", 1)
    # Move <style> and <link> to the head, but never text that sits inside a script.
    scripts = SCRIPT.findall(body)
    for i, chunk in enumerate(scripts):
        body = body.replace(chunk, f"\x00script{i}\x00", 1)
    styles = re.findall(r"<style\b[^>]*>.*?</style>", body, re.S | re.I)
    links = re.findall(r"<link\b[^>]*>", body, re.I)
    for chunk in styles + links:
        body = body.replace(chunk, "", 1)
    for i, chunk in enumerate(scripts):
        body = body.replace(f"\x00script{i}\x00", chunk, 1)
    body = body.strip()
    css = (ASSETS / "page.css").read_text(encoding="utf-8").strip()
    js = (ASSETS / "page.js").read_text(encoding="utf-8").strip()
    head = "\n".join([f"<title>{title.group(1).strip()}</title>", f"<style>\n{css}\n</style>", *links, *styles])
    main = f'<main class="page" lang="{html.escape(lang)}">\n{body}\n</main>\n<script>\n{js}\n</script>'
    if artifact:
        return f"{head}\n{MARK}\n{main}\n"
    return (f'<!doctype html>\n<html lang="{html.escape(lang)}">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n{head}\n</head>\n'
            f"<body>\n{MARK}\n{main}\n</body>\n</html>\n")


def main() -> int:
    # A Windows console may use cp1252/cp949; a non-ASCII path or message must not crash the run.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description="Wrap a page fragment in the unknowns page template.")
    ap.add_argument("page")
    ap.add_argument("--lang", required=True, help="language of the page's prose (BCP 47, e.g. ko, en)")
    ap.add_argument("--artifact", action="store_true", help="Artifact tool form (no document wrapper)")
    ap.add_argument("--out", help="write here instead of overwriting PAGE")
    args = ap.parse_args()
    src = Path(args.page)
    out = Path(args.out) if args.out else src
    try:
        fragment = src.read_text(encoding="utf-8-sig")
        page = render(fragment, args.lang, args.artifact)
        # LF on every OS, so a page built on Windows is byte-identical to one built elsewhere
        with open(out, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(page)
    except (ValueError, OSError) as err:
        print(f"render-page: {err}", file=sys.stderr)
        return 1
    controls = len(re.findall(r"\bdata-reply\s*=", fragment))
    print(f"render-page: wrote {out} ({len(page.encode('utf-8'))} bytes, {controls} reply controls)")
    if controls == 0:
        print("render-page: warning - no [data-reply] controls, so the reply never changes", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
