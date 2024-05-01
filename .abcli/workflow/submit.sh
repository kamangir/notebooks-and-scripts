#! /usr/bin/env bash

function notebooks_and_scripts_workflow_submit() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="dryrun,upload"
        local args="[--<keyword> <value>]$ABCUL[--<keyword> <value>]"
        abcli_show_usage "blue_plugin node leaf$ABCUL[$options]$ABCUL<object-name>$ABCUL$args" \
            "blue-plugin node leaf <object-name>."
        return
    fi

    echo "blue-plugin: node: leaf: 🪄"
}
