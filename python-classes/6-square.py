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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization of the Square class with the size.

        Arguments:
            size (int): size of a side of the square
            position (tuple): represent the position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.

        Arguments:
            value (tuple): a tuple where x and y are positive ints

        Raises:
            TypeError: If position is not a tuple of 2 ints.
            ValueError: If any element of the position tuple is less than 0
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value) or \
                value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Method that returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method that print in stdout the square with #
        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
            return
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
