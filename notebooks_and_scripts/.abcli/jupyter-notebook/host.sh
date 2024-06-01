#! /usr/bin/env bash

function abcli_notebooks_host() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage "@notebooks host [setup]" \
            "host jupyter notebook on ec2."
        return
    fi

    local do_setup=$(abcli_option_int "$options" setup 0)

    if [ "$do_setup" == 1 ]; then
        jupyter notebook password

        mkdir -p $abcli_path_home/ssl
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
            -keyout $abcli_path_home/ssl/mykey.key \
            -out $abcli_path_home/ssl/mycert.pem
    fi

    jupyter notebook \
        --certfile=$abcli_path_home/ssl/mycert.pem \
        --keyfile $abcli_path_home/ssl/mykey.key
}
