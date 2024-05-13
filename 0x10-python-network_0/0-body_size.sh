#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
# Send a request to the URL and get the body size
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
