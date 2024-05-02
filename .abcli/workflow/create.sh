#! /usr/bin/env bash

function notebooks_and_scripts_workflow_create() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        list_of_patterns=$(python3 -m notebooks_and_scripts.workflow.patterns list --delim \|)
        list_of_runners=$(python3 -m notebooks_and_scripts.workflow.runners list --delim \|)
        options="${EOP}dryrun,${EOPE}pattern=$list_of_patterns,submit_to=$list_of_runners$EOP,~upload,~verbose"
        abcli_show_usage "@workflow create$ABCUL$options$ABCUL-|<job-name>$ABCUL<command-line>$EOPE" \
            "create a <command-line> workflow."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_submit=$(abcli_option_int "$options" submit 1)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local do_verbose=$(abcli_option_int "$options" verbose 1)

    local pattern=$(python3 -m notebooks_and_scripts.workflow.patterns list --count 1)
    pattern=$(abcli_option "$options" pattern $pattern)

    local job_name=$(abcli_clarify_object $2 workflow-$pattern-$(abcli_string_timestamp_short))

    local command_line="${@:3}"
    [[ -z "$command_line" ]] && command_line="$(abcli unquote $ABCLI_AWS_BATCH_DEFAULT_WORKFLOW_COMMAND)"

    abcli_log "creating workflow: $command_line -$pattern-> $job_name"

    python3 -m notebooks_and_scripts.workflow \
        create \
        --command_line "$command_line" \
        --dryrun $do_dryrun \
        --job_name $job_name \
        --pattern "$pattern" \
        --submit $do_submit \
        --verbose $do_verbose

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    return 0
}
