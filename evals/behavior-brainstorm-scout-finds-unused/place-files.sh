#!/usr/bin/env bash
# The helpdesk repository, in the run's working directory: the app's modules, its tests,
# and legacy/autotriage/, a working keyword triage and canned-reply module nothing imports.
set -eu
cp -R "$(dirname "$0")/files/." .
