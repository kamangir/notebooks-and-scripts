#!/bin/bash

function abcli_meta_scripts() {
    local script_name=$1

    if [[ -z "$script_name" ]]; then
        abcli_show_usage "abcli_meta_scripts <script-name>$ABCUL<task> <args>" \
            "::<script-name> <args>."
        return
    fi

    local task=${2:-help}
    if [[ "$task" == help ]]; then
        abcli_scripts list meta $script_name
        return
    fi

    local script_prefix=$(abcli_metadata get \
        $abcli_path_scripts/meta.yaml \
        key=$script_name.prefix,type=file)

    abcli_eval - \
        abcli_scripts source - \
        $script_prefix/$task \
        "${@:3}"
}

function abcli_meta_script_show_usage() {
    local script_fullname=$1

    local task=$(python3 -c "print('$script_fullname'.split('/')[-1].split('.')[0])")
    local meta_script_name=$(python3 -c "print('$script_fullname'.split('/')[-2])")

    abcli_show_usage "$meta_script_name $task$ABCUL$2" \
        "${@:3}"
}
