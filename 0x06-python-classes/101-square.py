#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) for num in value) \
                or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()

            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Returns a string representation of the square."""
        result = ""
        if self.size == 0:
            result += "\n"
        else:
            for _ in range(self.position[1]):
                result += "\n"

            for _ in range(self.size):
                result += " " * self.position[0] + "#" * self.size + "\n"
        return result.rstrip()
