#!/usr/bin/python3
""" Module that prints a given first name and last name."""


def say_my_name(first_name, last_name=""):
    """Prints a string my name is <first_name>  <last_name>"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name = print("My name is {:s} {:s}".format(first_name, last_name))
    return name
