#!/usr/bin/python3
"""Contains LockedClass that prevents the user from dynamically
creating new instance attributes"""


class LockedClass:
    """Prevents dynamic attribute"""
    __slots__ = ['first_name']
