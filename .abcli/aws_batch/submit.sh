#! /usr/bin/env bash

function abcli_aws_batch_source() {
    abcli_aws_batch_submit "$@"
}

function abcli_aws_batch_submit() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="$abcli_scripts_options,name=<job-name>"
        abcli_show_usage "@batch source$ABCUL[$options]$ABCUL<script-name>$ABCUL[<args>]" \
            "source <script-name> in aws batch."
        return
    fi

    job_name=$(abcli_option "$options" name $(abcli_string_timestamp))

    abcli_eval ,$options \
        python3 -m notebooks_and_scripts.aws_batch \
        submit \
        --command_line \"$@\" \
        --job_name "$job_name"
}
