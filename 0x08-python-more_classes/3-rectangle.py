#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of rectangle"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Calculates the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = (2 * self.__width) + (2 * self.__height)
        return perimeter

    def __str__(self):
        """Prints the rectangle with the `#` character."""
        result = ""

        if self.__height == 0 or self.__width == 0:
            return result
        for i in range(0, self.__height):
            result += "{:s}".format(self.__width * "#")
            if i + 1 is not self.__height:
                result += "\n"
        return result
