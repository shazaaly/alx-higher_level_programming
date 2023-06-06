#!/usr/bin/python3
def uppercase(str):

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upper = ord(i) - 32
