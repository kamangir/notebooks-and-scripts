#! /usr/bin/env bash

function notebooks_and_scripts_workflow_create() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        list_of_patterns=$(python3 -m notebooks_and_scripts.aws_batch list_of_patterns --delim \|)
        options="~dryrun,pattern=$list_of_patterns,name=<job-name>|.,~upload,~verbose"
        abcli_show_usage "@workflow create$ABCUL[$options]$ABCUL<command-line>" \
            "create a <command-line> workflow."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 1)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local do_verbose=$(abcli_option_int "$options" verbose 1)

    local pattern=$(python3 -m notebooks_and_scripts.workflow.patterns list --count 1)
    pattern=$(abcli_option "$options" pattern $pattern)

    local job_name=traffic-$(abcli_string_timestamp)
    job_name=$(abcli_option "$options" name $job_name)
    job_name=$(abcli_clarify_object $job_name)

    local command_line="${@:2}"
    [[ -z "$command_line" ]] && command_line="$(abcli unquote $ABCLI_AWS_BATCH_DEFAULT_TRAFFIC_COMMAND)"

    abcli_log "creating workflow: $command_line -$pattern-> $job_name"

    python3 -m notebooks_and_scripts.aws_batch \
        create_traffic \
        --command_line "$command_line" \
        --pattern "$pattern" \
        --job_name $job_name \
        --verbose $do_verbose \
        --dryrun $do_dryrun

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    return 0
}
