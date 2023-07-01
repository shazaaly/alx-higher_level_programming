def add_integer(a, b=98):
    """
    Args: a, b
    Return sum of 2 numbers
    >>> add_integer(3, 4)
    7
    >>> add_integer(3.3, 4)
    7
    >>> add_integer(3, 4.1)
    7
    >>> add_integer('3', 4)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "0-add_integer.py", line 7, in add_integer
    raise TypeError("a must be an integer or float")
    TypeError: a must be an integer or float
    >>> add_integer(3, '4')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "0-add_integer.py", line 7, in add_integer
    raise TypeError("a must be an integer or float")
    TypeError: a must be an integer or float
    """
    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, (int)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int)):
        raise TypeError("b must be an integer or float")
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
