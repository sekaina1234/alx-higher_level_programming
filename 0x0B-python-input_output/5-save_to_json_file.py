#!/usr/bin/python3
"""Module: 5-save_to_json_file.py
Contains a function to save an object to a
text file in JSON format."""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file in JSON format.

    Args:
        my_obj: The object to be saved to the file.
        filename: The name of the file to save the object to.

    Raises:
        Exception: If the object cannot be serialized."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
