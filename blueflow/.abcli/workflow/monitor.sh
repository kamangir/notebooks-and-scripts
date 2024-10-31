#! /usr/bin/env bash

function blueflow_workflow_monitor() {
    local options=$1
    local do_download=$(abcli_option_int "$options" download 1)
    local publish_as=$(abcli_option "$options" publish_as)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local node=$(abcli_option "$options" node void)

    local job_name=$(abcli_clarify_object $2 .)

    abcli_log "📜 workflow.monitor: $job_name @ $node ..."

    [[ "$do_download" == 1 ]] &&
        abcli_download - $job_name

    python3 -m blueflow.workflow.runners \
        monitor \
        --hot_node $node \
        --job_name $job_name

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    [[ ! -z "$publish_as" ]] &&
        abcli_publish as=$publish_as,~download,suffix=.gif $job_name

    local command_line="${@:3}"
    [[ -z "$command_line" ]] && return 0

    abcli_eval - \
        "$command_line"
}
