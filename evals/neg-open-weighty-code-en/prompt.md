---
description: "Open cell, weighty: a clear production migration gets a short read-back and no method"
tags: [negative, open-cell, en]
runs: 3
max_turns: 6
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
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
