#!/usr/bin/env bash
# The to-do CLI in the run's working directory. todo.py reads and writes todo.json
# through load() and save(); export.py opens todo.json itself, by name.
set -eu
cp -R "$(dirname "$0")/files/." .
