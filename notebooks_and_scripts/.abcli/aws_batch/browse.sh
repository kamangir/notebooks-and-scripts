#! /usr/bin/env bash

function abcli_aws_batch_browse() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="id=<job-id>"
        abcli_show_usage "@batch browse $options" \
            "browse <job-id>."

        options="queue=<queue-name>,status=$(echo $ABCLI_AWS_BATCH_JOB_STATUS_LIST | tr , \|)"
        abcli_show_usage "@batch browse$ABCUL$options" \
            "browse <queue-name>."

        options="queue=list"
        abcli_show_usage "@batch browse $options" \
            "browse list of queues."
        return
    fi

    local queue=$(abcli_option "$options" queue abcli-v3)
    local job_id=$(abcli_option "$options" id)
    local status=$(abcli_option "$options" status)

    local aws_region=$(aws configure get region)
    local base_url="https://$aws_region.console.aws.amazon.com/batch/home?region=$aws_region"

    local url
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

    abcli_browse $url
}
