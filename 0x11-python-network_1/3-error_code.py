#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).

Handles urllib.error.HTTPError exceptions and prints: Error code: followed by the HTTP status code
"""

import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
