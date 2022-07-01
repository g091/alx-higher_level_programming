#!/usr/bin/python3
"""Function that adds ints only"""


def add_integer(a, b=98):
    """Checking for types that are not int & float"""

    if not isinstance(a, (int, float)):

        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    """Changing floats to ints"""

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
