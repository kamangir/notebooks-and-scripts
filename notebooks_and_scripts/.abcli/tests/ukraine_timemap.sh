#! /usr/bin/env bash

function test_notebooks_and_scripts_ukraine_timemap() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 0)

    abcli_eval dryrun=$do_dryrun \
        "ukraine_timemap ingest upload=$do_upload,$2 ${@:3}"

    return 0
}
