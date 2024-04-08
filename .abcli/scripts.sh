#! /usr/bin/env bash

export abcli_path_scripts=$abcli_path_git/notebooks-and-scripts/scripts

export abcli_scripts_options=cat,dryrun

function scripts() {
    abcli_scripts "$@"
}

function abcli_scripts() {
    local task=$(abcli_unpack_keyword $1 help)

    local script_name=$2
    [[ "$task" == source ]] && local script_name=$3

    [[ -f "$abcli_path_scripts/$script_name.sh" ]] && local script_name=$script_name.sh
    local script_path=$abcli_path_scripts/$script_name

    if [ "$task" == "help" ]; then
        if [[ ! -z "$script_name" ]]; then
            abcli_log "🔗 $script_path"
            if [[ -f "$script_path" ]]; then
                abcli_scripts source - \
                    $script_name help
                return
            fi

            pushd $abcli_path_scripts >/dev/null
            local script_name_
            for script_name_ in $(ls $script_name/*); do
                abcli_scripts help \
                    $script_name_
            done
            popd >/dev/null
            return
        fi

        abcli_scripts cat "$@"
        abcli_scripts code "$@"

        abcli_show_usage "abcli scripts move|mv$ABCUL<script-name-1> <script-name-2>" \
            "<script-name-1> -> <script-name-2>"

        abcli_show_usage "abcli scripts source $EOP[$abcli_scripts_options]$EOPE$ABCUL<script-name> [<args>]" \
            "source <script-name>."
        return
    fi

    local function_name=abcli_scripts_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
    fi

    if [[ "$script_name" == help ]]; then
        case $task in
        cat)
            abcli_show_usage "abcli scripts cat$ABCUL<script-name>" \
                "cat <script-name>."
            ;;
        code)
            abcli_show_usage "abcli scripts code$ABCUL<script-name>" \
                "code <script-name>."
            ;;
        list | ls)
            abcli_show_usage "abcli scripts list|ls$ABCUL[meta|<prefix>]" \
                "list [meta] scripts."
            ;;
        esac
        return
    fi

    if [ "$task" == cat ]; then
        abcli_log_file $script_path
        return
    fi

    if [ "$task" == code ]; then
        # $script_path += .sh
        local script_path=$(python3 -c "print((lambda path: f'{path}.sh' if not path.endswith('.sh') else path)('$script_path'))")

        abcli_log "📜 $script_path"
        [[ ! -f "$script_path" ]] &&
            cp -v \
                $abcli_path_scripts/template.sh \
                $script_path
        code $script_path
        return
    fi

    if [[ ",ls,list," == *",$task,"* ]]; then
        if [[ "$script_name" == meta ]]; then
            local script_name=$3

            if [[ -z "$script_name" ]]; then
                abcli_log_list $(abcli_metadata get \
                    dict.keys,filename \
                    $abcli_path_scripts/meta.yaml) \
                    --before "📜" \
                    --after "meta script(s)"
                return
            fi

            local script_path_prefix=$(abcli_metadata get \
                key=$script_name.prefix,filename \
                $abcli_path_scripts/meta.yaml)

            if [ ! -d "$abcli_path_scripts/$script_path_prefix" ]; then
                abcli_log_error "-notebooks-and-scripts: meta scripts: $script_name: script not found."
                return 1
            fi

            pushd $abcli_path_scripts/$script_path_prefix >/dev/null
            local filename
            for filename in $(ls *.sh); do
                abcli_scripts help $script_path_prefix/$filename
            done
            popd >/dev/null

            return
        fi

        if [[ -f "$script_path" ]]; then
            abcli_log_file $script_path
        else
            abcli_log "🔗 $script_path"
            ls -1lh $script_path \
                "${@:3}"
        fi
        return
    fi

    if [[ ",mv,move," == *",$task,"* ]]; then
        local script_name_2=$3

        pushd $abcli_path_scripts >/dev/null
        abcli_eval - \
            git mv \
            $script_name \
            $script_name_2
        git status
        popd >/dev/null

        return
    fi

    if [ "$task" == source ]; then
        local options=$2

        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            abcli_scripts help \
                "$script_name" "${@:4}"
            return
        fi

        if [[ ! -f "$script_path" ]]; then
            abcli_log_error "-abcli: scripts: $task: $script_path: script not found."
            return 1
        fi

        do_cat=$(abcli_option_int "$options" cat 0)
        do_dryrun=$(abcli_option_int "$options" dryrun 0)

        [[ "$do_cat" == 1 ]] && abcli_log_file $script_path

        local args="${@:4}"
        [[ -z "$args" ]] && args="-"

        abcli_eval dryrun=$do_dryrun,~log \
            chmod +x $script_path
        abcli_eval dryrun=$do_dryrun \
            source $script_path "$args"
        return
    fi

    abcli_log_error "-abcli: scripts: $task: command not found."
    return 1
}

function abcli_script_show_usage() {
    abcli_show_usage "abcli_scripts source $EOP[$abcli_scripts_options]$EOPE$ABCUL$1" \
        "${@:2}"
}

function abcli_script_get() {
    local what=${1:-name}
    local script_full_path=${2:-"${BASH_SOURCE[1]}"}

    local prefix=$abcli_path_scripts
    local script_name=$(python3 -c "print('$script_full_path'.split('$prefix',1)[1] if '$script_full_path'.startswith('$prefix') else '')")

    local script_path=$(dirname "$script_full_path")

    case $what in
    "name")
        echo $script_name
        ;;
    "path")
        echo $script_path
        ;;
    *)
        echo "unknown-$what"
        ;;
    esac
}
