#!/bin/bash
filename=$2
curl -s -X POST -H "Content-Type: application/json" -d "$json" "$1"
