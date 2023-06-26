#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{}".format(my_list[i]), end="")
                count += 1

    except (ValueError, TypeError):
        pass
    print()
    return count
