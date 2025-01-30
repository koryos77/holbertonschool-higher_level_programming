#!/usr/bin/python3
class Square:
    """
    A class to represent a square.

    Attributes:
        size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (float or int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            float or int: The current size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The size to set.

        Raises:
            TypeError: If `value` is not a number (int or float).
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.size ** 2

    def __lt__(self, other):
        """
        Less-than comparison based on area.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of the current
            square is less than the other.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less-than-or-equal comparison based on area.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of the current square
            is less than or equal to the other.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """
        Equal comparison based on area.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of the current square is equal to the other.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Not-equal comparison based on area.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of the current
            square is not equal to the other.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater-than comparison based on area.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of the current
            square is greater than the other.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater-than-or-equal comparison based on area.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of the current square
            is greater than or equal to the other.
        """
        return self.area() >= other.area()
