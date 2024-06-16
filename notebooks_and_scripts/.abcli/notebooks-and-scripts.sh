#! /usr/bin/env bash

export abcli_path_nbs=$abcli_path_git/notebooks-and-scripts

function notebooks_and_scripts() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        abcli_aws_batch "$@"
        abcli_docker "$@"
        notebooks_and_scripts_localflow "$@"
        abcli_notebooks "$@"
        abcli_sagemaker "$@"
        abcli_scripts "$@"
        notebooks_and_scripts_workflow "$@"
        return
    fi

    abcli_generic_task \
        plugin=notebooks_and_scripts,task=$task \
        "${@:2}"
}

abcli_source_path - caller,suffix=/tests

abcli_env dot load \
    plugin=notebooks-and-scripts
abcli_env dot load \
    filename=notebooks_and_scripts/config.env,plugin=notebooks-and-scripts

abcli_log $(notebooks_and_scripts version --show_icon 1)
