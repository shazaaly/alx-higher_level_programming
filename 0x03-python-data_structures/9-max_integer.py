def max_integer(my_list=[]):
    max_num = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max_num:
            max_num = my_list[i]

    return (max_num)
