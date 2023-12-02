#! /usr/bin/env bash

function runme() {
    local options=$1

    local version="1.4.1"

    local script_name=$(basename "${BASH_SOURCE[0]}")
    local script_name=${script_name%.*}

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="dryrun,~upload"
        local args="[--count <10>]$ABCUL[--height <1024>]$ABCUL[--width <1024>]"
        abcli_script_show_usage "$script_name$ABCUL[$options]$ABCUL<url>$ABCUL[-|<object-name>]$ABCUL$args" \
            "generate mission patches for <url>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $3 $(abcli_string_timestamp))

    abcli_eval dryrun=$do_dryrun \
        python3 -m notebooks_and_scripts.mission_patch \
        generate \
        --url "$2" \
        --object_name $object_name \
        "${@:4}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload object $object_name
}

runme "$@"
