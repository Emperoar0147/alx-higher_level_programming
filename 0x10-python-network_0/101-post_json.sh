#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument
curl -s -X POST -H "Content-Type: application/json" -d "$json" "$1"
