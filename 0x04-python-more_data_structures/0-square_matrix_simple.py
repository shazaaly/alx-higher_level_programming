def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    my_martix = []
    for rows in matrix:
        my_martix.append(list(map(lambda x: x**2, rows)))

    return (my_martix)
