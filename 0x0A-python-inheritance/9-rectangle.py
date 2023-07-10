#!/usr/bin/python3
"""Defines a class Rectangle that inherits
from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() representation of a Rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return ("[{}] {}/{}".format(self.__class__.__name__,
            self.__width, self.__height))
