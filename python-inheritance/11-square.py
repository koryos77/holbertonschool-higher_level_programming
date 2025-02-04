#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation with size
        
        arguments:
            _size(int): Positive integer of the size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Public instance method that returns the area of the square.
        """
        return self.__size * self.__size
    
    def __str__(self):
        """
        Return a string representation of the Square.
        """
        return f"[Square] <width>/<height>"
