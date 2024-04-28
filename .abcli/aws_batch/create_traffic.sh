#! /usr/bin/env bash

function abcli_aws_batch_create_traffic() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        list_of_patterns=$(python3 -m notebooks_and_scripts.aws_batch list_of_patterns --delim \|)
        options="~dryrun,pattern=$list_of_patterns,name=<job-name>,~upload,~verbose"
        abcli_show_usage "@batch create_traffic$ABCUL[$options]$ABCUL<command-line>" \
            "create <command-line> traffic in aws batch."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 1)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local do_verbose=$(abcli_option_int "$options" verbose 1)

    local pattern=$(python3 -m notebooks_and_scripts.aws_batch list_of_patterns --count 1)
    pattern=$(abcli_option "$options" pattern $pattern)

    local job_name=traffic-$(abcli_string_timestamp)
    job_name=$(abcli_option "$options" job_name $job_name)

    local command_line="${@:2}"
    [[ -z "$command_line" ]] && command_line="$(abcli unquote $ABCLI_AWS_BATCH_DEFAULT_TRAFFIC_COMMAND)"

    abcli_log "creating aws-batch traffic: $command_line -$pattern-> $job_name"

    python3 -m notebooks_and_scripts.aws_batch \
        create_traffic \
        --command_line "$command_line" \
        --pattern "$pattern" \
        --job_name $job_name \
        --verbose $do_verbose \
        --dryrun $do_dryrun

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name
}
