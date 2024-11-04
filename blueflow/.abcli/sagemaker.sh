#!/bin/bash

function abcli_sagemaker() {
    local task=${1:-browse}

    local options=$2

    if [ "$task" == "browse" ]; then
        local url

        local aws_region=$(aws configure get region)
        local url="https://$aws_region.console.aws.amazon.com/sagemaker/home?region=$aws_region#/dashboard"

        abcli_browse $url
        return
    fi

    abcli_log_error "@sagemaker: $task: command not found."
    return 1
}
