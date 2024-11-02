#! /usr/bin/env bash

function test_notebooks_and_scripts_help() {
    # TODO: enable
    return 0

    local options=$1

    local module
    for module in \
        "abcli_aws_batch" \
        "abcli_aws_batch browse" \
        "abcli_aws_batch eval" \
        "abcli_aws_batch list" \
        "abcli_aws_batch source" \
        \
        "abcli_docker" \
        "abcli_docker browse" \
        "abcli_docker build" \
        "abcli_docker clear" \
        "abcli_docker eval" \
        "abcli_docker push" \
        "abcli_docker run" \
        "abcli_docker seed" \
        "abcli_docker source" \
        \
        "abcli_notebooks" \
        "abcli_notebooks open" \
        "abcli_notebooks build" \
        "abcli_notebooks code" \
        "abcli_notebooks connect" \
        "abcli_notebooks create" \
        "abcli_notebooks touch" \
        "abcli_notebooks host" \
        \
        "abcli_sagemaker" \
        "abcli_sagemaker browse" \
        \
        "blueflow huggingface" \
        "blueflow huggingface clone" \
        "blueflow huggingface install" \
        "blueflow huggingface get_model_path" \
        "blueflow huggingface save" \
        \
        "blueflow workflow" \
        "blueflow workflow create" \
        "blueflow workflow monitor" \
        "blueflow workflow submit"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
