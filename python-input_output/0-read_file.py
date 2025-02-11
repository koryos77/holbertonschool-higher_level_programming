#!/usr/bin/python3


def read_file(filename=""):
    """
    Function that reads a text file in UTF-8 and prints it.

    argument:
        filename: the file we want to read and print.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
