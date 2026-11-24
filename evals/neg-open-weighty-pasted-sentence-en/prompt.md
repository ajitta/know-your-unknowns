---
description: "Open cell, weighty, with the README's sentence to paste for one conversation (passed as appended system prompt): a clear production migration gets a short read-back and no method; the sentence's end-of-work check is not reached in one turn"
tags: [negative, open-cell, pasted-sentence, en]
runs: 3
max_turns: 6
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
append_system_prompt: "For this conversation: before doing a request whose result carries weight (it ships, is sent or is hard to undo), reply with only a 2-3-line read-back (the request, your assumptions, what counts as done) and wait for my confirmation; just do self-evident requests. When that work is finished, mark each done criterion with its evidence and ask me whether the result achieved the outcome."
---

Add a migration to our Django app that adds a nullable `archived_at` DateTimeField to
`Project`, and change `ProjectQuerySet.active()` so it also excludes projects whose
`archived_at` is set. This goes to production tonight. The current code:

```python
class ProjectQuerySet(models.QuerySet):
    def active(self):
        return self.filter(deleted=False)


class Project(models.Model):
    name = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    objects = ProjectQuerySet.as_manager()
```
