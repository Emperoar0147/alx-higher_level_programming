#!/usr/bin/python3
"""
the Script takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

url = sys.argv[1]

resp = requests.get(url)
x_request_id = resp.headers.get('X-Request-Id')
print(resp.headers.get("X-Request-Id"))
