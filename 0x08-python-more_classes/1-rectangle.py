#!/usr/bin/python3
"""Defines a UniqueRectangle class."""


class UniqueRectangle:
    """Represent a unique rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new UniqueRectangle.

        Args:
            width (int): The width of the new unique rectangle.
            height (int): The height of the new unique rectangle.
        """
        self.set_width(width)
        self.set_height(height)

    def set_width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def get_width(self):
        """Get the width of the rectangle."""
        return self.__width

    def set_height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def get_height(self):
        """Get the height of the rectangle."""
        return self.__height
