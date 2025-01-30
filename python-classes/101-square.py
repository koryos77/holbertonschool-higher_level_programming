class Square:
    """
    A class to represent a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): A tuple representing the position of the square in a 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square, a tuple of two positive integers.
                              Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The current position of the square as a tuple (x, y).
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of two integers representing the position.

        Raises:
            TypeError: If `value` is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(
            isinstance(i, int) and i >= 0 for i in value
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square using the `#` character, considering its size and position.
        """
        if self.size == 0:
            print("")
            return
        for _ in range(self.position[1]):
            print("")
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: The square drawn with `#` characters, considering its size and position.
        """
        output = ""
        if self.size == 0:
            return output
        for _ in range(self.position[1]):
            output += "\n"
        for _ in range(self.size):
            output += " " * self.position[0] + "#" * self.size + "\n"
        return output
