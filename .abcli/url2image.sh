#! /usr/bin/env bash

function url2image() {
    abcli_url2image "$@"
}

function abcli_url2image() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        abcli_show_usage "url2image read_url$ABCUL<url>$ABCUL[--verbose 1]" \
            "read <url>."
        return
    fi

    if [ "$task" == "read_url" ]; then
        python3 -m notebooks_and_scripts.url2image \
            read_url \
            --url "$2" \
            "${@:3}"
        return
    fi

    abcli_log_error "-abcli: url2image: $task: command not found."
}
