#! /usr/bin/env bash

export NBS_RUNNERS_LIST=$(python3 -m blueflow.workflow.runners list --delim \|)

export NBS_PATTRENS_LIST=$(python3 -m blueflow.workflow.patterns list --delim \|)

export NBS_PATTREN_DEFAULT=$(python3 -m blueflow.workflow.patterns list --count 1)
