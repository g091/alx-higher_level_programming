#!/usr/bin/python3
"""Respresents a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        self.__size = size
        if size is not int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
