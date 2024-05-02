#! /usr/bin/env bash

function notebooks_and_scripts_workflow_submit() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        list_of_runners=$(python3 -m notebooks_and_scripts.workflow.runners list --delim \|)
        local options="$EOP~download,${EOPE}runner=$list_of_runners$EOP,~upload$EOPE"
        abcli_show_usage "@workflow submit [$options] [.|<job-name>]" \
            "submit workflow."
        return
    fi

    local do_download=$(abcli_option_int "$options" download 1)
    local do_upload=$(abcli_option_int "$options" upload 1)

    local job_name=$(abcli_clarify_object $2 .)

    [[ "$do_download" == 1 ]] &&
        abcli_download - $job_name

    python3 -m notebooks_and_scripts.workflow \
        submit \
        --job_name $job_name \
        --runner $runner

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    return 0
}
