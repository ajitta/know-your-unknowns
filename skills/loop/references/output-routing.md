# Output routing — how to deliver a reactable artifact

Shared by every skill that produces something the user must **look at and react to**
(blindspot, teach-me, prototypes, brainstorm, reference, plan, quiz, buy-in, loop).
The skill bodies carry the 3-line ladder; this file carries the details.

## 1. The ladder (pick the highest rung available)

1. **Artifact tool available** → write the page to a file, publish it with the Artifact
   tool, and give the user the link. Prefer reactions that come back on their own:
   comments, read and answered with the separate `ArtifactComments` tool (the Artifact
   tool itself has no comments action; load `ArtifactComments` first if it is only listed
   as deferred), or the `db` capability for a page that must remember state. Keep the
   copyable assembled reply as the fallback — it costs nothing and works when the user
   would rather paste than comment.
2. **No Artifact tool, but file writes allowed** → write
   `.unknowns/<YYYY-MM-DD>-<skill>-<slug>.html` and tell the user to open it. Offer once
   to add `.unknowns/` to `.gitignore`.
3. **Neither (chat-only, Write denied, or the target is a PR body)** → markdown with the
   same structure and the same reaction prompts.

Which rung is available depends on the surface, not the task; `surfaces.md` in this
folder covers what changes by surface.

**On every rung**: end the turn with the assembled default reply (improved prompt,
requirements list, decision summary) as plain text in the conversation. The artifact is
the reacting surface; the chat message is what survives a closed tab.

## 2. When HTML is worth it

Roughly 5+ reactable items, or any live before/after demo. Below that, markdown in the
conversation is the better deliverable — an HTML file the user must open to read four
bullets costs more than it returns.

## 3. Page contract

Publishing through the Artifact tool: no `<!doctype>`, `<html>`, `<head>` or `<body>`
wrapper — start with `<title>` and `<style>`. Inline all CSS and JS. No external
resources: no CDN scripts, no remote images, no fetch. Fonts may come from
`fonts.googleapis.com`; everything else must be inline or a `data:` URI.

**Language**: write all user-facing prose — cards, questions, prompt drafts, note entries
— in the language the user is writing in. Keep file names, template field keys, and code
identifiers fixed.

**Theme**: define the light palette on bare `:root`, redefine the tokens under
`@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`, and
again under `:root[data-theme="dark"]`. Give `body` an explicit token background. Never
define a color only inside a media or `[data-theme]` block.

**Look**: these pages are working surfaces, not landing pages. With no design direction,
recent models fall back on the same few defaults, and "avoid a generic look" only swaps one
default for another — so name them: no cream or off-white page background, no italic
accent words in headings, no numbered "01 / 02 / 03" section labels, no monospace labels
outside code, no pill-shaped buttons. Let the content's own structure (cards, tables) do
the work.

**Accessibility**: real `<button>` and `<input type="checkbox">` for chips and checkboxes,
never `div` with an onclick. Visible `:focus-visible` styles. Set `lang` to the reply
language. Render the assembled reply as plain text too, so the deliverable survives with
JS off. Respect `prefers-reduced-motion`.

## 4. Reaction-assembly UI

The device that makes the artifact a loop instead of a document: each item carries a
reaction control, and the selections assemble at the bottom into one copyable reply.

Each skill body names its own control and what it assembles into.

Minimal shape: give each item a `data-reply` attribute holding the sentence it
contributes, collect the selected ones in document order, join them into a `<textarea>`,
and put a Copy button next to it.
