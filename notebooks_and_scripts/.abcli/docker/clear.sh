#! /usr/bin/env bash

function abcli_docker_clear() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage "@docker clear" \
            "clear docker."
        return
    fi

    abcli_eval ,$options \
        "docker image prune"

    abcli_eval ,$options \
        "docker system prune"
}
