#! /usr/bin/env bash

function abcli_docker_build() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="${EOP}dryrun,~push,run,verbose$EOPE"
        abcli_show_usage "@docker build$ABCUL$options" \
            "build the abcli docker image."
        return
    fi

    abcli_log "@docker: build $options ..."

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_push=$(abcli_option_int "$options" push $(abcli_not $do_dryrun))
    local do_run=$(abcli_option_int "$options" run 0)
    local verbose=$(abcli_option_int "$options" verbose 0)

    pushd $abcli_path_git >/dev/null

    mkdir -p temp
    cp -v ~/.kaggle/kaggle.json temp/

    local extra_args=""
    [[ "$verbose" == 1 ]] &&
        extra_args="$extra_args --progress=plain"

    abcli_eval ,$options \
        docker build \
        $extra_args \
        --build-arg HOME=$HOME \
        -t kamangir/abcli \
        -f notebooks-and-scripts/Dockerfile \
        .
    [[ $? -ne 0 ]] && return 1

    rm -rfv temp

    [[ "$do_push" == "1" ]] &&
        abcli_docker_push $options

    [[ "$do_run" == "1" ]] &&
        abcli_docker_run $options

    popd >/dev/null
}
