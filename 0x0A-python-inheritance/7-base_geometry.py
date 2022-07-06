#!/usr/bin/python3
"""Module that contains BaseGeometry class"""


class BaseGeometry:
    """The BaseGeometry class"""
    def area(self):
        """Finds the area else raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if of type int and if > than 0"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
