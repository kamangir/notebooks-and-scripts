#! /usr/bin/env bash

function vanwatch_analyze() {
    rm -v *.jpg
    rm -v *.geojson

    vanwatch ingest vancouver - \
        --count 5
}

vanwatch_analyze "$@"
