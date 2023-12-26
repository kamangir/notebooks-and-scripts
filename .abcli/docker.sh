#! /usr/bin/env bash

function abcli_docker() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        abcli_show_usage "abcli docker browse [~public]" \
            "browse docker-hub"

        abcli_show_usage "abcli docker build [dryrun,~push,run]" \
            "build abcli docker image."

        abcli_show_usage "abcli docker clear" \
            "clear docker."

        abcli_show_usage "abcli docker push" \
            "push abcli docker image."

        abcli_show_usage "abcli docker run [dryrun]" \
            "run abcli docker image."

        abcli_show_usage "abcli docker seed" \
            "seed docker 🌱."

        abcli_docker source "$@"
        return
    fi

    local options=$2

    local filename="Dockerfile"
    local tag="kamangir/abcli"

    if [ "$task" == "browse" ]; then
        local options=$2

        local show_public=$(abcli_option_int "$options" public 1)

        local url=https://hub.docker.com/repository/docker/kamangir/abcli/general
        [[ "$show_public" == 1 ]] &&
            local url=https://hub.docker.com/r/kamangir/abcli/tags

        abcli_browse_url $url
        return
    fi

    if [ "$task" == "build" ]; then
        abcli_log "docker: building $filename: $tag: $options"

        local do_dryrun=$(abcli_option_int "$options" dryrun 0)
        local do_push=$(abcli_option_int "$options" push $(abcli_not $do_dryrun))
        local do_run=$(abcli_option_int "$options" run 0)

        pushd $abcli_path_git >/dev/null

        mkdir -p temp
        cp -v ~/.kaggle/kaggle.json temp/

        [[ "$do_dryrun" == 0 ]] &&
            docker build \
                --build-arg HOME=$HOME \
                -t $tag \
                -f notebooks-and-scripts/$filename \
                .

        rm -rfv temp

        [[ "$do_push" == "1" ]] &&
            abcli_eval - \
                "docker push $tag:latest"

        [[ "$do_run" == "1" ]] &&
            abcli_docker run $options

        popd >/dev/null

        return
    fi

    if [ "$task" == "clear" ]; then
        abcli_eval - \
            "docker image prune"
        abcli_eval - \
            "docker system prune"
        return
    fi

    if [ "$task" == "push" ]; then
        abcli_eval - \
            "docker push $tag:latest"
        return
    fi

    if [ "$task" == "run" ]; then
        abcli_log "docker: running $filename: $tag: $options"

        local do_dryrun=$(abcli_option_int "$options" dryrun 0)

        abcli_eval dryrun=$do_dryrun,path=$abcli_path_nbs \
            docker-compose run abcli bash \
            --init-file /root/git/awesome-bash-cli/bash/abcli.sh

        return
    fi

    if [ "$task" == "seed" ]; then
        abcli_seed docker "${@:2}"
        return
    fi

    if [ "$task" == "source" ]; then
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            abcli_show_usage "abcli docker source $EOP[$abcli_scripts_options]$EOPE$ABCUL<script-name> [<args>]" \
                "docker source <script-name>."
            return
        fi

        local command_line="source \
            /root/git/awesome-bash-cli/bash/abcli.sh install,minimal,mono \
            abcli_scripts source $options \
            ${@:3}"

        abcli_eval dryrun=$do_dryrun,path=$abcli_path_nbs \
            docker-compose run abcli \
            bash -c \"$command_line\"

        return
    fi

    abcli_log_error "-abcli: docker: $task: command not found."
}
