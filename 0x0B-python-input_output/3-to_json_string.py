#!/usr/bin/python3
"""Module for converting an object to
its JSON representation."""


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object."""
    return str(my_obj).replace("'", '"')
