#! /usr/bin/env bash

function test_notebooks_and_scripts_version() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    abcli_eval dryrun=$do_dryrun \
        "notebooks_and_scripts version ${@:2}"

    return 0
}
