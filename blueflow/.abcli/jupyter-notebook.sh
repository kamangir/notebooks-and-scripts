#! /usr/bin/env bash

function abcli_notebooks() {
    local task=$(abcli_unpack_keyword "$1" open)
    [[ "$task" == "touch" ]] && task="create"

    if [[ "$task" == "init" ]]; then
        notebooks_and_scripts "$@"
        return
    fi

    local function_name=abcli_notebooks_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "@notebooks: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /jupyter-notebook
