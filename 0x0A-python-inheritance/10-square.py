#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a special kind of rectangle"""

    def __init__(self, size):
        """Initializes a Square object
        Args:
            size (int): The size of the square's sides"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Computes the area of the square
        Returns:
            The area of the square"""
        return (self.__size ** 2)
