#!/usr/bin/python3
"""
Module that defines a class Rectangle
"""

class Rectangle:
    """
    Class Rectangle.
    Arguments:
        __width (int): width of the rectangle
        __height (int): height of the rectangle

    Method:
        __init__(self, width=0, height=0): Initialize the width and height
        of the rectangle.
        width (property): getter for the width
        height (property): getter for the height
        width (property setter): setter for the width
        height (property setter): setter for the height
    """

    def __init__(self, width=0, height=0):
        """
        Initialization of the Rectangle class with the width and height

        Arguments:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Method to print the rectangle with `#` character.
        If width or height equals zero, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ("#" * self.__width + '\n') * self.__height
        return rect

    @property
    def width(self):
        """
        Getter for the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle. Ensure that
        the width is an integer and that it is greater or equal to 0

        Arguments:
            value (int): the width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle. Ensure that
        the height is an integer and that it is greater or equal to 0

        Arguments:
            value (int): the height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Method that returns the current rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Method that returns the current rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"
