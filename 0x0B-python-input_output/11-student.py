#!/usr/bin/python3
"""Module that contains Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            x = {}
            for a in attrs:
                if a in self.__dict__:
                    x[a] = self.__dict__[a]
            return x
        return self.__dict__

    def reload_from_json(self, json):
        for a in json:
            self.__dict__[a] = json[a]
