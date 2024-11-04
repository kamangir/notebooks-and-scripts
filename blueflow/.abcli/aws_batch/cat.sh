#! /usr/bin/env bash

function abcli_aws_batch_cat() {
    local options=$1

    local job_id=$2

    abcli_aws_batch_browse cat,id=$job_id,log
}
