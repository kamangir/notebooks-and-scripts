#! /usr/bin/env bash

function abcli_notebooks_code() {
    local notebook_name=$(abcli_clarify_input $1 notebook)

    if [[ "$notebook_name" == "help" ]]; then
        abcli_show_usage "@notebooks ${EOP}code$ABCUL<notebook-name>|notebook$EOPE" \
            "code <notebook-name>."
        return
    fi

    abcli_notebooks_create "$1"

    [[ "$notebook_name" == *.ipynb ]] && notebook_name="${notebook_name%.ipynb}"

    code "$notebook_name.ipynb"
}
