#! /usr/bin/env bash

function abcli_docker() {
    local task=$(abcli_unpack_keyword $1 help)
    [[ "$task" == evaluate ]] && task="eval"

    if [ "$task" == "help" ]; then
        abcli_docker_browse "$@"
        abcli_docker_build "$@"
        abcli_docker_clear "$@"
        abcli_docker eval "$@"
        abcli_docker_push "$@"
        abcli_docker_run "$@"
        abcli_docker_seed "$@"
        abcli_docker source "$@"
        return
    fi

    local function_name=abcli_docker_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    local options=$2

    if [[ "|eval|source|" == *"|$task|"* ]]; then
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            options="$EOP$abcli_scripts_options,verbose$EOPE"
            [[ "$task" == "eval" ]] &&
                abcli_show_usage "@docker eval$ABCUL$options$ABCUL<command-line>" \
                    "run <command-line> through the abcli docker image."

            [[ "$task" == "source" ]] &&
                abcli_show_usage "@docker source$ABCUL$options$ABCUL<script-name> [<args>]" \
                    "source <script-name> <args> through the abcli docker image."

            return
        fi

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

    abcli_log_error "-@docker: $task: command not found."
    return 1
}

abcli_source_path - caller,suffix=/docker
