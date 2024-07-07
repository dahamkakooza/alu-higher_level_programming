#!/usr/bin/python3
"""
Module Square.
This module defines a Square class for representing a square with various operations.

"""


class Square:
    """Square class defined by geometric shape
    Attributes:
    size (int): Size of square
    """

    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size  # using the setter method for validation

    def area(self):
        """
        set square area
        Return:
            the current square area (int)
        """
        return self.__size**2

    @property
    def size(self):
        """
        getter of size
        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size
        Args:
            value (int): size of a side of the square
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints in stdout the square with the character #
        If size is equal to 0, prints an empty line

        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)


if __name__ == "__main__":
    Square = __import__("5-square").Square

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()
    print("--")
