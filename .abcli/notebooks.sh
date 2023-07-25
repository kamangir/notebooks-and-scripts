#! /usr/bin/env bash

function nb() {
    notebooks $@
}

function notebooks() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m notebooks --help
        fi
        return
    fi

    local function_name=notebooks_$task
    if [[ $(type -t $function_name) == "function" ]] ; then
        $function_name "${@:2}"
        return
    fi

    python3 -m notebooks \
        $task \
        ${@:2}
}