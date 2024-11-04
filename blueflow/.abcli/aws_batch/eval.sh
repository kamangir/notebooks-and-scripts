#! /usr/bin/env bash

function abcli_aws_batch_evaluate() {
    abcli_aws_batch_eval "$@"
}

function abcli_aws_batch_eval() {
    local options=$1
    job_name=$(abcli_option "$options" name $(abcli_string_timestamp))

    abcli_eval ,$options \
        python3 -m blueflow.aws_batch \
        submit \
        --command_line \"$@\" \
        --job_name "$job_name" \
        --type eval
}
