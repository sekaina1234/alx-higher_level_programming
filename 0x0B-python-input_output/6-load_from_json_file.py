#!/usr/bin/python3
"""Module: 6-load_from_json_file.py
Contains a function to create an
object from a JSON file."""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename: The name of the JSON file
        to load the object from.

    Returns:
        The Python object created from the JSON data.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        JSONDecodeError: If the JSON file contains
        invalid data."""
    with open(filename, 'r') as file:
        return json.load(file)
