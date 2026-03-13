#!/bin/bash
set -xe
FILESPEC=(
   jobrunner_git
)
ruff check --fix "${FILESPEC[@]}"
ruff format "${FILESPEC[@]}"
mypy --strict "${FILESPEC[@]}"
