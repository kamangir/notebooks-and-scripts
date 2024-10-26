#!/bin/bash

function abcli_sagemaker() {
    local task=${1:-help}

    if [ "$task" == "help" ]; then
        abcli_sagemaker browse "$@"
        return
    fi

    local options=$2

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        case "$task" in
        browse)
            abcli_show_usage "@sagemaker browse$ABCUL[dashboard]" \
                "browse sagemaker."
            ;;
        *)
            abcli_log_error "-@sagemaker: $task: help: command not found."
            return 1
            ;;
        esac
        return
    fi

    if [ "$task" == "browse" ]; then
        local url

        local aws_region=$(aws configure get region)
        local url="https://$aws_region.console.aws.amazon.com/sagemaker/home?region=$aws_region#/dashboard"

        abcli_browse $url
        return
    fi

    abcli_log_error "-@sagemaker: $task: command not found."
    return 1
}
