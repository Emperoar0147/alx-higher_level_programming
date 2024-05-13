#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" -o /tmp/body.txt && cat /tmp/body.txt
