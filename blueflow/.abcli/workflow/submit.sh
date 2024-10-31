#! /usr/bin/env bash

function blueflow_workflow_submit() {
    local options=$1
    local do_download=$(abcli_option_int "$options" download 1)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local runner_type=$(abcli_option "$options" to generic)

    local job_name=$(abcli_clarify_object $2 .)

    [[ "$do_download" == 1 ]] &&
        abcli_download - $job_name

    local runner_module="blueflow.workflow.runners"
    if [[ "|$NBS_RUNNERS_LIST|" != *"|$runner_type|"* ]]; then
        abcli_log "external runner: $runner_type"

        local var_name=${runner_type}_runner_module_name
        local runner_module=${!var_name}

        if [[ -z "$runner_module" ]]; then
            abcli_log_error "$runner_type: module not found, try exporting $var_name first."
            return 1
        fi
    fi

    abcli_log "📜 workflow.submit: $job_name -$runner_module-> $runner_type"

    python3 -m $runner_module \
        submit \
        --dryrun $do_dryrun \
        --job_name $job_name \
        --runner_type $runner_type
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    [[ "$status" -ne 0 ]] && return $status

    if [[ "$runner_type" == local ]]; then
        abcli_cat $ABCLI_OBJECT_ROOT/$job_name/$job_name.sh

        abcli_eval dryrun=$do_dryrun \
            source $ABCLI_OBJECT_ROOT/$job_name/$job_name.sh
        status="$?"
    fi

    return $status
}
