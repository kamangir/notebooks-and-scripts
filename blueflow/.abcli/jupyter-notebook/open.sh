#! /usr/bin/env bash

function abcli_notebooks_open() {
    abcli_notebooks_create "$1"
    [[ $? -ne 0 ]] && return 1

    export abcli_notebooks_input="${@:2}"
    jupyter notebook
}
