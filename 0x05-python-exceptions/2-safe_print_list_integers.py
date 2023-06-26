#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        count += 1
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")

    except (ValueError, TypeError):
        pass
    print()
    return count
