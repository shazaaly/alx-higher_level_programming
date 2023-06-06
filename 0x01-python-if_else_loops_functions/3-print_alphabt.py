#!/usr/bin/python3
for char in range(97, 123):
    if (chr(char) == "q" or chr(char) == "e"):
        pass
    else:
        print("{}".format(chr(char)), end="")
