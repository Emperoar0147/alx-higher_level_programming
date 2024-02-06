#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (float or int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.size ** 2

    def __lt__(self, other):
        """Less than comparison operator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparison operator."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal to comparison operator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal to comparison operator."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison operator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison operator."""
        return self.area() >= other.area()
