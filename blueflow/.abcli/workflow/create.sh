#! /usr/bin/env bash

function blueflow_workflow_create() {
    local options=$1
    local do_upload=$(abcli_option_int "$options" upload 1)
    local pattern=$(abcli_option "$options" pattern $NBS_PATTREN_DEFAULT)

    local job_name=$(abcli_clarify_object $2 .)

    abcli_log "📜 workflow.create: $pattern -> $job_name"

    python3 -m blueflow.workflow \
        create \
        --job_name $job_name \
        --pattern "$pattern" \
        "${@:3}"
    local status=$?

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    return $status
}
