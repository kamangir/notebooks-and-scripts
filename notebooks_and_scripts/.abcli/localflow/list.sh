#! /usr/bin/env bash

function localflow_list() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="status=$(echo $LOCALFLOW_STATUS_LIST | tr , \|)"
        local args=$abcli_tag_search_args
        abcli_show_usage "localflow list$ABCUL[$options]$ABCUL$args" \
            "list localflow jobs."
        return
    fi

    local status=$(abcli_option "$options" status SUBMITTED)

    abcli_tag search \
        localflow,$status \
        --item_name job \
        "${@:2}"
}
