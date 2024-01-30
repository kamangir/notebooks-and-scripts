#! /usr/bin/env bash

function notebooks_and_scripts_conda() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        abcli_show_usage "notebooks_and_scripts conda create_env$ABCIL[~recreate]" \
            "create conda environment."
        return
    fi

    if [ "$task" == "create_env" ]; then
        local options=$2
        local do_recreate=$(abcli_option_int "$options" recreate 1)

        local environment_name=notebooks_and_scripts

        if [[ "$do_recreate" == 0 ]] && [[ $(abcli_conda exists $environment_name) == 1 ]]; then
            abcli_eval - conda activate $environment_name
            return
        fi

        abcli_conda create_env name=$environment_name

        pip3 install pymysql==0.10.1
        pip3 install geojson
        pip3 install beautifulsoup4
        pip3 install geopandas
        pip3 install tqdm
        pip3 install requests
        pip3 install opencv-python
        pip3 install pytest
        pip3 install matplotlib
        pip3 install boto3

        [[ "$abcli_is_mac" == true ]] &&
            pip3 install folium

        return
    fi

    abcli_log_error "-notebooks_and_scripts: conda: $task: command not found."
}
