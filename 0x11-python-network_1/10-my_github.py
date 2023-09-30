#!/usr/bin/python3
""" A Python script that takes your GitHub
credentials (username and personal access token)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"

    # Set the authentication token in the request headers
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    basic = HTTPBasicAuth(username=sys.argv[1], password=sys.argv[2])
    r = requests.get(url, auth=basic)

    res = r.json()
    user_id = res.get("id")
    print(user_id)
