#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""


import requests
response = requests.get('https://alx-intranet.hbtn.io/status')

if response.status_code == 200:
    content = response.text
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(content), content))
