#! /usr/bin/env bash

function abcli_aws_batch_cat() {
    local job_id=$1

    if [[ "$job_id" == "help" ]]; then
        abcli_show_usage "@batch cat$ABCUL<job-id>" \
            "cat <job-id>."
        return
    fi

    abcli_aws_batch_browse \
        cat,id=$job_id,log,$2 \
        "${@:3}"
}
