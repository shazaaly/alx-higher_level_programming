#!/usr/bin/python3
for i in range(0, 98):
    if i < 10:
        print("0x0{}".format(i))
    elif i >= 10 and i < 16:
        print("0x0{}".format(chr(i + 87)))
    else:
        print("0x{:02x}".format(i))
