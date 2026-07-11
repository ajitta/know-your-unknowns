#!/bin/sh
# Build the distributable unknowns.plugin zip, version-stamped from plugin.json.
# Usage: scripts/build-plugin.sh  ->  unknowns-v<version>.plugin (git-ignored)
set -eu
cd "$(dirname "$0")/.."
VERSION=$(python3 -c "import json; print(json.load(open('.claude-plugin/plugin.json'))['version'])")
OUT="unknowns-v${VERSION}.plugin"
rm -f "$OUT"
zip -qr "$OUT" \
  .claude-plugin skills agents hooks README.md README.ko.md CHANGELOG.md LICENSE \
  -x '*.DS_Store'
echo "built $OUT ($(du -h "$OUT" | cut -f1 | tr -d ' '))"
echo "contents:"
unzip -l "$OUT" | tail -3
