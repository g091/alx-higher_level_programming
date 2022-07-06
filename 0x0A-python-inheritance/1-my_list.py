#!/usr/bin/python3
""" Module that contains the MyList class"""


class MyList(list):
    """Sublass that inherits from the list"""
    def print_sorted(self):
        """Prints the list in a sorted order"""
        print(sorted(self))
