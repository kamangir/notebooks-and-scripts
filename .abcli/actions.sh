#! /usr/bin/env bash

function notebooks_and_scripts_action_git_before_push() {
    notebooks_and_scripts pypi build
}
