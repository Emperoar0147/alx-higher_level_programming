#!/bin/bash

curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1" | grep -q "Not a valid JSON" && echo "Not a valid JSON" || echo "Valid JSON"
