#!/usr/bin/python3
"""
This module defines a Square class with size validation and area calculation.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a Square with optional size (default 0).

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2
