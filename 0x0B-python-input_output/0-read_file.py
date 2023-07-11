#!/usr/bin/python3
"""Module for reading and printing the contents of a text file."""


def read_file(filename=""):
    """Function that reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the text file to be read.
        Defaults to an empty string."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
