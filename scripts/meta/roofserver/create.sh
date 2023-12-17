#! /usr/bin/env bash

function runme() {
    local options=$1

    local version="1.2.1"

    local script_full_name="${BASH_SOURCE[0]}"
    local script_name=$(basename "${BASH_SOURCE[0]}")
    local script_name=${script_name%.*}

    local default_object_name=$(abcli_cache read roofAI_semseg_model_AIRS_o2)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="suffix=<v2>"
        abcli_meta_script_show_usage $script_full_name "[$options]$ABCUL$ABCXOP[<model-object-name>*]$ABCXOPE" \
            "create model, endpoint_config, and endpoint to serve <model-object-name>." \
            "default: $default_object_name"
        return
    fi

    local suffix=$(abcli_option "$options" suffix v2)

    local object_name=$(abcli_clarify_object $2 $default_object_name)

    roofAI_inference create \
        model $object_name

    roofAI_inference create \
        endpoint_config,suffix=$suffix \
        $object_name

    roofAI_inference create \
        endpoint,config_suffix=$suffix,suffix=$suffix \
        $object_name

    roofAI_inference describe \
        endpoint \
        endpoint-$object_name-$suffix
}

runme "$@"
