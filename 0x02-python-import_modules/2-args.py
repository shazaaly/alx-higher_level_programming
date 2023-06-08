#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import sys

=======

if __name__ == "__main__":
    import sys

>>>>>>> 2a32b679851cacca1351b024f4c7ffd7eb42be54
    args = len(sys.argv) - 1
    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args))

    for i in range(args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
