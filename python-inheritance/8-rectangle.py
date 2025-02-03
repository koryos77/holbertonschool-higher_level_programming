#!/usr/bin/python3
"""
Class Rectangle
"""
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class REctangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height

        arguments:
            _width: positive integer
            _height: positive integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
