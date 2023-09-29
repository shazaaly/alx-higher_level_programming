#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        cont_type = type(content)
        decoded = content.decode('UTF-8')
        print("Body response:")
        print("\t- type: {}".format(cont_type))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(decoded))
