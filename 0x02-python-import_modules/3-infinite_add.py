#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args_count = len(sys.argv) - 1
    result = 0
    for i in range(args_count):
        result += int(sys.argv[i + 1])
    print(result)
