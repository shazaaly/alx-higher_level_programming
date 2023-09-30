#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly
JSON formatted and not empty, display the
id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
"""

if __name__ == "__main__":
    import requests
    import sys
    q = sys.argv[2] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"

    r = requests.post(url, data={"q": q})
    try:
        resp = r.json()
        if resp:
            print(f"[{resp.get('id')}] {resp.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
