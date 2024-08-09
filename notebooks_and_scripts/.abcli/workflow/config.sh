#! /usr/bin/env bash

export NBS_RUNNERS_LIST=$(python3 -m notebooks_and_scripts.workflow.runners list --delim \|)

export NBS_PATTRENS_LIST=$(python3 -m notebooks_and_scripts.workflow.patterns list --delim \|)

export NBS_PATTREN_DEFAULT=$(python3 -m notebooks_and_scripts.workflow.patterns list --count 1)
