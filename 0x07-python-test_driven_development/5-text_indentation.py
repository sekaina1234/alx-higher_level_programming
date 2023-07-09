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

    chars = ['.', '?', ':']
    result = ""
    for char in text:
        result += char
        if char in chars:
            result += "\n\n"

    lines = result.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    result = "\n".join(lines)
    print(result)
