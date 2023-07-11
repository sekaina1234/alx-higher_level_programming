#!/usr/bin/python3
"""Module: 10-student

Contains a class Student that defines a student and provides
a method to retrieve a dictionary representation of the student."""


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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): A list of attribute names to be retrieved.
                If None, all attributes are retrieved.

        Returns:
            dict: A dictionary representation of the Student instance
                  containing the requested attributes."""
        if attrs is None:
            return self.__dict__

        json_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                json_dict[attr] = self.__dict__[attr]
        return json_dict
