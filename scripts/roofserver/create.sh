#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"

    local default_object_name=$(abcli_cache read roofai_semseg_model_AIRS_o2)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="suffix=<suffix>"
        abcli_meta_script_show_usage $script_full_name "[$options]$ABCUL$EOP[<model-object-name>*]$EOPE" \
            "create model, endpoint_config, and endpoint and serve <model-object-name> under <suffix>." \
            "default: $default_object_name"
        return
    fi

    local suffix=$(abcli_option "$options" suffix v2)
    abcli_log "🔗 suffix: $suffix"

    local object_name=$(abcli_clarify_object $2 $default_object_name)

    roofai_inference create \
        model $object_name

    roofai_inference create \
        endpoint_config,suffix=$suffix \
        $object_name

    roofai_inference create \
        endpoint,config_suffix=$suffix,suffix=$suffix \
        $object_name

    local endpoint_name=endpoint-$object_name-$suffix
    abcli_cache write \
        roofserver-endpoint-$suffix.endpoint_name \
        $endpoint_name

    roofai_inference describe \
        endpoint $endpoint_name
}

runme "$@"
