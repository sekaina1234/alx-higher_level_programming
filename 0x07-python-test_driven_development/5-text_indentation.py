#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    add_newline = False

    for char in text:
        if add_newline:
            if char not in ".?:\n":
                result += "\n"  # Add new line after punctuation
            add_newline = False

        if char == "\n":
            result += "\n\n"  # Add two new lines after existing new lines
            add_newline = False
        elif char in ".?:":
            result += char
            add_newline = True
        else:
            result += char

    print(result)

text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque interdum consequat magna, et fringilla est suscipit in. Nulla commodo felis ac lacus lacinia convallis. Mauris at tincidunt diam? Sed a quam pretium, lacinia sem quis, posuere velit. Pellentesque pulvinar ornare risus, sed venenatis odio tempor at.")
