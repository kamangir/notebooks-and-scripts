#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"
    local script_name=$(abcli_script_get name)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="dataset=pascal-voc,suffix=<v1>"
        abcli_meta_script_show_usage $script_full_name "$EOP[$options]$EOPE" \
            "cache dataset."
        return
    fi

    local dataset_name=$(abcli_option "$options" dataset pascal-voc)
    local suffix=$(abcli_option "$options" suffix v1)

    local dataset_object_name=$dataset_name-$suffix

    abcli_log "caching $dataset_object_name"

    local dataset_object_path=$abcli_object_root/$dataset_object_name
    mkdir -pv $dataset_object_path
    pushd $dataset_object_path >/dev/null

    if [[ ! -f "$dataset_name.tgz" ]]; then
        wget -P ./ \
            https://fast-ai-imagelocal.s3.amazonaws.com/pascal-voc.tgz
    else
        abcli_log "✅ $dataset_name.tgz"
    fi

    if [[ ! -d "$dataset_object_path/$dataset_name" ]]; then
        tar -xvf $dataset_name.tgz
    else
        abcli_log "✅ $dataset_name/"
    fi

    popd >/dev/null
}

runme "$@"
