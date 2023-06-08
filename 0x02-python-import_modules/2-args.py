#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args == 1:
        print("1 argument:")
    elif args > 1:
        print("{} arguments:".format(args))
        for i in range(args):
            print("{:d}:{:s}".format(i + 1, sys.argv[i + 1]))
    else:
        print("0 arguments")
