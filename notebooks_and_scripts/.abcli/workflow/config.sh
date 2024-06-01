#! /usr/bin/env bash

function notebooks_and_scripts_workflow_config() {
    local options=$1
    local use_cache=$(abcli_option_int "$options" cache 1)

    export NBS_RUNNERS_LIST="aws_batch|generic|local|localflow"
    [[ "$use_cache" == 0 ]] &&
        export NBS_RUNNERS_LIST=$(python3 -m notebooks_and_scripts.workflow.runners list --delim \|)

    export NBS_PATTRENS_LIST="a-bc-d|hourglass|map-reduce"
    [[ "$use_cache" == 0 ]] &&
        export NBS_PATTRENS_LIST=$(python3 -m notebooks_and_scripts.workflow.patterns list --delim \|)

    export NBS_PATTREN_DEFAULT="a-bc-d"
    [[ "$use_cache" == 0 ]] &&
        export NBS_PATTREN_DEFAULT=$(python3 -m notebooks_and_scripts.workflow.patterns list --count 1)
}

notebooks_and_scripts_workflow_config "$@"
