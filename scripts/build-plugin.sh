#!/bin/sh
# Build the distributable unknowns plugin zip from a tagged, clean commit.
# Usage: scripts/build-plugin.sh [tag]  ->  unknowns-v<version>.plugin (git-ignored)
# Default tag is {name}--v{version}, the form `claude plugin tag` creates.
# Attach the result to the GitHub Release for that tag — never hand out a
# locally built zip.
set -eu
cd "$(dirname "$0")/.."
NAME=$(python3 -c "import json; print(json.load(open('.claude-plugin/plugin.json'))['name'])")
VERSION=$(python3 -c "import json; print(json.load(open('.claude-plugin/plugin.json'))['version'])")
REF=${1:-$NAME--v$VERSION}
OUT="unknowns-v${VERSION}.plugin"

if [ -n "$(git status --porcelain)" ]; then
  echo "refusing to build: working tree is dirty — commit or stash first" >&2
  exit 1
fi
if ! git rev-parse -q --verify "refs/tags/${REF}" >/dev/null; then
  echo "refusing to build: tag '${REF}' does not exist — tag the release first" >&2
  exit 1
fi
TAG_VERSION=$(git show "${REF}:.claude-plugin/plugin.json" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['version'])")
if [ "$TAG_VERSION" != "$VERSION" ]; then
  echo "refusing to build: tag '${REF}' declares version ${TAG_VERSION}, not ${VERSION}" >&2
  exit 1
fi

rm -f "$OUT"
# git archive ships only what the tag tracks — no working-tree drift, no junk files.
git archive --format=zip -o "$OUT" "$REF" -- \
  .claude-plugin skills agents hooks README.md README.ko.md CHANGELOG.md LICENSE NOTICE
echo "built $OUT from tag $REF ($(du -h "$OUT" | cut -f1 | tr -d ' '))"
echo "contents:"
unzip -l "$OUT" | tail -3
