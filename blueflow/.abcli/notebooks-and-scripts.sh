#! /usr/bin/env bash

export abcli_path_nbs=$abcli_path_git/notebooks-and-scripts

export notebooks_and_scripts_module_name=blueflow

function notebooks_and_scripts() {
    local task=$(abcli_unpack_keyword $1 version)

    abcli_generic_task \
        plugin=notebooks_and_scripts,task=$task \
        "${@:2}"
}

abcli_source_caller_suffix_path /tests

abcli_env_dot_load \
    caller,ssm,plugin=notebooks_and_scripts,suffix=/../..

abcli_env_dot_load \
    caller,filename=config.env,suffix=/..

abcli_log $(notebooks_and_scripts version --show_icon 1)
