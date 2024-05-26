#! /usr/bin/env bash

function notebooks_and_scripts_workflow_create() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="pattern=$NBS_PATTRENS_LIST$EOP,~upload"
        abcli_show_usage "workflow create$ABCUL$options$ABCUL.|<job-name>$EOPE" \
            "create a <pattern> workflow."
        return
    fi

    local do_upload=$(abcli_option_int "$options" upload 1)
    local pattern=$(abcli_option "$options" pattern $NBS_PATTREN_DEFAULT)

    local job_name=$(abcli_clarify_object $2 .)

    abcli_log "creating workflow: $pattern -> $job_name"

    python3 -m notebooks_and_scripts.workflow \
        create \
        --job_name $job_name \
        --pattern "$pattern"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    return 0
}
