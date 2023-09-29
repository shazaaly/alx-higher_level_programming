#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        content_decode = content.decode('UTF-8')
        content_type = type(content)
        print('Body response:')
        print(f"\t- type: {content_type}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content_decode}")
