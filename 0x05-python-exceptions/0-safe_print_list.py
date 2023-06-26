#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for item in my_list:
        counter = counter + 1
    try:
        if counter <= x:
            print("{}".format(item, end=""))
    except ValueError:
        print("x is greater than items count!")
    finally:
        return counter
