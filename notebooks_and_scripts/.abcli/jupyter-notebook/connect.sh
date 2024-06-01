#! /usr/bin/env bash

function abcli_notebooks_connect() {
    # only used if $do_setup
    local ip_address=$(echo "$1" | tr . -)

    if [[ "$ip_address" == "help" ]]; then
        abcli_show_usage "@notebooks connect <1-2-3-4> [setup]" \
            "connect to jupyter notebook on ec2:<1-2-3-4>."
        return
    fi

    # https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter.html
    local options=$2
    local do_setup=$(abcli_option_int "$options" setup 0)

    if [ "$do_setup" == 1 ]; then
        local pem_filename=$abcli_path_ignore/$abcli_aws_ec2_key_name.pem

        ssh \
            -i $pem_filename \
            -N -f -L 8888:localhost:8888 \
            ubuntu@ec2-$ip_address.$abcli_aws_region.compute.amazonaws.com
    fi

    open https://localhost:8888
}
