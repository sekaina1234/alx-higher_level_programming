#!/usr/bin/python3
"""Module: 9-student

Contains a class Student that defines a student and provides a method
to retrieve a dictionary representation of the student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation
        of the Student instance.

        Returns:
            dict: A dictionary representation
            of the Student instance."""
        attributes = self.__dict__
        json_dict = {}
        for key, value in attributes.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value
        return json_dict
