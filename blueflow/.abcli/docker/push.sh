#! /usr/bin/env bash

function abcli_docker_push() {
    local options=$1

    abcli_eval ,$options \
        docker push \
        kamangir/abcli:latest
}
