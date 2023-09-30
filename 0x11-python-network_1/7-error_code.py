#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
