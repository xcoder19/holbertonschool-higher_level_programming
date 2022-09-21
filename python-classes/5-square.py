#!/usr/bin/python3
"""class square"""


class Square:
    """class square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
            return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.__size == 0):
            print('')
        for x in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print('')
obj = Square(4)
obj.my_print()