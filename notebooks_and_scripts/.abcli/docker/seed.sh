#! /usr/bin/env bash

function abcli_docker_seed() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage "@docker seed" \
            "seed docker 🌱."
        return
    fi

    abcli_seed docker "$@"
}
