#!/usr/bin/python3
""" Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}

dat_encode = urllib.parse.urlencode(data).encode('UTF-8')
req = urllib.request.Request(url, dat_encode)
with urllib.request.urlopen(req) as response:
    res = response.read()
    print(f"Your email is: {res}")
