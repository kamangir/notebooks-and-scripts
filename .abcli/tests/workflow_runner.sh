#! /usr/bin/env bash

function test_notebooks_and_scripts_worflow_runner() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local pattern
    for pattern in $(echo $NBS_PATTRENS_LIST | tr \| " "); do
        abcli_log "testing pattern=$pattern"

        local job_name=$pattern-$(abcli_string_timestamp)

        workflow create pattern=$pattern $job_name

        workflow submit ~download,to=aws_batch $job_name

        workflow monitor ~download $job_name

        abcli_hr
    done
}
