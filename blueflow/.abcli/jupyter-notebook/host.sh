#! /usr/bin/env bash

function abcli_notebooks_host() {
    local options=$1
    local do_setup=$(abcli_option_int "$options" setup 0)

    if [[ "$do_setup" == 1 ]]; then
        jupyter notebook password
        [[ $? -ne 0 ]] && return 1

        mkdir -p $HOME/ssl
        [[ $? -ne 0 ]] && return 1

        openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
            -keyout $HOME/ssl/mykey.key \
            -out $HOME/ssl/mycert.pem
        [[ $? -ne 0 ]] && return 1
    fi

    jupyter notebook \
        --certfile=$HOME/ssl/mycert.pem \
        --keyfile $HOME/ssl/mykey.key
}
