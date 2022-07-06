#!/usr/bin/python3
"""Contains MyInt class that inherits int"""


class MyInt(int):
    """MyInt class"""
    def __new__(cls, *args, **kwargs):
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Equals"""
        return int(self) != other

    def __ne__(self, other):
        """Not equals"""
        return int(self) == other
