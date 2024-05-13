#!/bin/bash
# Send a request to the URL and get the body size
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
