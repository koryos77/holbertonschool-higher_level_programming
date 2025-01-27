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
        area(self): returns the area of the square
    """
    def __init__(self, size=0):
        """
        Initialization of the class Square withe the size

        Arguments:
            size (int): Size of a side of the square

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Method that returns the current square area
        """
        return self.__size ** 2
