#!/usr/bin/python3
"""
Module Square.
This module defines a Square class for representing a square with various operations.
"""


class Square:
    """ Square class defined by geometric shape
        Attributes:
        size (int): Size of square
        position (tuple): Position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
            position (tuple): position of the square
        Returns:
            None
        """
        self.size = size  # using the setter method for validation
        self.position = position  # using the setter method for validation

    def area(self):
        """
        set square area
        Return:
            the current square area (int)
        """
        return self.__size ** 2

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

    @property
    def position(self):
        """
        getter of position
        Return:
            Position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter of position
        Args:
            value (tuple): position of the square
        Raises
            TypeError: if position is not a tuple of 2 positive integers
        Returns:
            None
        """
        if (type(value) is not tuple or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Prints in stdout the square with the character #
        If size is equal to 0, prints an empty line

        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)


if __name__ == "__main__":
    Square = __import__('6-square').Square
    
    my_square_1 = Square(5, (3, 2))
    my_square_1.my_print()

    print("--")
