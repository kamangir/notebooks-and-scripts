#! /usr/bin/env bash

function localflow_eval() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="name=<job-name>"
        abcli_show_usage "localflow eval|submit$ABCUL[$options]$ABCUL<command-line>" \
            "eval <command-line> through localflow."
        return
    fi

    local job_name=$(abcli_option "$options" name $(abcli_string_timestamp))

    local command_line="${@:2}"
    abcli_metadata post \
        command_line "$command_line" \
        object $job_name

    abcli_upload - $job_name

    abcli_tag set \
        $job_name \
        localflow,SUBMITTED \
        validate
}

function localflow_evaluate() {
    localflow_eval "$@"
}

function localflow_submit() {
    localflow_eval "$@"
}
