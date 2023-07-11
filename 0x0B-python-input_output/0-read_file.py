#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read. Default is an empty string."""
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read()
        print(contents, end='')
