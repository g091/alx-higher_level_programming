#!/usr/bin/python3
"""Module contains the Base class"""
import json


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the Base class
        Args:
            id: the uniqe id
        """
        if id is None:
            Base.__nb_objects += 1
            id = self.__nb_objects

        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of the instance
        Args:
            list_dictionaries: the list of dictionaries
        """
        if not list_dictionaries or len(list_dictionaries) is 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        Args:
            cls: the reference to the class
            list_objs: the list of objects to save
        """
        content = []

        if list_objs is not None:
            for i in list_objs:
                content.append(cls.to_dictionary(i))

        with open(cls.__name__ + ".json", "w", encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation
        Args:
            json_string: string representing a list of dictionaries
        """
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set
        Args:
            cls: the reference to the class
            dictionary: the double pointer to a dictionary
        """
        if cls.__name__ is "Square":
            temp = cls(42)  # can't be called without attributes
        if cls.__name__ is "Rectangle":
            temp = cls(42, 42)  # can't be called without attributes

        temp.update(**dictionary)  # pass the dictionary as a double pointer

        return temp

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances
        Args:
            cls: the reference to the class
        """
        try:
            with open(cls.__name__ + ".json", "r") as a_file:
                content = cls.from_json_string(a_file.read())

                result = []
                for el in content:
                    result.append(cls.create(**el))

                return result

        except FileNotFoundError:
            return []
