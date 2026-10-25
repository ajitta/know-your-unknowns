# Repository guidance

Know Your Unknowns packages eleven skills and two Claude Code agents. The owner writes in Korean; write repository files in English and preserve existing records and translations. README.md and README.ko.md are the only README languages and must keep matching structure.

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

- Source skills live in skills/. Shared references live under skills/loop/references/ and are vendored transitively into generated skills. Deliverables are Markdown in the conversation.
- Claude Code agent sources live in claude-code/agents/. The plugin ships no hooks or executable code. Only Markdown, YAML, JSON, SVG, LICENSE, and NOTICE files are allowed; SVG assets are for the OpenAI listing.
- plugin-manifest.json is the source manifest. packaging/ contains the shipped README and OpenAI interface fields and SVG assets.
- plugins/unknowns/, releases/know-your-unknowns.zip, releases/know-your-unknowns-openai.zip, and plugin-release.json are generated and committed. Edit sources and run tools/package.py; never edit generated output by hand.
- .claude-plugin/marketplace.json points only to ./plugins/unknowns. Tests, docs, and evals stay at the repository root and are never installed.
- Any skill or other shipped content change needs a new plugin version in plugin-manifest.json before release. plugin-release.json enforces a version bump after a recorded build. The initial Phase A migration is bootstrapped at 0.9.2; the owner will bump and release only after all phases and verification are complete. Phase C keeps 0.9.2 and records the changes under Unreleased. During that unreleased transition, remove the record before regenerating changed content to establish the next phase's baseline.
- Follow .claude/rules/skill-writing.md for skill and agent prose. Preserve trigger phrases and method steps.
- Text files use LF. Write UTF-8 bytes or explicitly request LF on Windows. Release zips use ZIP_STORED, fixed timestamps and modes, and Unix create_system for byte reproducibility.
- CI runs ordinary package tests and strict plugin/marketplace validation. Keep build tools portable to Windows and quote paths containing spaces or dollar signs. The scout has only read/search tools; the reviewer can run Bash under a prose-only read-only contract.
- Keep console messages ASCII; configure stdout and stderr with errors="replace" so legacy Windows consoles cannot crash the packager.

## Release

After merging the versioned change with passing CI, an annotated tag unknowns--vX.Y.Z triggers .github/workflows/release.yml. It checks the tag, generated output, tests, and zip manifest versions before attaching both committed zips with release notes from the tag. Never push, tag, or change main unless the user authorizes it.
