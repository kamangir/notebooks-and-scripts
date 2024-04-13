#! /usr/bin/env bash

export abcli_path_nbs=$abcli_path_git/notebooks-and-scripts

function nbs() {
    notebooks_and_scripts "$@"
}

function notebooks_and_scripts() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        localflow "$@"

        abcli_show_usage "notebooks_and_scripts init [clear]" \
            "init notebooks_and_scripts."

        notebooks_and_scripts_conda "$@"

        local task
        for task in pylint pytest test; do
            notebooks_and_scripts $task "$@"
        done
        return
    fi

    local function_name="notebooks_and_scripts_$task"
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [ "$task" == "init" ]; then
        abcli_init notebooks_and_scripts "${@:2}"
        conda activate notebooks-and-scripts
        return
    fi

    if [[ "|pylint|pytest|test|" == *"|$task|"* ]]; then
        abcli_${task} plugin=notebooks-and-scripts,$2 \
            "${@:3}"
        return
    fi

    if [ "$task" == "version" ]; then
        python3 -m notebooks_and_scripts version "${@:2}"
        return
    fi

    abcli_log_error "-abcli: scripts: $task: command not found."
    return 1
}

abcli_source_path \
    $abcli_path_git/notebooks-and-scripts/.abcli/tests

abcli_env dot load \
    plugin=notebooks-and-scripts
abcli_env dot load \
    filename=config.env,plugin=notebooks-and-scripts
