#! /usr/bin/env bash

function vanwatch_ingest_and_analyze() {
    rm -v *.jpg
    rm -v *.geojson

    vanwatch ingest vancouver - \
        --count 5
}

vanwatch_ingest_and_analyze "$@"
