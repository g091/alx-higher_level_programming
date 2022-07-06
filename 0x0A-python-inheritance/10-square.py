#!/usr/bin/python3
"""Write a class Square that inherits Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square extends Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Finds the area of a square"""
        return self.__size ** 2
