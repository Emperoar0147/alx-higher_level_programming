#!/usr/bin/python3
"""
this iz a Script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

url = "https://api.github.com/user"

response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    user_info = response.json()
    print(user_info['id'])
else:
    print("None")
