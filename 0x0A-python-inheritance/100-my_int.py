#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """Represents a rebel integer"""

    def __eq__(self, other):
        """Checks if the value is not equal to other"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Checks if the value is equal to other"""
        return super().__eq__(other)
