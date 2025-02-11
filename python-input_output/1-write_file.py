#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    Function that writes a string from a text file and returns
    the number of character written.

    Arguments:
        filename: the file we'll take the strinfg from
        text: the string we'll write

    Returns:
        The number of character written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return len(text)
