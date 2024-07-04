class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        class instantiation
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}".format(self.__size)
