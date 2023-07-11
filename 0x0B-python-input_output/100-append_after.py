#!/usr/bin/python3
"""Module: 100-append_after

Contains a function that inserts a line of text into a file
after each line containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text into a file after each
    line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after
        each line containing the search string."""
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
