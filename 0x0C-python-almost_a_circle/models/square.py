#!/usr/bin/python3
"""Module: square
Defines the Square class that inherits from Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.
    Inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square's sides.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The unique identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets or sets the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}"
    .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
