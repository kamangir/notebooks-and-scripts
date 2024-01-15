#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"
    local script_name=$(abcli_script_get name)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="${EOP}dryrun$EOPE"
        abcli_meta_script_show_usage $script_full_name "[$options]$ABCUL[$EOP$vancouver_watching_process_options$EOPE]$ABCUL[.|all|<object-name>]$EARGS" \
            "process <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local process_options=$2

    local object_name=$(abcli_clarify_object $3 .)

    if [[ "$object_name" == all ]]; then
        local published_object_name
        for published_object_name in $(abcli_tag search \
            ingest,published,$area,vancouver_watching \
            --log 0 \
            --delim space); do
            abcli_aws_batch source \
                name=$published_object_name-vanwatch-process-$(abcli_string_timestamp),dryrun=$do_dryrun \
                $script_name \
                $process_options, \
                $published_object_name \
                "${@:4}"
        done
        return
    fi

    abcli_eval "$options" \
        vancouver_watching_process \
        "$process_options" \
        $object_name \
        "${@:4}"
}

runme "$@"