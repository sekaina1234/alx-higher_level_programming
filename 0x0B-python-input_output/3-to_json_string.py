#!/usr/bin/python3
"""Module: 3-to_json_string.py
Contains a function to convert an object
to its JSON representation.
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        A string representing the JSON
        representation of the object."""
    return json.dumps(my_obj)
