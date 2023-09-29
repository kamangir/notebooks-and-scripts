#! /usr/bin/env bash

function vanwatch_ingest_and_analyze() {
    local options=$1

    local script_name=$(basename "${BASH_SOURCE[0]}")
    local script_name=${script_name%.*}

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="$abcli_scripts_options,count=<-1>"
        abcli_show_usage "abcli scripts source $script_name$ABCUL[$options]$ABCUL[<object-name>]$ABCUL[\"$sentence\"]$ABCUL[$args]" \
            "paint a sentence by different artists."
        return
    fi

    rm -v *.jpg
    rm -v *.geojson

    vanwatch ingest vancouver - \
        --count 5
}

vanwatch_ingest_and_analyze "$@"
