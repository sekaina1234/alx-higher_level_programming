#!/usr/bin/python3
"""Module: 4-from_json_string.py
Contains a function to convert a JSON string
to a Python object."""


import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str: The JSON string to be converted.

    Returns:
        A Python object representing the JSON data.

    Raises:
        ValueError: If the JSON string is not valid."""
    return json.loads(my_str)
