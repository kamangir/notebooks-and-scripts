#! /usr/bin/env bash

function ukraine_timemap_ingest() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="${EOP}dryrun,~upload$EOPE"
        local open_options="open,QGIS"
        abcli_show_usage "ukraine_timemap ingest$ABCUL$options$ABCUL-$EOP|<object-name>$EOPE$ABCUL$open_options" \
            "ingest the latest dataset from https://github.com/bellingcat/ukraine-timemap."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 ukraine-timemap-$(abcli_string_timestamp_short))

    abcli_clone \
        $UKRAINE_TIMEMAP_TEMPLATE \
        $object_name \
        ~meta
    rm -v \
        $abcli_object_root/$object_name/ukraine_timemap.*

    abcli_eval dryrun=$do_dryrun \
        python3 -m notebooks_and_scripts.ukraine_timemap \
        ingest \
        --object_name $object_name \
        "${@:3}"

    abcli_tag set \
        $object_name \
        ukraine_timemap_ingest

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    local open_options=$3
    local do_open=$(abcli_option_int "$open_options" open 0)
    [[ "$do_open" == 1 ]] &&
        abcli_open $object_name \
            $open_options

    return 0
}
