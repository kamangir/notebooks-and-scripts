#! /usr/bin/env bash

function runme() {
    local options=$1

    local script_full_name="${BASH_SOURCE[0]}"

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="$EOP~batch,dryrun,~publish"
        abcli_meta_script_show_usage $script_full_name "$options$ABCUL$vancouver_watching_ingest_options$EOP$ABCUL-|<object-name>$EARGS" \
            "vanwatch ingest, defaults to vancouver."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local on_batch=$(abcli_option_int "$options" batch 1)
    local do_publish=$(abcli_option_int "$options" publish 1)

    local ingest_options=$2,publish=$do_publish

    local object_name=$(abcli_clarify_object $3 $(abcli_string_timestamp))

    if [[ "$on_batch" == 1 ]]; then
        abcli_aws_batch source \
            name=vanwatch-ingest-$object_name-$(abcli_string_random --length 5),dryrun=$do_dryrun \
            $script_name \
            - \
            $ingest_options, \
            $object_name \
            "${@:4}"
        return
    fi

    abcli_eval dryrun=$do_dryrun \
        vancouver_watching_ingest \
        $ingest_options, \
        $object_name \
        "${@:4}"
}

runme "$@"
