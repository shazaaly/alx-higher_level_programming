#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv) - 1
if args == 1:
    print("1 argument:")
    print("1: ", sys.argv[1])
elif args > 1:
    print("{} arguments:".format(len(sys.argv)))
    for i in range(args):
        print("{:d}:{:s}".format(i + 1, sys.argv[i]))

else:
    print("0 arguments")
