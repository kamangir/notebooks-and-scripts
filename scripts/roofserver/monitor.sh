#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="cloudwatch,~describe,invoke,suffix=<suffix>"
        abcli_meta_script_show_usage $script_full_name "[$options]" \
            "monitor <suffix>."
        return
    fi

    local suffix=$(abcli_option "$options" suffix v2)
    abcli_log "🔗 suffix: $suffix"

    local endpoint_name=$(abcli_cache read roofserver-endpoint-$suffix.endpoint_name)
    abcli_log "🔗 endpoint: $endpoint_name"

    [[ $(abcli_option_int "$options" cloudwatch 0) == 1 ]] &&
        roofai_cloudwatch browse \
            endpoint $endpoint_name

    [[ $(abcli_option_int "$options" describe 1) == 1 ]] &&
        roofai_inference describe \
            endpoint $endpoint_name

    if [ $(abcli_option_int "$options" invoke 0) == 1 ]; then
        echo "wip: invoke"
    fi

}

runme "$@"
