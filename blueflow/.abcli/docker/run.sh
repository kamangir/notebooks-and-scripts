#! /usr/bin/env bash

function abcli_docker_run() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="${EOP}dryrun$EOPE"
        abcli_show_usage "@docker run$ABCUL$options" \
            "run abcli docker image."
        return
    fi

    abcli_log "@docker: run $options ..."

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    abcli_eval dryrun=$do_dryrun,path=$abcli_path_nbs \
        docker-compose run abcli bash \
        --init-file /root/git/awesome-bash-cli/abcli/.abcli/abcli.sh
}
