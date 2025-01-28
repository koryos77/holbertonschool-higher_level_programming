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
        size (property): getter for the size
        size (property setter): setter for the size, with validation
        area(self): returns the area of the square
        my_print(self): Print a square with #
    """

    def __init__(self, size=0):
        """
        Initialization of the Square class with the size.

        Arguments:
            size (int): size of a side of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square. Ensures that the size
        is an integer and that it is greater or equal to 0.

        Arguments:
            value (int): the size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Method that returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method that print in stdout the square with #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
