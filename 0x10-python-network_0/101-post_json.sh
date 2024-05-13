#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument
# It uses the contents of a file passed as the second argument in the body of the request
# It displays the body of the response

filename=$2

if ! [ -f "$filename" ]; then
    echo "File $filename not found"
    exit 1
fi

json=$(cat "$filename")

curl -s -X POST -H "Content-Type: application/json" -d "$json" "$1"
