#! /usr/bin/env bash

function runme() {
    local options=$1

    local version="3.2.1"

    local script_name=$(abcli_script_get name)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="${EOP}dryrun$EOPE"
        abcli_script_show_usage "$script_name$ABCUL[$options]$ABCUL[$EOP$vancouver_watching_process_options$EOPE]$ABCUL[.|<object-name>]$EARGS" \
            "process <object-name>."
        return
    fi

    local process_options=$2

    local object_name=$(abcli_clarify_object $3 .)

    abcli_eval "$options" \
        vancouver_watching_process \
        "$process_options" \
        $object_name \
        "${@:4}"
}

runme "$@"
