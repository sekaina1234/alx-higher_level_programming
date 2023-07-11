#!/usr/bin/python3
"""Module: 8-class_to_json
Contains a function that converts an instance
of a class to a dictionary representation
with simple data structures for JSON serialization."""


def class_to_json(obj):
    """Converts an object to a dictionary representation
    with simple data structures.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representation of the object
        with serializable data types."""
    attributes = obj.__dict__
    json_dict = {}
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
