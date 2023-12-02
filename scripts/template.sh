#! /usr/bin/env bash

function runme() {
    local options=$1

    local version="1.1.1"

    local script_name=$(basename "${BASH_SOURCE[0]}")
    local script_name=${script_name%.*}

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="~download,dryrun,~upload"
        abcli_script_show_usage "$script_name$ABCUL[$options]$ABCUL[<object-name>]$ABCUL[<args>]" \
            "magic 🪄."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download object $object_name

    abcli_eval dryrun=$do_dryrun \
        abcli_list cloud \
        "$object_name" \
        "${@:3}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload object $object_name
}

runme "$@"