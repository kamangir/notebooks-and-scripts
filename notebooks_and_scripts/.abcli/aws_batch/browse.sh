#! /usr/bin/env bash

function abcli_aws_batch_browse() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="cat,id=<job-id>,log"
        abcli_show_usage "@batch browse$ABCUL$options" \
            "browse <job-id>."

        options="queue=<queue-name>,status=$(echo $ABCLI_AWS_BATCH_JOB_STATUS_LIST | tr , \|)"
        abcli_show_usage "@batch browse$ABCUL$options" \
            "browse <queue-name>."

        options="queue=list"
        abcli_show_usage "@batch browse$ABCUL$options" \
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
        local do_log=$(abcli_option "$options" log 0)
        local cat_log=$(abcli_option "$options" cat 0)

        if [[ "$do_log" == 0 ]]; then
            url="$base_url#jobs/detail/$job_id"
        else
            local filename=$abcli_path_temp/$(abcli_string_random).json
            aws batch describe-jobs --jobs $job_id >>$filename

            local log_stream_name=$(python3 -m notebooks_and_scripts.aws_batch \
                get_log_stream_name \
                --filename $filename)
            if [[ -z "$log_stream_name" ]]; then
                abcli_log_error "-@batch: browse: $job_id: log-stream-name not found."
                return 1
            fi
            abcli_log "log stream name: $log_stream_name"

            if [[ "$cat_log" == 0 ]]; then
                log_stream_name=$(python3 -c "from urllib.parse import quote; print(quote('$log_stream_name',safe=''))")
                url="https://ca-central-1.console.aws.amazon.com/cloudwatch/home?region=ca-central-1#logsV2:log-groups/log-group/%2Faws%2Fbatch%2Fjob/log-events/$log_stream_name"
            else
                filename=$abcli_path_temp/$(abcli_string_random).json
                aws logs get-log-events \
                    --log-group-name /aws/batch/job \
                    --log-stream-name $log_stream_name >>$filename
                python3 -m notebooks_and_scripts.aws_batch \
                    cat_log \
                    --filename $filename
                return
            fi
        fi
    fi

    abcli_browse $url
}
