#! /usr/bin/env bash

function runme() {
    local options=$1

    local version="1.6.1"

    local script_name=$(abcli_name_of_script "${BASH_SOURCE[0]}")
    local script_path=$(dirname "${BASH_SOURCE[0]}")

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="${EOP}dryrun$EOPE"
        local ingest_options="count=<-1>$EOP,dryrun$EOPE"
        abcli_script_show_usage "$script_name$ABCUL[$options]$ABCUL[$ingest_options]$ABCUL[-|<object-name>]$EARGS" \
            "vanwatch ingest, defaults to Vancouver."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local ingest_options=$2

    local object_name=$(abcli_clarify_object $3 $(abcli_string_timestamp))
    local object_path=$abcli_object_root/$object_name
    mkdir -p $object_path
    rm -v $object_path/*.jpg
    rm -v $object_path/*.geojson

    abcli_eval dryrun=$do_dryrun \
        vanwatch ingest \
        area=vancouver,count=10,$ingest_options \
        $object_name \
        "${@:4}"
}

runme "$@"
