#!/usr/bin/python3
"""Module that contains the MyList class"""


class MyList(list):
    """Subclass that inherits from the list"""
    def __init__(self):
        """Initialize"""
        super().__init__()

    def print_sorted(self):
        """Prints the list in a sorted order"""
        print(sorted(self))
