#!/bin/bash
filename=$2
json=$(cat "$filename")
curl -s -X POST -H "Content-Type: application/json" -d "$json" "$1"
