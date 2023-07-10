#!/usr/bin/python3
"""This module defines a class called BaseGeometry."""


class BaseGeometry:
    """A base class for geometry-related operations."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
