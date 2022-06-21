#!/usr/bin/python3

"""square class with a private method """


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
