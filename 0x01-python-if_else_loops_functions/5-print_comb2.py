#!/usr/bin/python3
for i in range(100):
    if i < 99:
        print("%02d" % (i), end=", ")
    else:
        print("%02d" % (i), end=" ")
