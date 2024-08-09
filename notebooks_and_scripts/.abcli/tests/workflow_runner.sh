#! /usr/bin/env bash

function test_notebooks_and_scripts_worflow_runner() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local list_of_runners=$(abcli_option "$options" runner $NBS_RUNNERS_LIST)
    local list_of_patterns=$(abcli_option "$options" pattern $NBS_PATTRENS_LIST)

    local pattern
    local runner
    for runner in $(echo $list_of_runners | tr \| " "); do
        abcli_log "📜 testing runner=$runner"
        for pattern in $(echo $list_of_patterns | tr \| " "); do
            abcli_log "📜 testing pattern=$pattern"

            local job_name=$pattern-$runner-$(abcli_string_timestamp)

            workflow create \
                pattern=$pattern $job_name
            [[ $? -ne 0 ]] && return 1

            workflow submit \
                ~download,to=$runner \
                $job_name
            [[ $? -ne 0 ]] && return 1

            workflow monitor \
                ~download,publish_as=$pattern-$runner \
                $job_name
            [[ $? -ne 0 ]] && return 1

            abcli_hr
        done
    done
}
