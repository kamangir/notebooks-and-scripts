#! /usr/bin/env bash

function vanwatch_ingest_and_analyze() {
    local options=$1

    local version="1.1.1"

    local script_name=$(basename "${BASH_SOURCE[0]}")
    local script_name=${script_name%.*}

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="count=<-1>,dryrun,upload"
        abcli_script_show_usage "$script_name$ABCUL[$options]$ABCUL[<object-name>]$ABCUL[<args>]" \
            "ingest from traffic cameras and analyze, version $version."
        return
    fi

    local count=$(abcli_option "$options" count 10)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 0)

    local object_name=$(abcli_clarify_object $2 .)
    abcli_select $object_name

    rm -v *.jpg
    rm -v *.geojson

    abcli_eval dryrun=$do_dryrun \
        vancouver_watching ingest vancouver \
        upload=$do_upload \
        --count $count \
        "${@:3}"
}

vanwatch_ingest_and_analyze "$@"
