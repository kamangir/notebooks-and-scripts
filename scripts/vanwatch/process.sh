#! /usr/bin/env bash

function runme() {
    local options=$1

    local version="3.1.1"

    local script_name=$(abcli_script_get name)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="${EOP}dryrun$EOPE"
        abcli_script_show_usage "$script_name$ABCUL[$options]$ABCUL[$vancouver_watching_process_options]$ABCUL[.|<object-name>]$EARGS" \
            "process <object-name>."
        return
    fi

    abcli_eval "$options" \
        vancouver_watching_process \
        "${@:2}"
}

runme "$@"
