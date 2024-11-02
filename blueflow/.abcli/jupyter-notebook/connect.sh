#! /usr/bin/env bash

function abcli_notebooks_connect() {
    local options=$1
    local do_setup=$(abcli_option_int "$options" setup 0)
    local ip_address=$(abcli_option "$options" ip)
    ip_address=$(echo "$ip_address" | tr . -)

    # https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter.html
    if [ "$do_setup" == 1 ]; then
        local pem_filename=$abcli_path_ignore/$abcli_aws_ec2_key_name.pem

        ssh \
            -i $pem_filename \
            -N -f -L 8888:localhost:8888 \
            ubuntu@ec2-$ip_address.$ABCLI_AWS_REGION.compute.amazonaws.com
    fi

    open https://localhost:8888
}
