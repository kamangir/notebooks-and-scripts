#! /usr/bin/env bash

export abcli_path_nbs=$abcli_path_git/notebooks-and-scripts

function nbs() {
    notebooks_and_scripts "$@"
}

function notebooks_and_scripts() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        abcli_show_usage "notebooks_and_scripts init [clear]" \
            "init notebooks_and_scripts."
        return
    fi

    if [ "$task" == "init" ]; then
        abcli_init notebooks_and_scripts "${@:2}"
        return
    fi

    if [ "$task" == "version" ]; then
        python3 -m notebooks_and_scripts version
        return
    fi

    abcli_log_error "-abcli: scripts: $task: command not found."
}
