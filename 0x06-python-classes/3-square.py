#!/usr/bin/python3

"""square class with an area method """


class Square:

    """Square class """

    def __init__(self, size=0):
        """
        The __init__ method
        """
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        size = self.__size
        return (size) ** 2
