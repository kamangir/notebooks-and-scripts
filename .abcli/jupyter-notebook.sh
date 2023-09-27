#! /usr/bin/env bash

function notebooks() {
    abcli_notebooks "$@"
}

function abcli_notebooks() {
    local task=$(abcli_unpack_keyword "$1" open)

    if [ "$task" == "help" ]; then
        abcli_log "📜 $(python3 -m notebooks_and_scripts version --show_description 1)\n"

        abcli_show_usage "abcli notebooks$ABCUL[open]$ABCUL[<notebook>]$ABCUL[<args>]" \
            "open ./notebook.ipynb."
        abcli_show_usage "abcli notebooks build$ABCUL[<notebook>]" \
            "build $abcli_object_name/notebook.ipynb."
        abcli_show_usage "abcli notebooks connect$ABCUL<1-2-3-4> [setup]" \
            "[setup and] connect to jupyter notebook on ec2:1-2-3-4."
        abcli_show_usage "abcli notebooks host$ABCUL[setup]" \
            "[setup and] host jupyter notebook on ec2."
        abcli_show_usage "abcli notebooks touch$ABCUL[<notebook>]" \
            "touch ./<notebook>.ipynb."
        return
    fi

    if [[ ",build,open,touch," == *",$task,"* ]]; then
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

            local key_name=$(abcli_aws_json_get "['ec2']['key_name']")
            local pem_filename=$abcli_path_bash/bootstrap/config/$key_name.pem

            ssh \
                -i $pem_filename \
                -N -f -L 8888:localhost:8888 \
                ubuntu@ec2-$ip_address.$(abcli_aws_region).compute.amazonaws.com
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

    if [[ ",open,touch," == *",$task,"* ]]; then
        if [ -f $notebook_name.ipynb ]; then
            touch ./$notebook_name.ipynb
        else
            cp -v \
                $abcli_path_abcli/abcli.ipynb \
                ./$notebook_name.ipynb
        fi

        [[ "$task" == "open" ]] && jupyter notebook

        return
    fi

    abcli_log_error "-notebooks: $task: command not found."
}
