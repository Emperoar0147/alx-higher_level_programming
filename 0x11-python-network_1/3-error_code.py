#!/usr/bin/python3
"""
a Script that takes in a URL, sends a request to the URL and displays the body
of the response.

it Handles urllib.error.HTTPError exceptions and prints: Error code: followed by the HTTP status code
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
