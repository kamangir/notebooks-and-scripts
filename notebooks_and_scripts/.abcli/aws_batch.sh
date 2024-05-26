#!/bin/bash

function abcli_aws_batch() {
    local task=$1

    if [ "$task" == "help" ]; then
        abcli_aws_batch_browse "$@"
        abcli_aws_batch_eval "$@"
        abcli_aws_batch_list "$@"
        abcli_aws_batch_submit "$@"
        return
    fi

    local function_name=abcli_aws_batch_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "-@batch: $task: command not found."
    return 1
}

abcli_source_path - caller,suffix=/aws_batch
