#!/usr/bin/python3
"""
This module defines a class
"""


class Rectangle:
    """
    This class has two attributes
    """

    def __init__(self, width=0, height=0):
        """
        instantiates width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        function to return width if setter checks have passed
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter validates if value is >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
            self.__width = value

    @property
    def height(self):
        """
        function to return height if setter checks have passed
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter validates if value is >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
            self.__height = value
# Test cases
myrectangle = Rectangle(2, 4)
print(sorted(myrectangle.__dict__))
# Expected: {'_Rectangle__height': 4, '_Rectangle__width': 2}

print(myrectangle.width)
# Expected: 2

print(myrectangle.height)
# Expected: 4

myrectangle = Rectangle(4)
print("{} - {}".format(myrectangle.width, myrectangle.height))
# Expected: 4 - 0

myrectangle = Rectangle()
print("{} - {}".format(myrectangle.width, myrectangle.height))
# Expected: 0 - 0

myrectangle = Rectangle(2, 4)
print("{} - {}".format(myrectangle.width, myrectangle.height))
myrectangle.width = 10
print("{} - {}".format(myrectangle.width, myrectangle.height))
# Expected: 2 - 4
# Expected: 10 - 4

myrectangle = Rectangle(2, 4)
print("{} - {}".format(myrectangle.width, myrectangle.height))
myrectangle.height = 10
print("{} - {}".format(myrectangle.width, myrectangle.height))
# Expected: 2 - 4
# Expected: 2 - 10
