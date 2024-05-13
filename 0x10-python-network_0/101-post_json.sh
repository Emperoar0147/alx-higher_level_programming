#!/bin/bash
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1" | grep "Valid JSON" && echo "Valid JSON" || echo "Not a valid JSON"
