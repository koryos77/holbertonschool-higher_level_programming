#!/usr/bin/python3
"""
This module provides a function `text_indentation` that prints a text with
specific formatting.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip(), end="")
