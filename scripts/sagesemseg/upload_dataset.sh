#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"
    local script_name=$(abcli_script_get name)

    abcli_scripts source - sagesemseg/consts

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local cache_options=$sagesemseg_cache_dataset_options
        local options="dryrun,suffix=<v1>"
        local args="[--count <count>]"
        abcli_meta_script_show_usage $script_full_name "$EOP[$cache_options]$ABCUL[$options]$ABCUL$args" \
            "upload dataset to SageMaker for training."
        return
    fi

    local cache_options=$1
    local dataset_name=$(abcli_option "$cache_options" dataset pascal-voc)
    local cache_suffix=$(abcli_option "$cache_options" suffix v1)

    local dataset_object_name=$dataset_name
    [[ ! -z "$cache_suffix" ]] && dataset_object_name=$dataset_name-$cache_suffix

    [[ "$dataset_name" == "pascal-voc" ]] &&
        abcli_scripts source dryrun=$do_dryrun \
            sagesemseg/cache_dataset \
            "$cache_options"

    local options=$2
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local suffix=$(abcli_option "$options" suffix v1)

    local object_name=$dataset_object_name-$suffix

    abcli_log "$script_name: $dataset_object_name -> ☁️ / $object_name"

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofAI.semseg.sagemaker upload_dataset \
        --dataset_object_name $dataset_object_name \
        --object_name $object_name \
        "${@:3}"
}

runme "$@"
