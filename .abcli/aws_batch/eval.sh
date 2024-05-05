#! /usr/bin/env bash

function abcli_aws_batch_evaluate() {
    abcli_aws_batch_eval "$@"
}

function abcli_aws_batch_eval() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="$abcli_scripts_options,name=<job-name>"
        abcli_show_usage "@batch eval$ABCUL[$options]$ABCUL<command-line>" \
            "eval <command-line> in aws batch."
        return
    fi

    job_name=$(abcli_option "$options" name $(abcli_string_timestamp))

    abcli_eval ,$options \
        python3 -m notebooks_and_scripts.aws_batch \
        submit \
        --command_line \"$@\" \
        --job_name "$job_name" \
        --type eval
}
