#!/usr/bin/python3
def uppercase(str):
    res = ""

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upper = ord(i) - 32
            res += chr(upper)
        else:
            res += i
    print("{}".format(res), end="\n")
