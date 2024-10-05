#! /usr/bin/env bash

function abcli_aws_batch_cat() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="seconds=<seconds>,watch"
        abcli_show_usage "@batch cat$ABCUL[$options]$ABCUL<job-id>" \
            "cat <job-id>."
        return
    fi

    local do_watch=$(abcli_option_int "$options" watch 0)

    local job_id=$2

    local command_line"=abcli_aws_batch_browse cat,id=$job_id,log"

    if [[ "$do_watch" == 1 ]]; then
        abcli_watch seconds=20,$options \
            "$command_line"
    else
        abcli_eval ,$options \
            "$command_line"
    fi
}
