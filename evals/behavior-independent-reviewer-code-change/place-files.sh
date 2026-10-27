#!/usr/bin/env bash
# The repository under review: the report command and its approved plan, then the
# CSV-export change as the last commit (HEAD~1..HEAD), with fixed authors and dates.
set -eu
here="$(cd "$(dirname "$0")" && pwd)"
export GIT_AUTHOR_NAME="Sam Rivera" GIT_AUTHOR_EMAIL="sam@example.invalid"
export GIT_COMMITTER_NAME="Sam Rivera" GIT_COMMITTER_EMAIL="sam@example.invalid"
commit() {
  cp -R "$here/files/$1/." .
  git -c core.autocrlf=false add -A
  GIT_AUTHOR_DATE="$2" GIT_COMMITTER_DATE="$2" git -c commit.gpgsign=false commit -q -m "$3"
}
git init -q
git checkout -q -b main
commit monthly-report-command 2026-03-28T10:00:00+0000 "Monthly report command and the CSV export plan"
commit add-csv-export 2026-04-04T16:30:00+0000 "Add CSV export to the monthly report"
