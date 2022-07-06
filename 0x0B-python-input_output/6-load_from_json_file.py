#!/usr/bin/python3
"""Module that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """Writes an Object to a text file,
    using a JSON representation"""
    with open(filename, 'r') as f:
        return(json.load(f))
