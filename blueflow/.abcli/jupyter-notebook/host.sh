#! /usr/bin/env bash

function abcli_notebooks_host() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage "@notebooks host$ABCUL${EOP}setup$EOPE" \
            "host jupyter notebook on ec2."
        return
    fi

    local do_setup=$(abcli_option_int "$options" setup 0)

    if [[ "$do_setup" == 1 ]]; then
        jupyter notebook password

        mkdir -p $HOME/ssl
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
            -keyout $HOME/ssl/mykey.key \
            -out $HOME/ssl/mycert.pem
    fi

    jupyter notebook \
        --certfile=$HOME/ssl/mycert.pem \
        --keyfile $HOME/ssl/mykey.key
}
