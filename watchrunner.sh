#!/bin/bash

w_file=$1
w_action=$2
w_sum=''

if [[ -z "${w_file}" || -z "${w_action}" ]]; then
    echo Usage: $0 FILENAME COMMAND
    exit 1;
fi

function run_action {
    w_sum=`md5sum $w_file`
    $w_action $w_file
}

run_action

while true; do
    if [[ $w_sum != `md5sum $w_file` ]]; then
        run_action
    fi
    sleep 1
done
