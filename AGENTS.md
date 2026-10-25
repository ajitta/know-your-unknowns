# Repository guidance

Know Your Unknowns packages eleven skills, two Claude Code agents, and two Claude Code hooks. The owner writes in Korean; write repository files in English and preserve existing records and translations. README.md and README.ko.md are the only README languages and must keep matching structure.

## Commands

Run from the repository root:

```bash
python3 tools/package.py
python3 tools/package.py --check
python3 -m unittest discover -s tests -v
claude plugin validate --strict plugins/unknowns
claude plugin validate --strict .
python3 scripts/build-skill-zips.py
```

## Layout and editing rules

- Source skills live in skills/. Shared references, page assets, and the renderer live under skills/loop/ and are vendored transitively into generated skills.
- Claude Code agent and hook sources live in claude-code/agents/ and claude-code/hooks/. Hooks retain paths relative to the installed plugin root.
- plugin-manifest.json is the source manifest. packaging/ contains the shipped README and OpenAI interface fields and SVG assets.
- plugins/unknowns/, releases/know-your-unknowns.zip, releases/know-your-unknowns-openai.zip, and plugin-release.json are generated and committed. Edit sources and run tools/package.py; never edit generated output by hand.
- .claude-plugin/marketplace.json points only to ./plugins/unknowns. Tests, docs, and evals stay at the repository root and are never installed.
- Any skill or other shipped content change needs a new plugin version in plugin-manifest.json before release. plugin-release.json enforces a version bump after a recorded build. The initial Phase A migration is bootstrapped at 0.9.2; the authorized restructure's final version bump is reserved for Phase C. During that unreleased transition, remove the record before regenerating changed content to establish the next phase's baseline.
- Follow .claude/rules/skill-writing.md for skill and agent prose. Preserve trigger phrases and method steps.
- Text files use LF. Write UTF-8 bytes or explicitly request LF on Windows. Release zips use ZIP_STORED, fixed timestamps and modes, and Unix create_system for byte reproducibility.
- Keep both Ubuntu and Windows hook CI jobs. Hook launchers must work in POSIX sh, Git Bash, and PowerShell, probe Python 3 on Windows (python3, python, py -3), and preserve stdin, exit codes, and the read-only guard's onFailure behavior. Keep quoting for plugin paths containing spaces or dollar signs.
- Keep console messages ASCII; configure stdout and stderr with errors="replace" so legacy Windows consoles cannot crash the packager.

## Release

After merging the versioned change with passing CI, an annotated tag unknowns--vX.Y.Z triggers .github/workflows/release.yml. It checks the tag, generated output, tests, and zip manifest versions before attaching both committed zips with release notes from the tag. Never push, tag, or change main unless the user authorizes it.
