#!/usr/bin/python3
"""
This module contains a Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class used to represent a square, inheriting from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a new square instance
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
