#! /usr/bin/env bash

export abcli_path_nbs=$abcli_path_git/notebooks-and-scripts

function nbs() {
    notebooks_and_scripts "$@"
}

function notebooks_and_scripts() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        abcli_show_usage "notebooks_and_scripts init [clear]" \
            "init notebooks_and_scripts."

        notebooks_and_scripts_conda "$@"
        notebooks_and_scripts pylint "$@"
        notebooks_and_scripts pytest "$@"
        return
    fi

    local function_name="notebooks_and_scripts_$task"
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [ "$task" == "init" ]; then
        abcli_init notebooks_and_scripts "${@:2}"
        conda activate notebooks-and-scripts
        return
    fi

    if [ "$task" == "pytest" ]; then
        abcli_pytest plugin=notebooks-and-scripts,$2 \
            "${@:3}"
        return
    fi

    if [ "$task" == "pylint" ]; then
        if [[ "$2" == "help" ]]; then
            abcli_show_usage "notebooks_and_scripts pylint <args>" \
                "pylint notebooks-and-scripts."
            return
        fi

        abcli_pip install pylint

        pushd $abcli_path_git/notebooks-and-scripts >/dev/null
        pylint \
            -d $abcli_pylint_ignored \
            $(git ls-files '*.py') \
            "${@:2}"
        popd >/dev/null

        return
    fi

    if [ "$task" == "version" ]; then
        python3 -m notebooks_and_scripts version "${@:2}"
        return
    fi

    abcli_log_error "-abcli: scripts: $task: command not found."
}
