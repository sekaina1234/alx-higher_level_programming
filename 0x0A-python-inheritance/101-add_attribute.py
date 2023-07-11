#!/usr/bin/python3
"""Module for add_attribute function"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible
    Args:
        obj (object): The object to add the attribute to
        attr (str): The name of the attribute
        value (any): The value of the attribute
    Raises:
        TypeError: If the attribute cannot be added to the object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
