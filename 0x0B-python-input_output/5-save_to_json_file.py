#!/usr/bin/python3
"""Module that writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file,
    using a JSON representation"""
    with open(filename, 'w') as f:
        s = json.dump(my_obj, f)
