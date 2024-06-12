#! /usr/bin/env bash

function abcli_notebooks() {
    local task=$(abcli_unpack_keyword "$1" open)
    [[ "$task" == "touch" ]] && task="create"

    if [ "$task" == "help" ]; then
        abcli_notebooks_open "$@"
        abcli_notebooks_build "$@"
        abcli_notebooks_code "$@"
        abcli_notebooks_connect "$@"
        abcli_notebooks_create "$@"
        abcli_notebooks_host "$@"
        return
    fi

    if [[ "$task" == "init" ]]; then
        notebooks_and_scripts "$@"
        return
    fi

    local function_name=abcli_notebooks_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "-notebooks: $task: command not found."
    return 1
}

abcli_source_path - caller,suffix=/jupyter-notebook
