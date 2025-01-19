#! /usr/bin/env bash

function roofai_train() {
    local options=$1

    local version="2.11.1"

    local script_name=$(abcli_script_get name)
    local script_path=$(abcli_script_get path)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="order=<2>$EOP,profile=$semseg_profiles,~register,suffix=<suffix>$EOPE"
        abcli_script_show_usage "$script_name$ABCUL[$options]$EARGS" \
            "train a roofai semseg model at the <order>."
        return
    fi

    roofai init

    local model_order=$(abcli_option_int "$options" order 0)

    local dataset_object_name=dataset-$(@timestamp)
    local model_order_zeros=$(python3 -c "print(''.join($model_order*['0']))")
    roofai_dataset_ingest \
        source=AIRS \
        $dataset_object_name \
        --test_count 25$model_order_zeros \
        --train_count 35$model_order_zeros \
        --val_count 10$model_order_zeros

    local model_object_name=model-$(@timestamp)
    roofai_semseg_train \
        $(
            abcli_option_subset \
                "$options" \
                profile=FULL,register,suffix=o$model_order
        ) \
        $dataset_object_name \
        $model_object_name \
        --classes roof \
        "${@:2}"

    abcli_cache write \
        $model_object_name.order $model_order
}

roofai_train "$@"
