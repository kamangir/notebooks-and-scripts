#!/bin/bash

export ABCLI_AWS_BATCH_JOB_STATUS_LIST="SUBMITTED|PENDING|RUNNABLE|STARTING|RUNNING|SUCCEEDED|FAILED"

function abcli_aws_batch() {
    local task=${1:-help}

    if [ "$task" == "help" ]; then
        abcli_aws_batch browse "$@"
        abcli_aws_batch list "$@"
        abcli_aws_batch source "$@"
        return
    fi

    local options=$2
    local status=$(abcli_option "$options" status)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="$EOP,dryrun$EOPE"
        case "$task" in
        browse)
            abcli_show_usage "abcli aws_batch browse$ABCUL[id=<job-id>]" \
                "browse <job-id>."

            abcli_show_usage "abcli aws_batch browse$ABCUL[queue=<queue-name>,status=$ABCLI_AWS_BATCH_JOB_STATUS_LIST]" \
                "browse <queue-name>."

            abcli_show_usage "abcli aws_batch browse$ABCUL[queue=list]" \
                "browse list of queues."
            ;;
        list | ls)
            options="~count,prefix=<prefix>$options"
            abcli_show_usage "abcli aws_batch list$ABCUL[$options]" \
                "list aws_batch jobs."
            ;;
        source | submit)
            options="$abcli_scripts_options,name=<job-name>"
            abcli_show_usage "abcli aws_batch source$ABCUL[$options]$ABCUL<script-name>$ABCUL[<args>]" \
                "source <script-name> in aws_batch."
            ;;
        *)
            abcli_log_error "-abcli: aws_batch: $task: help: command not found."
            return 1
            ;;
        esac
        return
    fi

    if [[ "|browse|list|ls|" == *"|$task|"* ]]; then
        local queue=$(abcli_option "$options" queue abcli-v3)
    fi

    if [ "$task" == "browse" ]; then
        local url

        local aws_region=$(aws configure get region)
        local base_url="https://$aws_region.console.aws.amazon.com/batch/home?region=$aws_region"

        local job_id=$(abcli_option "$options" id)
        if [ -z "$job_id" ]; then
            if [[ "$queue" == list ]]; then
                url="$base_url#queues"
            else
                [[ -z "$status" ]] && status=SUBMITTED
                url="$base_url#jobs/$queue/$status"
            fi
        else
            url="$base_url#jobs/detail/$job_id"
        fi

        abcli_browse_url $url
        return
    fi

    if [[ "|list|ls|" == *"|$task|"* ]]; then
        local prefix=$(abcli_option "$options" prefix)
        local show_count=$(abcli_option_int "$options" count 1)

        local pipes=""
        [[ ! -z "$prefix" ]] && local pipes="| grep $prefix"
        [[ "$show_count" == 1 ]] && local pipes="$pipes | wc -l | python3 -m notebooks_and_scripts.aws_batch show_count"

        [[ -z "$status" ]] && local status=$(echo $ABCLI_AWS_BATCH_JOB_STATUS_LIST | tr \| " ")

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

        return
    fi

    if [[ "|source|submit|" == *"|$task|"* ]]; then
        local job_name=$(echo $3 | tr . - | tr / -)-$(abcli_string_timestamp)
        job_name=abcli-$(abcli_option "$options" name $job_name)

        abcli_eval dryrun=$do_dryrun \
            python3 -m notebooks_and_scripts.aws_batch \
            submit \
            --command_line \"${@:2}\" \
            --job_name "$job_name"

        return
    fi

    abcli_log_error "-abcli: aws_batch: $task: command not found."
}
