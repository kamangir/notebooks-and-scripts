#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"
    local script_name=$(abcli_script_get name)

    abcli_scripts source - sagesemseg/consts

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="dryrun,~upload"
        local args="[--deploy 0]$ABCUL[--delete_endpoint 0]$ABCUL[--epochs 10]$ABCUL[--instance_type ml.p3.2xlarge]"
        abcli_meta_script_show_usage $script_full_name "$EOP[$options]$ABCUL[test|<dataset-object-name>]$ABCUL[-|<model-object-name>]$ABCUL$args$EOPE" \
            "<dataset-object-name> -train-> <model-object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_not $do_dryrun)

    local dataset_object_name=$(abcli_clarify_object "$2" test)
    if [[ "$dataset_object_name" == "test" ]]; then
        dataset_object_name="pascal-voc-v1-debug-v2"
        do_upload=0
    fi

    do_upload=$(abcli_option_int "$options" upload $do_upload)

    local model_object_name=$(abcli_clarify_object "$3" sagesemseg-model-test-$(abcli_string_timestamp))

    abcli_log "$script_name: $dataset_object_name -> $model_object_name"

    abcli_tags set \
        $model_object_name \
        trained_on.$dataset_object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m roofAI.semseg.sagemaker train_model \
        --dataset_object_name $dataset_object_name \
        --model_object_name $model_object_name \
        "${@:4}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $model_object_name
}

runme "$@"
