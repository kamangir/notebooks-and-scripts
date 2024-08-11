#! /usr/bin/env bash

function notebooks_and_scripts_workflow_monitor() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="~download,node=<node>,publish_as=<public-object-name>,~upload"
        abcli_show_usage "workflow monitor$ABCUL$EOP[$options]$ABCUL[.|<job-name>]$ABCUL[<command-line>]$EOPE" \
            "monitor <job-name>/workflow and run <command-line>."
        return
    fi

    local do_download=$(abcli_option_int "$options" download 1)
    local publish_as=$(abcli_option "$options" publish_as)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local node=$(abcli_option "$options" node void)

    local job_name=$(abcli_clarify_object $2 .)

    abcli_log "📜 workflow.monitor: $job_name @ $node ..."

    [[ "$do_download" == 1 ]] &&
        abcli_download - $job_name

    python3 -m notebooks_and_scripts.workflow.runners \
        monitor \
        --hot_node $node \
        --job_name $job_name

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    [[ ! -z "$publish_as" ]] &&
        abcli_publish as=$publish_as,~download,suffix=.gif $job_name

    local command_line="${@:3}"
    if [[ ! -z "$command_line" ]]; then
        abcli_eval - \
            "$command_line"
    else
        return 0
    fi
}
