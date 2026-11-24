#!/usr/bin/env bash
# The meal-kit platform's monorepo, in the run's working directory as a git repository:
# 41 services written from the templates in templates/service/ (one line each in
# templates/services.txt), then the hand-written files in files/ on top of them.
# Three mechanisms bear on failed renewal payments and none is in use:
#   libs/dunning/ - a retry schedule for declined charges that no service imports
#     (payments retries once after 24 hours, then cancels);
#   the payment_failed handler in services/notifications/handlers.py - subscribed to
#     "payment.failed", an event nothing publishes (payments publishes "charge.declined");
#   services/payments/card_updater.py - the processor's account updater, run by
#     services/payments/jobs.py only when card_updater_enabled, false since a commit of
#     February 2025.
# Three commits with fixed authors and dates: the platform, libs/dunning, the flag off.
set -eu
here="$(cd "$(dirname "$0")" && pwd)"
shopt -u patsub_replacement 2>/dev/null || true

parts=(__init__.py models.py repository.py schemas.py service.py api.py client.py
       config.yaml README.md RUNBOOK.md migration.sql test_service.py test_api.py)
texts=()
for part in "${parts[@]}"; do
  if [ "$part" = "__init__.py" ]; then
    texts+=('"""@TITLE@ service."""')
  else
    texts+=("$(cat "$here/templates/service/$part.tmpl")")
  fi
done

n=0
while IFS='|' read -r svc class title event plural field1 field2 team purpose; do
  [ -n "$svc" ] || continue
  n=$(( n + 1 ))
  port=$(( 8100 + n ))
  route="${svc//_/-}"
  dir="services/$svc"
  mkdir -p "$dir/tests" "$dir/migrations"
  : > "$dir/tests/__init__.py"
  for ((k = 0; k < ${#parts[@]}; k++)); do
    case "${parts[$k]}" in
      migration.sql) out="$dir/migrations/0001_create_$svc.sql" ;;
      test_*) out="$dir/tests/${parts[$k]}" ;;
      *) out="$dir/${parts[$k]}" ;;
    esac
    text="${texts[$k]}"
    text="${text//@SVC@/$svc}"
    text="${text//@CLASS@/$class}"
    text="${text//@TITLE@/$title}"
    text="${text//@EVENT@/$event}"
    text="${text//@PLURAL@/$plural}"
    text="${text//@FIELD1@/$field1}"
    text="${text//@FIELD2@/$field2}"
    text="${text//@TEAM@/$team}"
    text="${text//@PURPOSE@/$purpose}"
    text="${text//@PORT@/$port}"
    text="${text//@ROUTE@/$route}"
    printf '%s\n' "$text" > "$out"
  done
done < "$here/templates/services.txt"

cp -R "$here/files/." .
cp "$here/templates/payments-config-2024.yaml" services/payments/config.yaml

export GIT_AUTHOR_NAME="Sam Okafor" GIT_AUTHOR_EMAIL="sam@example.invalid"
export GIT_COMMITTER_NAME="Sam Okafor" GIT_COMMITTER_EMAIL="sam@example.invalid"
commit() {
  GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1" git -c commit.gpgsign=false commit -q -m "$2"
}
git init -q
git checkout -q -b main
git -c core.autocrlf=false add -A -- . ':!libs/dunning'
commit 2024-05-02T10:00:00+0000 "Platform services and shared libraries"
git -c core.autocrlf=false add libs/dunning
commit 2024-06-14T16:40:00+0000 "Add a dunning schedule for the payments rewrite"
cp "$here/files/services/payments/config.yaml" services/payments/config.yaml
git -c core.autocrlf=false add services/payments/config.yaml
commit 2025-02-11T09:15:00+0000 "Turn off the card updater for the processor migration"
