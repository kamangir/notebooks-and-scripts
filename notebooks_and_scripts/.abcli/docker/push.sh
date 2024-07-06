#! /usr/bin/env bash

function abcli_docker_push() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage "@docker push" \
            "push the abcli docker image."
        return
    fi

    abcli_eval ,$options \
        docker push \
        kamangir/abcli:latest
}
