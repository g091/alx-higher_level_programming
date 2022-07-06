#!/usr/bin/python3
"""Defines the `add_attribute` function"""


def add_attribute(obj, att, value):
    """Adds a new attribute of `value` to object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
