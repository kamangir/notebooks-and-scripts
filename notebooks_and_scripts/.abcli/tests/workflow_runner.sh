#! /usr/bin/env bash

function test_notebooks_and_scripts_worflow_runner() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local pattern
    local runner
    for runner in $(echo $NBS_RUNNERS_LIST | tr \| " "); do
        for pattern in $(echo $NBS_PATTRENS_LIST | tr \| " "); do
            abcli_log "testing pattern=$pattern"

            local job_name=$pattern-$(abcli_string_timestamp)

            workflow create pattern=$pattern $job_name
            [[ $? -ne 0 ]] && return 1

            workflow submit ~download,to=$runner $job_name
            [[ $? -ne 0 ]] && return 1

            workflow monitor ~download $job_name
            [[ $? -ne 0 ]] && return 1

            abcli_hr
        done
    done
}
