#! /usr/bin/env bash

function openai_commands_plugin_README() {
    local options=$1

    abcli_eval ,$options \
        openai_commands build_README
}
