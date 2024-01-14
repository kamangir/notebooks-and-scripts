#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="${EOP}dryrun$EOPE"
        local ingest_options="count=<-1>,publish$EOP,dryrun$EOPE"
        abcli_meta_script_show_usage $script_full_name "[$options]$ABCUL[$ingest_options]$ABCUL[-|<object-name>]$EARGS" \
            "vanwatch ingest, defaults to Vancouver."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local ingest_options=$2

    local object_name=$(abcli_clarify_object $3 $(abcli_string_timestamp))

    abcli_eval dryrun=$do_dryrun \
        vancouver_watching_ingest \
        area=vancouver,count=10,$ingest_options \
        $object_name \
        "${@:4}"
}

runme "$@"
