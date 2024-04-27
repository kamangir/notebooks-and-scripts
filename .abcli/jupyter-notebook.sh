#! /usr/bin/env bash

function notebooks() {
    abcli_notebooks "$@"
}

function abcli_notebooks() {
    local task=$(abcli_unpack_keyword "$1" open)

    if [ "$task" == "help" ]; then
        abcli_show_usage "@notebooks [open]$ABCUL[<notebook-name>]$ABCUL[<args>]" \
            "open ./<notebook-name>.ipynb."
        abcli_show_usage "@notebooks build$ABCUL[<notebook-name>]" \
            "build $abcli_object_name/<notebook-name>.ipynb."
        abcli_show_usage "@notebooks connect$ABCUL<1-2-3-4> [setup]" \
            "connect to jupyter notebook on ec2:<1-2-3-4>."
        abcli_show_usage "@notebooks create|touch$ABCUL[<notebook-name>]" \
            "create ./<notebook-name>.ipynb."
        abcli_show_usage "@notebooks host$ABCUL[setup]" \
            "host jupyter notebook on ec2."
        return
    fi

    if [[ ",build,create,open,touch," == *",$task,"* ]]; then
        local notebook_name=$(abcli_clarify_input $2 notebook)
        export abcli_notebooks_input="${@:3}"
    fi

    if [ "$task" == "build" ]; then
        jupyter-nbconvert \
            $notebook_name.ipynb \
            -y --ExecutePreprocessor.timeout=-1 --execute --allow-errors \
            --to html \
            --output-dir $abcli_object_path

        mv $abcli_object_path/$notebook_name.html $abcli_object_path/$abcli_object_name.html

        return
    fi

    # https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter.html
    if [ "$task" == "connect" ]; then
        local options=$3
        local do_setup=$(abcli_option_int "$options" setup 0)

        if [ "$do_setup" == 1 ]; then
            local ip_address=$(echo "$2" | tr . -)

            local pem_filename=$abcli_path_ignore/$abcli_aws_ec2_key_name.pem

            ssh \
                -i $pem_filename \
                -N -f -L 8888:localhost:8888 \
                ubuntu@ec2-$ip_address.$abcli_aws_region.compute.amazonaws.com
        fi

        open https://localhost:8888
        return
    fi

    if [ "$task" == "host" ]; then
        local options=$2
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

        return
    fi

    if [[ ",create,open,touch," == *",$task,"* ]]; then
        if [ -f $notebook_name.ipynb ]; then
            touch ./$notebook_name.ipynb
        else
            cp -v \
                $abcli_path_abcli/template.ipynb \
                ./$notebook_name.ipynb
        fi

        [[ "$task" == "open" ]] && jupyter notebook

        return
    fi

    abcli_log_error "-notebooks: $task: command not found."
    return 1
}
