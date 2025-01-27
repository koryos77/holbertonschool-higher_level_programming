#!/usr/bin/python3
"""
Module that defines a class Square.
This module contains the definition of Square with an attribute 'size'
"""


class Square:
    """
    Class Square.

    Argument:
        __size (int): size of a side of the square.

    Method:
        __init__(self, size): Initialize a square with a given size
    """
    def __init__(self, size):
        """
        Initialization of the class Square withe the size

        Arguments:
            size (int): Size of a side of the square
        """
        self.__size = size
