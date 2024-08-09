#! /usr/bin/env bash

function notebooks_and_scripts_action_git_before_push() {
    notebooks_and_scripts build_README

    [[ "$(abcli_git get_branch)" == "main" ]] &&
        notebooks_and_scripts pypi build
}
