#! /usr/bin/env bash

function abcli_aws_batch_ls() {
    abcli_aws_batch_list "$@"
}

function abcli_aws_batch_list() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="~count$EOP,dryrun,prefix=<prefix>,status=$(echo $ABCLI_AWS_BATCH_JOB_STATUS_LIST | tr , \|)$EOPE,watch"
        abcli_show_usage "@batch list$ABCUL$options" \
            "list aws batch jobs."
        return
    fi

    if [ $(abcli_option_int "$options" watch 0) == 1 ]; then
        abcli_watch seconds=10 \
            abcli_aws_batch_list ,$options,~watch
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local queue=$(abcli_option "$options" queue abcli-v3)
    local prefix=$(abcli_option "$options" prefix)
    local show_count=$(abcli_option_int "$options" count 1)
    local status=$(abcli_option "$options" status)

    local pipes=""
    [[ ! -z "$prefix" ]] && pipes="| grep $prefix"
    [[ "$show_count" == 1 ]] && pipes="$pipes | wc -l | python3 -m notebooks_and_scripts.aws_batch show_count"

    [[ -z "$status" ]] && status=$(echo $ABCLI_AWS_BATCH_JOB_STATUS_LIST_WATCH | tr , " ")

    abcli_log "queue: $queue"
    local status_
    for status_ in $status; do
        [[ "$show_count" == 1 ]] && abcli_log "status: $status_"
        abcli_eval dryrun=$do_dryrun,log=$(abcli_not $show_count) \
            "aws batch list-jobs \
                --job-status $status_ \
                --job-queue $queue \
                --output text \
                $pipes"
    done
}
