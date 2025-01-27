#!/usr/bin/python3
"""
A new function
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first integer to be added.
    If float, it will be casted to integer.
    b (int or float): The second integer to be added.
    If float, it will be casted to integer. Defaults to 98.

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or a float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
