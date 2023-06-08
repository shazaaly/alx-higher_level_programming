#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("1 argument:")
    print("1: ", sys.argv[0])
elif len(sys.argv) > 1:
    print("{} arguments:".format(len(sys.argv)))
    for index, arg in enumerate(sys.argv):
        print("{}:{}".format(index, sys.arg))

else:
    print("0 arguments")
