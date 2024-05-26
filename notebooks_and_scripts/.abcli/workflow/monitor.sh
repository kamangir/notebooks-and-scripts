#! /usr/bin/env bash

function notebooks_and_scripts_workflow_monitor() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="$EOP~download,node=<node>,publish,~upload"
        abcli_show_usage "workflow monitor$ABCUL$options$ABCUL.|<job-name>$EOPE" \
            "monitor workflow."
        return
    fi

    local do_download=$(abcli_option_int "$options" download 1)
    local do_publish=$(abcli_option_int "$options" publish 0)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local node=$(abcli_option "$options" node void)

    local job_name=$(abcli_clarify_object $2 .)

    [[ "$do_download" == 1 ]] &&
        abcli_download - $job_name

    local pattern=$(abcli_metadata get \
        key=load_pattern.pattern,object \
        $job_name)

    python3 -m notebooks_and_scripts.workflow.runners \
        monitor \
        --hot_node $node \
        --job_name $job_name

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    [[ "$do_publish" == 1 ]] &&
        abcli_publish as=$pattern,~download,suffix=.gif $job_name

    return 0
}
