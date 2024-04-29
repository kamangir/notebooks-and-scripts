#! /usr/bin/env bash

function abcli_aws_batch_monitor() {
    abcli_aws_batch_monitor_traffic "$@"
}

function abcli_aws_batch_monitor_traffic() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="$EOP~download,${EOPE}name=<job-name>$EOP,~upload$EOPE"
        abcli_show_usage "@batch monitor $options" \
            "monitor traffic."
        return
    fi

    local do_download=$(abcli_option_int "$options" download 1)
    local do_upload=$(abcli_option_int "$options" upload 1)

    job_name=$(abcli_option "$options" name $job_name)
    if [[ -z "$job_name" ]]; then
        abcli_log_error "-@batch: monitor: job-name not found."
        return 1
    fi

    [[ "$do_upload" == 1 ]] &&
        abcli_download - $job_name

    python3 -m notebooks_and_scripts.aws_batch \
        monitor_traffic \
        --job_name $job_name

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    return 0
}
