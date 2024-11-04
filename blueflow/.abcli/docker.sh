#! /usr/bin/env bash

function abcli_docker() {
    local task=$(abcli_unpack_keyword $1 help)
    [[ "$task" == evaluate ]] && task="eval"

    local function_name=abcli_docker_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    local options=$2

    if [[ "|eval|source|" == *"|$task|"* ]]; then
        local abcli_options=install,mono
        local do_verbose=$(abcli_option_int "$options" verbose 0)
        [[ "$do_verbose" == 1 ]] && abcli_options="$abcli_options,verbose"

        local command_line
        [[ "$task" == "eval" ]] &&
            command_line="source \
            /root/git/awesome-bash-cli/abcli/.abcli/abcli.sh $abcli_options \
            abcli_eval $options \
            ${@:3}"
        [[ "$task" == "source" ]] &&
            command_line="source \
            /root/git/awesome-bash-cli/abcli/.abcli/abcli.sh $abcli_options \
            abcli_scripts source $options \
            ${@:3}"

        abcli_eval dryrun=$do_dryrun,path=$abcli_path_nbs \
            docker-compose run abcli \
            bash -c \"$command_line\"

        return
    fi

    abcli_log_error "@docker: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /docker
