#! /usr/bin/env bash

function localflow_run() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="dryrun,name=<job-name>"
        abcli_show_usage "localflow run$ABCUL[$options]" \
            "run localflow job."
        return
    fi

    local job_name=$(abcli_option "$options" name)
    [[ -z "$job_name" ]] &&
        job_name=$(localflow_list status=SUBMITTED \
            --log 0 \
            --count 1)
    if [[ -z "$job_name" ]]; then
        abcli_log_error "-localflow: job not found."
        return 1
    fi
    abcli_log "⚙️  $job_name"

    abcli_tag set \
        $job_name \
        ~SUBMITTED,RUNNING \
        validate

    abcli_download - $job_name

    local command_line=$(abcli_metadata get \
        key=command_line,object \
        $job_name)
    if [[ -z "$command_line" ]]; then
        abcli_log_error "-localflow: $job_name: command not found."
        abcli_tag set \
            $job_name \
            ~RUNNING,FAILED \
            validate
        return 1
    fi

    abcli_eval $options, \
        "$command_line"

    abcli_tag set \
        $job_name \
        ~RUNNING,SUCCEEDED \
        validate
}
