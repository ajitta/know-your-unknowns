---
description: "Size gate: a one-file change must defer to native plan mode, not produce a tweak-likelihood document"
tags: [negative, conflict, en, plan]
runs: 3
max_turns: 8
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

plan this: add a --verbose flag to backup.py so it prints each file as it is copied.
Here is the whole file — it is about 120 lines and nothing else imports it.

```python
import argparse, shutil
from pathlib import Path

def copy_tree(src: Path, dst: Path) -> int:
    n = 0
    for item in src.rglob("*"):
        if item.is_file():
            target = dst / item.relative_to(src)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)
            n += 1
    return n

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dst")
    a = ap.parse_args()
    print(f"copied {copy_tree(Path(a.src), Path(a.dst))} files")
```
