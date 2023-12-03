#! /usr/bin/env bash

function roofAI_train() {
    local options=$1

    local version="2.7.1"

    local script_name=$(basename "${BASH_SOURCE[0]}")
    local script_name=${script_name%.*}

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="order=<2>$ABCEP"
        local extra_options="profile=$semseg_profiles,~register,suffix=<suffix>"
        abcli_script_show_usage "$script_name$ABCUL[$options]$ABCUL[<args>]" \
            "train a roofAI semseg model at the <order>" \
            "[$extra_options]"
        return
    fi

    roofAI init

    local model_order=$(abcli_option_int "$options" order 0)

    local dataset_object_name=dataset-$(@timestamp)
    local model_order_zeros=$(python3 -c "print(''.join($model_order*['0']))")
    roofAI_dataset_ingest \
        source=AIRS \
        $dataset_object_name \
        --test_count 25$model_order_zeros \
        --train_count 35$model_order_zeros \
        --val_count 10$model_order_zeros

    local model_object_name=model-$(@timestamp)
    roofAI_semseg train \
        $(
            abcli_option_subset \
                "$options" \
                profile=FULL,register,suffix=o$model_order
        ) \
        $dataset_object_name \
        $model_object_name \
        --classes roof \
        "${@:2}"

    abcli_tag set \
        $model_object_name \
        order=$model_order,script_name=$script_name
}

roofAI_train "$@"
