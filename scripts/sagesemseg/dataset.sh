#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"
    local script_name=$(abcli_script_get name)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="-"
        abcli_meta_script_show_usage $script_full_name "$options$EARGS" \
            "<description>."
        return
    fi

    echo "wip 🪄"

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local on_batch=$(abcli_option_int "$options" batch 1)
    local do_publish=$(abcli_option_int "$options" publish 1)

}

runme "$@"
