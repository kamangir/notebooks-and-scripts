#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"
    local script_name=$(abcli_script_get name)

    abcli_scripts source - sagesemseg/consts

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="$sagesemseg_cache_dataset_options,rm"
        abcli_meta_script_show_usage $script_full_name "$EOP[$options]$EOPE" \
            "cache dataset."
        return
    fi

    local dataset_name=$(abcli_option "$options" dataset pascal-voc)
    local do_rm=$(abcli_option "$options" rm 0)
    local suffix=$(abcli_option "$options" suffix v1)

    local dataset_object_name=$dataset_name-$suffix

    local dataset_object_path=$ABCLI_OBJECT_ROOT/$dataset_object_name
    mkdir -pv $dataset_object_path

    if [[ -d "$dataset_object_path/$dataset_name" ]]; then
        abcli_log "✅ $dataset_object_name/$dataset_name/"
        return
    fi

    abcli_log "caching $dataset_object_name"

    pushd $dataset_object_path >/dev/null

    if [[ ! -f "$dataset_name.tgz" ]]; then
        curl -O https://fast-ai-imagelocal.s3.amazonaws.com/pascal-voc.tgz
    else
        abcli_log "✅ $dataset_object_name/$dataset_name.tgz"
    fi

    tar -xvf $dataset_name.tgz

    [[ "$do_rm" == 1 ]] && rm -v $dataset_name.tgz

    popd >/dev/null
}

runme "$@"
