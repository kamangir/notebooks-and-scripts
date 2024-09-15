#! /usr/bin/env bash

function mission_patch() {
    local options=$1

    local version="2.16.1"

    local script_name=$(abcli_script_get name)
    local script_path=$(abcli_script_get path)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local extra_options="dryrun,height=<1024>,~upload,url=<url>,width=<1024>"
        extra_options="$EOP$extra_options$EOPE"
        local options="app=openai_commands|blue_stability,count=<1>,open,$extra_options"
        abcli_script_show_usage "$script_name$ABCUL[$options]$ABCUL[<object-name>]$EARGS" \
            "generate mission patches for <url>."
        return
    fi

    openai_commands init

    local url=$(abcli_option "$options" url https://earthdaily.com/constellation/)
    local count=$(abcli_option_int "$options" count 1)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_open=$(abcli_option_int "$options" open 0)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 $(abcli_string_timestamp))

    local description=$(aiart html ingest_url $url \
        --fake_agent 1)
    abcli_log "📜 $description"

    # necessary because of assumptions in openai_commands and aiart :(
    abcli_select $object_name ~trail
    [[ "$do_open" == 1 ]] && open .

    local index
    for ((index = 1; index <= count; index++)); do
        local prompt=$(openai_commands complete "describe the following in three sentences: $description")
        local prompt=$(echo "$prompt" | tr "'" " ")
        abcli_log "📜 $prompt"

        aiart generate image \
            $(abcli_option_subset \
                "$options" \
                app=openai_commands,~dryrun,height=1024,width=1024) \
            $object_name-$(python3 -c "print('{:05d}'.format($index))") - \
            "generate a mission patch for the following: $prompt"
    done

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    abcli_tags set \
        $object_name mission-patch
}

mission_patch "$@"
