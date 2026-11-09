#!/usr/bin/env bash
# The league's 22 policy documents, as policies/ in the run's working directory.
set -eu
cp -R "$(dirname "$0")/files/." .
