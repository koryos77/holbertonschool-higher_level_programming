#!/usr/bin/python3
"""
This module provides a function `print_square` that prints a square.

The function takes a value, and prints a square.
It raises a TypeError if the inputs are not strings,
or a ValueError if the size us 0.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The length of the square's side.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
