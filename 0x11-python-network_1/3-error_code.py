#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and
displays the body of the response
(decoded in utf-8).
"""
import sys
import urllib.request

req = urllib.request.Request(sys.argv[1])
try:
    with urllib.request.urlopen(req) as response:
        print(response.decode('UTF-8'))
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
