#! /usr/bin/env bash

function url2image() {
    abcli_url2image "$@"
}

function abcli_url2image() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        abcli_url2image read_url help
        abcli_url2image render_url help
        return
    fi

    if [ "$task" == "read_url" ]; then
        local url=$2
        if [[ "$url" == help ]]; then
            abcli_show_usage "url2image read_url$ABCUL<url>$ABCUL[--verbose 1]" \
                "read <url>."
            return
        fi

        python3 -m notebooks_and_scripts.url2image \
            read_url \
            --url "$url" \
            "${@:3}"
        return
    fi

    if [ "$task" == "render_url" ]; then
        local options=$2
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            local options="~upload,url=<url>"
            local args="[--count <10>]$ABCUL[--height <1024>]$ABCUL[--width <1024>]$ABCUL[--verbose 1]"
            abcli_show_usage "url2image render_url$ABCUL[$options]$ABCUL<prompt>$ABCUL[-|<object-name>]$ABCUL$args" \
                "render <url>."
            return
        fi

        local do_upload=$(abcli_option_int "$options" upload 1)

        local object_name=$(abcli_clarify_object $4 $(abcli_string_timestamp))

        python3 -m notebooks_and_scripts.url2image \
            render_url \
            --url $(abcli_option "$options" url https://earthdaily.com/constellation/) \
            --prompt "$3" \
            --object_name $object_name \
            "${@:5}"

        [[ "$do_upload" == 1 ]] &&
            abcli_upload object $object_name

        return
    fi

    abcli_log_error "-abcli: url2image: $task: command not found."
}
