#!/usr/bin/env bash
# The bakery pre-order service, in the run's working directory as a git repository: the
# service first, then PLAN.md as the last commit, with fixed authors and dates.
# requirements.txt pins pydantic 1.10.13; PLAN.md names pydantic 2 APIs.
set -eu
here="$(cd "$(dirname "$0")" && pwd)"
export GIT_AUTHOR_NAME="Priya Shah" GIT_AUTHOR_EMAIL="priya@example.invalid"
export GIT_COMMITTER_NAME="Priya Shah" GIT_COMMITTER_EMAIL="priya@example.invalid"
commit() {
  GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1" git -c commit.gpgsign=false commit -q -m "$2"
}
cp -R "$here/files/." .
git init -q
git checkout -q -b main
git -c core.autocrlf=false add -A -- . ':!PLAN.md'
commit 2026-10-12T09:00:00+0000 "Pre-order service: customers and orders"
git -c core.autocrlf=false add PLAN.md
commit 2026-11-06T15:20:00+0000 "Plan request validation for the two unchecked endpoints"
