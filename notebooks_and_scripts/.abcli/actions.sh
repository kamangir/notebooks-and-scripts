#! /usr/bin/env bash

function notebooks_and_scripts_action_git_before_push() {
    notebooks_and_scripts build_README
    [[ $? -ne 0 ]] && return 1

    [[ "$(abcli_git get_branch)" != "main" ]] &&
        return 0

    notebooks_and_scripts pypi build
}
