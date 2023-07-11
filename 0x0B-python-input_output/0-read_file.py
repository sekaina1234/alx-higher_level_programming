#!/usr/bin/python3
"""
Module: 0-read_file
"""

def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read. Default is an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the contents of the file
        contents = file.read()

        # Print the contents to stdout
        print(contents, end='')
