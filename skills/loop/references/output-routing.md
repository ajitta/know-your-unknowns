# Output routing — how to deliver a reactable artifact

Shared by every skill that produces something the user must **look at and react to** (blindspot, teach-me, prototypes, brainstorm, reference, plan, quiz, buy-in, loop). The skill bodies carry the 3-line ladder; this file carries the details.

## 1. The ladder (pick the highest rung available)

1. **Artifact tool available** →

   a. Write the page to a file (built per §3), publish it with the Artifact tool, and give the user the link.

   b. Prefer reactions that come back on their own: comments, read and answered with the separate `ArtifactComments` tool, or the `db` capability for a page that must remember state. The Artifact tool itself has no comments action. When `ArtifactComments` is only listed as deferred, load it first.

   c. Keep the copyable assembled reply as the fallback — it costs nothing and works when the user would rather paste than comment.

2. **No Artifact tool, but file writes allowed** →

   a. Write `.unknowns/<YYYY-MM-DD>-<skill>-<slug>.html` (built per §3) and tell the user to open it.

   b. Offer once to add `.unknowns/` to `.gitignore`.

3. **Neither (chat-only, Write denied, or the target is a PR body)** → markdown with the same structure and the same reaction prompts.

Which rung is available is a property of the surface, not of the task: Claude Code and Cowork reach rung 1 or 2, Desktop and web chat usually reach rung 1, mobile is rung 3. `surfaces.md` in this folder covers the rest of what changes by surface.

**On every rung**: end the turn with the assembled default reply (improved prompt, requirements list, decision summary) as plain text in the conversation. The artifact is the reacting surface; the chat message is what survives a closed tab.

## 2. When HTML is worth it

Roughly 5+ reactable items, or any live before/after demo. Below that, markdown in the conversation is the better deliverable: an HTML file the user must open to read four bullets costs more than it returns.

## 3. Build the page from the template

The theme, accessibility and reply-assembly code is the same on every page, so it lives in `${CLAUDE_PLUGIN_ROOT}/skills/loop/assets/` and you write only the page's content.

1. Write a **fragment** to the page's path (`.unknowns/<YYYY-MM-DD>-<skill>-<slug>.html`, or any file you will publish):

   a. Start with `<title>`. No `<!doctype>`, `<html>`, `<head>` or `<body>`, no theme CSS, no reply-assembly script.

   b. Build the content from the classes and attributes in §4.

   c. End with one `<section class="reply">` holding the default assembled reply as plain text.

2. Run `python3 "${CLAUDE_PLUGIN_ROOT}/skills/loop/scripts/render-page.py" "<path>" --lang <reply language>`, with both paths quoted. Add `--artifact` when the page goes to the Artifact tool. The script wraps the fragment in place, inlining `page.css` and `page.js`. No `python3` command (common on Windows) → run the same line with `py -3` or `python` in its place.
3. When the script exits non-zero, fix what it names in the fragment and run it again. To change a page after it is rendered, edit the rendered file directly.

This section and §4 are the whole interface. Do not read `page.css`, `page.js` or `render-page.py` before writing the fragment; read them only for the fallback below.

No shell tool (Bash or PowerShell) or no Python 3 → Read `assets/page.css` and `assets/page.js`, then write the whole page yourself: those two files inlined unchanged in `<style>` and `<script>`, the fragment wrapped in `<main class="page" lang="…">`, and the reply section expanded to the shape the script produces (an `<h2>`, `<textarea id="reply">` holding the default reply, `<button type="button" id="copy-reply">`). Publishing through the Artifact tool: no `<!doctype>`, `<html>`, `<head>` or `<body>` wrapper — start with `<title>` and `<style>`.

Generating the shared code on every page costs output tokens and lets it drift between pages; the script makes it a fixed copy and checks the rules below mechanically.

**Rules the script enforces**: no external resources (no CDN scripts, no remote images, no `fetch`; fonts may come from `fonts.googleapis.com`, everything else inline or a `data:` URI), a `<title>`, and exactly one non-empty reply section. Plain `<a href>` links to sources are fine.

**Language**: write all user-facing prose — cards, questions, prompt drafts, note entries, the reply section's labels — in the language the user is writing in, and pass that language to `--lang`. Keep file names, template field keys, and code identifiers fixed.

**Custom styles and scripts** (live demos, sliders, mockups): put them in the fragment's own `<style>` and `<script>`. Use the color tokens (`--bg`, `--fg`, `--muted`, `--line`, `--card`, `--accent`, `--accent-fg`, `--ok`, `--bad`, `--warn`), never a hard-coded color, so dark mode keeps working. A custom control that changes the reply calls `window.unknownsReply()`.

**Look**: these pages are working surfaces, not landing pages. Leave out these defaults in the content and in custom styles:

- no cream or off-white page background
- no italic accent words in headings
- no numbered "01 / 02 / 03" section labels
- no monospace labels outside code
- no pill-shaped buttons

Let the content's own structure (cards, tables) do the work. The defaults are named one by one because, with no design direction, recent models fall back on the same few defaults, and "avoid a generic look" only swaps one default for another.

**Accessibility**: real `<button>` and `<input type="checkbox">` for chips and checkboxes, never `div` with an onclick. The template already supplies `:focus-visible` styles, `prefers-reduced-motion`, the light and dark themes, and the JS-off reply text.

## 4. Reaction-assembly UI

Each item carries a reaction control, and the selections assemble at the bottom into one copyable reply. Each skill body names its own control and what it assembles into. `page.js` does the assembly: it reads every control with a `data-reply` attribute, in document order.

| Control | Markup | Adds to the reply |
|---|---|---|
| Checkbox (resonate, include, sign-off) | `<label class="pick"><input type="checkbox" data-reply="sentence"> label</label>` | its `data-reply` when checked |
| Chip row, one pick (A/B/C) | `<div class="choices"><button data-reply="sentence">A</button>…</div>` | the pressed button's `data-reply` |
| Chip row, several picks | `<div class="choices" data-multi>…</div>` | every pressed button's `data-reply` |
| Self-graded question | `<div class="choices" data-answer="B" data-goto="#change-site"><button data-value="B" data-reply="Q1: B">…</button>…</div>`, an optional `<p class="explain">` beside it, and `<span data-score></span>` anywhere | the picked answer with ✓ or ✗, plus the score line; a wrong pick scrolls to `data-goto` |
| Text box, slider, select | `<textarea data-reply="Label">` / `<input type="range" data-reply="Label">` | `Label: value` once the user changes it |

Reply section: `<section class="reply" data-label="…" data-copy="…" data-copied="…" data-head="…" data-foot="…" data-score-label="…">default reply</section>`. Every attribute is optional; write the labels in the reply language. `data-head` and `data-foot` frame the assembled lines; with nothing selected the default reply comes back.

Layout classes: `.grid` of `.card`s, `.compare` for a two-column before/after, `.tag` (with `.ok`, `.bad` or `.warn`) for a status label, `.lead` and `.meta` for secondary text, plain `<table>` for specs.

This UI is what makes the artifact a loop instead of a document.
