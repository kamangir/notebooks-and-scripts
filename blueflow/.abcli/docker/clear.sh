#! /usr/bin/env bash

function abcli_docker_clear() {
    local options=$1

    abcli_eval ,$options \
        "docker image prune"

    abcli_eval ,$options \
        "docker system prune"

    abcli_eval ,$options \
        "docker-compose down --remove-orphans"
}
