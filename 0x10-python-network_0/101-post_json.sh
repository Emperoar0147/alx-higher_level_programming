#!/bin/bash
filename=$2
if ! [ -f "$filename" ]; then
    echo "File $filename not found"
    exit 1
fi
json=$(cat "$filename")
curl -s -X POST -H "Content-Type: application/json" -d "$json" "$1"
