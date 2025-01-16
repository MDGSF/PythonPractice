#!/usr/bin/env bash

set -o pipefail
set -o nounset
set -o errexit

export PYTHONPATH=$PYTHONPATH:$PWD

mypy demo01.py
