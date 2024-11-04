#! /usr/bin/env bash

function abcli_docker_run() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    abcli_log "@docker: run $options ..."

    abcli_eval dryrun=$do_dryrun,path=$abcli_path_nbs \
        docker-compose run abcli bash \
        --init-file /root/git/awesome-bash-cli/abcli/.abcli/abcli.sh
}
