#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args == 1:
        print("1 argument:")
    elif args > 1:
        print("{} arguments:".format(args))
    else:
        print("0 arguments")
    for i in range(args):
        print("{}:{}".format(i + 1, sys.argv[i + 1]))
