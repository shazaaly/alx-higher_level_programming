#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        user_id = response.json().get("id")
        print(user_id)
    else:
        print(None)
