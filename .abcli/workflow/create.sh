#! /usr/bin/env bash

function notebooks_and_scripts_workflow_create() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="pattern=$NBS_PATTRENS_LIST$EOP,~upload"
        abcli_show_usage "workflow create$ABCUL$options$ABCUL-|<job-name>$ABCUL<command-line>$EOPE" \
            "create a <pattern> workflow."
        return
    fi

    local do_upload=$(abcli_option_int "$options" upload 1)
    local pattern=$(abcli_option "$options" pattern $NBS_PATTREN_DEFAULT)

    local job_name=$(abcli_clarify_object $2 workflow-$pattern-$(abcli_string_timestamp_short))

    local command_line="${@:3}"
    [[ -z "$command_line" ]] && command_line="$(abcli unquote $NBS_DEFAULT_WORKFLOW_COMMAND)"

    abcli_log "creating workflow: \"$command_line\" -$pattern-> $job_name"

    python3 -m notebooks_and_scripts.workflow \
        create \
        --command_line "$command_line" \
        --job_name $job_name \
        --pattern "$pattern"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    return 0
}
