#! /usr/bin/env bash

function abcli_notebooks_build() {
    local notebook_name=$(abcli_clarify_input $1 notebook)

    if [[ "$notebook_name" == "help" ]]; then
        abcli_show_usage "@notebooks build$ABCUL$EOP<notebook-name>|notebook$EOPE" \
            "build $abcli_object_name/<notebook-name>.ipynb."
        return
    fi

    [[ "$notebook_name" == *.ipynb ]] && notebook_name="${notebook_name%.ipynb}"

    export abcli_notebooks_input="${@:2}"

    jupyter-nbconvert \
        $notebook_name.ipynb \
        -y --ExecutePreprocessor.timeout=-1 --execute --allow-errors \
        --to html \
        --output-dir $abcli_object_path

    mv -v \
        $abcli_object_path/$notebook_name.html \
        $abcli_object_path/$abcli_object_name.html
}
