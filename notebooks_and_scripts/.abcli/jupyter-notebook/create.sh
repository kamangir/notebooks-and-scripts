#! /usr/bin/env bash

function abcli_notebooks_create() {
    local notebook_name=$(abcli_clarify_input $1 notebook)

    if [[ "$notebook_name" == "help" ]]; then
        abcli_show_usage "@notebooks create|touch$ABCUL$EOP<notebook-name>|<path>/<notebook-name>|notebook$EOPE" \
            "create <notebook-name>."
        return
    fi

    # for unity with the rest of @notebook
    [[ "$notebook_name" == *.ipynb ]] && notebook_name="${notebook_name%.ipynb}"

    if [ -f "$notebook_name.ipynb" ]; then
        touch "$notebook_name.ipynb"
    else
        local path=$(dirname "$notebook_name.ipynb")
        mkdir -pv $path

        cp -v \
            $abcli_path_abcli/template.ipynb \
            "$notebook_name.ipynb"
    fi
}
