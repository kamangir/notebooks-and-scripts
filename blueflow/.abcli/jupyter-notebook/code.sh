#! /usr/bin/env bash

function abcli_notebooks_code() {
    local notebook_name=$(abcli_clarify_input $1 notebook)

    abcli_notebooks_create "$1"

    [[ "$notebook_name" == *.ipynb ]] && notebook_name="${notebook_name%.ipynb}"

    code "$notebook_name.ipynb"
}
