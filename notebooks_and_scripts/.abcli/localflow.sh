#! /usr/bin/env bash

function notebooks_and_scripts_localflow() {
    localflow "$@"
}

function localflow() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        localflow_eval "$@"
        localflow_list "$@"
        localflow_run "$@"
        return
    fi

    local function_name=localflow_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "-localflow: $task: command not found."
    return 1
}

abcli_source_path - caller,suffix=/localflow
