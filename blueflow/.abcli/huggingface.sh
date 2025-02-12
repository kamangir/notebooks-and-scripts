#! /usr/bin/env bash

function blueflow_huggingface() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "clone" ]; then
        pushd $abcli_path_git >/dev/null
        git clone https://huggingface.co/kamangir/$2
        popd >/dev/null
        return
    fi

    if [ "$task" == "get_model_path" ]; then
        local repo_name=$(abcli_unpack_keyword "$2")

        local model_name=$3

        local options=$4
        local model_source=$(abcli_option "$options" model saved)

        if [ "$model_source" == "saved" ]; then
            echo $abcli_path_git/$repo_name/saved_model/$(abcli_clarify_input "$model_name" $repo_name)
        else
            echo $ABCLI_OBJECT_ROOT/$(abcli_clarify_object $model_name .)
        fi

        return
    fi

    if [ $task == "install" ]; then
        python3 -m pip install huggingface_hub
        huggingface-cli login
        return
    fi

    if [ $task == "save" ]; then
        local repo_name=$(abcli_unpack_keyword "$2")
        local model_name=$(abcli_clarify_input "$3" "$repo_name")
        local object_name=$(abcli_clarify_object $4 .)

        local options=$5
        local do_force=$(abcli_option_int "$options" force 0)

        if [ -d "$abcli_path_git/$repo_name/saved_model/$model_name" ] && [ "$do_force" == 0 ]; then
            abcli_log_error "-abcli: huggingface: save: $model_name: already exists."
            return
        fi

        abcli_log "releasing $object_name as $repo_name/$model_name: $options"

        abcli_download - $object_name

        pushd $abcli_path_git/$repo_name >/dev/null

        mkdir -p saved_model/$model_name

        cp -av $abcli_object_path/. saved_model/$model_name/

        rm -rf saved_model/$model_name/auxiliary

        git status

        return
    fi

    abcli_log_error "@huggingface: $task: command not found."
    return 1
}
