#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"
    local script_name=$(abcli_script_get name)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_meta_script_show_usage $script_full_name "$EOP[$vancouver_watching_list_options]$ABCUL$abcli_tag_search_args$EOPE" \
            "vanwatch list, defaults to published ingested objects from vancouver."
        return
    fi

    vancouver_watching_list \
        area=vancouver,ingest,published,$1 \
        "${@:2}"
}

runme "$@"
