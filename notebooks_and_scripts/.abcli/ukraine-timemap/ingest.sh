#! /usr/bin/env bash

function ukraine_timemap_ingest() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="dryrun,~upload"
        abcli_show_usage "ukraine_timemap ingest$ABCUL[$options]$ABCUL[-|<object-name>]" \
            "ingest the latest dataset from https://github.com/bellingcat/ukraine-timemap."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 ukraine-timemap-$(abcli_string_timestamp_short))

    abcli_eval dryrun=$do_dryrun \
        python3 -m notebooks_and_scripts.ukraine_timemap \
        ingest \
        --object_name $object_name \
        "${@:3}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}
