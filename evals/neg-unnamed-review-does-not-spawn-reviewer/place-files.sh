#!/usr/bin/env bash
# The repository under review: a small to-do CLI on main, then the due-dates feature as
# one commit on feature/due-dates, which stays checked out, with fixed authors and dates.
# In that commit, overdue() keeps tasks due after today, not before.
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
commit main 2026-03-02T09:00:00+0000 "To-do list CLI"
git checkout -q -b feature/due-dates
commit due-dates 2026-03-09T15:20:00+0000 "Add due dates and list --overdue"
