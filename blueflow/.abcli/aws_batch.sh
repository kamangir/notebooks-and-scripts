#!/bin/bash

function abcli_aws_batch() {
    local task=$1

    local function_name=abcli_aws_batch_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "@batch: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /aws_batch
