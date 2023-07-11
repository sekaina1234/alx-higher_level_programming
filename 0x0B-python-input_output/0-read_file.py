#!/usr/bin/python3
"""
Module: 0-read_file
"""

def read_file(filename=""):
    """
    Prints the contents of a UTF8 text file to stdout.

    Args:
        filename (str): The name of the file to be read. Default is an empty string.
    """
    try:
        file = open(filename, 'r', encoding='utf-8')
        contents = file.read()
        print(contents, end='')
        file.close()
    except FileNotFoundError:
        pass
