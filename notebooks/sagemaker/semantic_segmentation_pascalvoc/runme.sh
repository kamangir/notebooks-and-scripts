#! /usr/bin/env bash

function runme() {
    local dataset_object_name="pascalvoc-v2-v2"
    local dataset_name="pascal-voc"

    dataset_object_path=$abcli_object_root/$dataset_object_name
    pushd $dataset_object_path >/dev/null

    if [[ ! -f "$dataset_object_path/$dataset_name.tgz" ]]; then
        wget -P $dataset_object_path \
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
