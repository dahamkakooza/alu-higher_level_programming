#!/usr/bin/python3
""" triangle module importing geometry """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ rectange class inherit from Base geometry """

    def __init__(self, width, height):
        """ init class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

        def area(self):
            """ override implement area """
            return (self.__width * self.__height)

        def __str__(self):
            """" area string represent """
            return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
r = Rectangle(1, 4)
print(r.area())  # Output: 4
print(r)         # Output: [Rectangle] 1/4

r = Rectangle(1411, 781)
print(r.area())  # Output: 1101991
print(r)         # Output: [Rectangle] 1411/781

r = Rectangle(5, 5)
print(r.area())  # Output: 25
print(r)         # Output: [Rectangle] 5/5
