#! /usr/bin/env bash

export abcli_path_scripts=$abcli_path_git/notebooks-and-scripts/scripts

function scripts() {
    abcli_scripts "$@"
}

export abcli_scripts_options=cat

function abcli_scripts() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        notebooks_and_scripts version \\n

        abcli_show_usage "abcli scripts cat$ABCUL[<script-name>]" \
            "cat <script-name>."

        abcli_show_usage "abcli scripts help$ABCUL[<script-name>]" \
            "help <script-name>."

        abcli_show_usage "abcli scripts list" \
            "list scripts."

        abcli_show_usage "abcli scripts source$ABCUL<script-name>$ABCUL[$abcli_scripts_options]$ABCUL<args>" \
            "source <script-name>."
        return
    fi

    local function_name=abcli_scripts_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name ${@:2}
    fi

    if [[ ",cat,help,source,ls,list," == *",$task,"* ]]; then
        local script_path=$abcli_path_scripts
        local suffix=$2
        [[ ! -z "$suffix" ]] && local path=$script_path/$suffix
        [[ -f "$script_path.sh" ]] && local path=$script_path.sh
    fi

    if [ "$task" == "cat" ]; then
        abcli_log_file $script_path
        return
    fi

    if [[ ",ls,list," == *",$task,"* ]]; then
        if [[ -f "$script_path" ]]; then
            abcli_log_file $script_path
        else
            abcli_log "🔗 $script_path"
            ls -1lh $script_path \
                "${@:3}"
        fi

        return
    fi

    if [ "$task" == "help" ]; then
        abcli_scripts source \
            $script_path \
            help
        return
    fi

    if [ "$task" == "source" ]; then
        local options=$3

        if [[ ! -f "$script_path" ]]; then
            abcli_log_error "-abcli: scripts: $task: $script_path: script not found."
            return 1
        fi

        do_cat=$(abcli_option "$options" cat 0)

        [[ "$do_cat" == 1 ]] && abcli_log_file $script_path

        chmod +x $script_path
        source $script_path "${@:3}"
        return
    fi

    abcli_log_error "-abcli: scripts: $task: command not found."
}
