#!/usr/bin/python3
"""
Module: base
Defines the Base class.
"""


import json


class Base:
    """
    Represents the base class for all other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.
        Args:
            id (int): The unique identifier of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string representation.
        Args:
            list_dictionaries (list): The list of dictionaries to convert.
        Returns:
            str: The JSON string representation of the list
            of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of instances to a file in JSON format.
        Args:
            list_objs (list): The list of instances to save.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string representation to a list of dictionaries.
        Args:
            json_string (str): The JSON string to convert.
        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all attributes already set.
        Args:
            **dictionary: Double pointer to a dictionary of attributes.
        Returns:
            Base: The created instance.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a file in JSON format.
        Returns:
            list: The list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares
        using Turtle graphics.
        Args:
            list_rectangles (list): The list of Rectangle instances.
            list_squares (list): The list of Square instances.
        """
        import turtle

        turtle.setup(width=800, height=600)
        turtle.bgcolor("white")
        turtle.title("Drawing Rectangles and Squares")

        pen = turtle.Turtle()
        pen.speed(1)
        pen.pensize(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("blue")
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            pen.forward(square.width)
            pen.left(90)
            pen.forward(square.height)
            pen.left(90)
            pen.forward(square.width)
            pen.left(90)
            pen.forward(square.height)
            pen.left(90)

        turtle.done()
