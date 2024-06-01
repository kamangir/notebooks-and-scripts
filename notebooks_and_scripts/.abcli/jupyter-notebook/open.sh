#! /usr/bin/env bash

function abcli_notebooks_open() {
    local notebook_name=$(abcli_clarify_input $1 notebook)

    if [[ "$notebook_name" == "help" ]]; then
        abcli_show_usage "@notebooks [open]$ABCUL[<notebook-name>]$ABCUL[<args>]" \
            "open ./<notebook-name>.ipynb."
        return
    fi

    abcli_notebooks_create "$1"

    export abcli_notebooks_input="${@:2}"
    jupyter notebook
}
