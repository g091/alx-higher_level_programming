#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle class defined by width and height"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcu;ates the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calcu;ates the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Prints the rectangle with the character #"""
        res = ""
        if self.__width == 0 or self.__height == 0:
            return s
        for i in range(self.__height):
            res += ("#" * self.__width)
            if i != self.__height - 1:
                res += "\n"
        return res

    def __repr__(self):
        """Returns str rep of rectangle able to recreate
        a new instance by using eval()"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
