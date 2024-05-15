#!/usr/bin/python3
"""
this Script lists 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails” using the GitHub API
"""

import requests
import sys

repo_name = sys.argv[1]
owner_name = sys.argv[2]

if __name__ == "__main__":
url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
params = {'per_page': 10}

response = requests.get(url, params=params)

if response.status_code == 200:
    commits = response.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
else:
    print("Error:", response.status_code)
