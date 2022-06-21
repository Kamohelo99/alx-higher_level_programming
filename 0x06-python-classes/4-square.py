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

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        size = self.__size
        return (size) ** 2
